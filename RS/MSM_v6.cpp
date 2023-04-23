#include <iostream>
#include <ctime>
#include <vector>
#include <random>
#include <chrono>
#include <fstream>
using namespace std;


// TOPPLE function
void topple(int size, int site, vector<int> &m)
{
    //static std::random_device rd;
    //static std::mt19937 gen(rd());

    for(int a = 0; a < 2; a++) {
        m[site] = m[site] - 1;

        // Generate a random probability between (0,1)
        //static std::uniform_real_distribution<double> dist(0.0, 1.0);
        //double r = dist(gen);

        double r = (double)rand() / RAND_MAX;
 
        // Particle moves left or right with 1/2 probability each
        if (r < 0.5) {
            int i = (site + size - 1) % size;
            m[i] = m[i] + 1;
        } 
        else {
            int j = (site + 1) % size;
            m[j] = m[j] + 1;
        }
    }
}

// dynamics function
void func(vector<double> &sigma, vector<double> &rhoS, double M) 
{ 
    const int tf = 2000000;
    const int ts = 1000000;
    const int L = 1000;
    const int R = 1;
    int curr = M;

    double FM = 0;
    double SM = 0;
    double S = 0;
    double sig = 0;
    double rho = 0;

    // Use the current time as a random seed
    //unsigned seed = std::chrono::system_clock::now().time_since_epoch().count();
    //std::mt19937 gen(seed);

    // REALIZATION loop
    for (int r = 0; r < R; r++) { 

        // Initialize a vector to represent the sites
        std::vector<int> m(L, 0);
        
        while (curr != 0) {
            int rgP  = (int)rand() % (curr+1);
            curr = curr - rgP;
            int rgL = rand() % L;
            m[rgL] = m[rgL] + rgP;
        }

        // MACRO LOOP
        for (int t = 0; t < tf; t++) {
            
            // MICRO LOOP            
            for (int tm = 0; tm < L; tm++) {

                    // Selecting a random site
                    //std::uniform_int_distribution<> distrib(0, L - 1);
                    //int ran_S = distrib(gen);

                int ran_S = (int)(L * ((double)rand() / RAND_MAX));

                // Check for active sites and topple if active
                if (m[ran_S] > 1) {
                    topple(L, ran_S, m);
                }
            }

            if(t > ts) {
                FM = FM + m[0];
                SM = SM + pow(m[0],2);         
            }
        }            
        
    }
    
    FM /= (double)(R * (tf - ts));
    SM /= (double)(R * (tf - ts));
    sig = SM - pow(FM, 2);
    rho = M / L;
    sigma.push_back(sig);
    rhoS.push_back(rho);
    //cout << "rho = " << rho << ", sigma = " << sig << endl;
    
}

int main()
{
    srand(time(0));
    double M = 950;
    vector<double> sigma, rhoS;

    // Open a file for writing
    ofstream outfile("MSM_v6.1.csv");

    // Write the header row
    outfile << "RHO,SIGMA SQUARED" << endl;

    int i = 0;
    while (M <= 990) {
        
        // For different values of Rho
        func(sigma, rhoS, M);
        if ((M >= 950 && M <= 965)) {
            M += 1;
        } 
        else {
            M += 2;
        }
        outfile << (rhoS[i] - 0.950) << "," << sigma[i] << endl;
        std::cout << (rhoS[i]  - 0.950) << " " << sigma[i] << endl;
        i++;
    }

    // Close the file
    outfile.close();   
}