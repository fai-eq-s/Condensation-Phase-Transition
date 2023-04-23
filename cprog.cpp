#include <iostream>
#include <vector>
#include <fstream>
#include <random>

using namespace std;

default_random_engine rand_gen;

void chipping(vector<int>& m, int i, int L){
    double x = generate_canonical<double, 10>(rand_gen);
    int j;
    if (x<0.5) {
        j = (i + 1) % L;
    }
    else{
        j = (i + L - 1) % L;
    }
    m[j] = m[j] + 1;
    m[i] = m[i] - 1;
}

void diffuse(vector<int>& m, int i, int L){
    double x = generate_canonical<double, 10>(rand_gen);
    int j;
    if (x<0.5) {
        j = (i + 1) % L;
    }
    else{
        j = (i + L - 1) % L;
    }
    m[j] = m[j]+m[i];
    m[i]=0;
}

void dynamics(vector<double>& sigmaModel, vector<double>& rhos, int M, vector<double>& sigmaAnalytic, vector<int>& m, int R, int L, int tf, int ts, ofstream& csvwriter){
    int rgn = 0;
    int curr = M;
    double FM = 0;
    double SM = 0;

    for (int r = 0; r < R; r++) {
        while (curr!=0) {
            curr = curr - rgn;
            rgn = rand_gen() % (curr+1);
            int a = rand_gen() % L;
            m[a] = m[a] + rgn;
        }
        for (int t = 0; t <tf ; t++) {
            for (int i = 0; i < L; i++) {
                double x = generate_canonical<double, 10>(rand_gen);
                if (x < rhos[i]) {
                    chipping(m, i, L);
                }
                else if (x < sigmaModel[i] + rhos[i]) {
                    diffuse(m, i, L);
                }
            }
            if (t % ts == 0) {
                double sum = 0;
                for (int i = 0; i < L; i++) {
                    sum += m[i];
                }
                double avg = sum / L;
                double var = 0;
                for (int i = 0; i < L; i++) {
                    var += (m[i] - avg) * (m[i] - avg);
                }
                var /= L;
                double sigma = sqrt(var) / avg;
                FM += avg;
                SM += sigma;
            }
        }
        double avgFM = FM / (tf / ts);
        double avgSM = SM / (tf / ts);
        sigmaAnalytic[r] = avgSM;
        FM = 0;
        SM = 0;
        curr = M;
        rgn = 0;
        for (int i = 0; i < L; i++) {
            m[i] = 0;
        }
    }
    for (int i = 0; i < R; i++) {
        csvwriter << sigmaAnalytic[i] << ",";
    }
}

int main() {
    vector<double> sigmaModel = {0.5, 0.5, 0.5, 0.5, 0.5};
    vector<double> rhos = {0.1, 0.1, 0.1, 0.1, 0.1};
    int M = 100;
    vector<double> sigmaAnalytic(10);
    vector<int> m = {0, 0, 0, 0, 0};
    int R = 10;
    int L = 5;
    int tf = 1000;
    int ts = 10;
    ofstream csvwriter;
    csvwriter.open("output.csv");
    dynamics(sigmaModel, rhos, M, sigmaAnalytic, m, R, L, tf, ts, csvwriter);
    csvwriter.close();
    return 0;
}