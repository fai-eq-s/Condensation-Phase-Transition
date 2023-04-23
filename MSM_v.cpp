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
    static std::random_device rd;
    static std::mt19937 gen(rd());
    for(int a = 0; a < 2; a++) {
        m[site] = m[site] - 1;

        // Generate a random probability between (0,1)
        static std::uniform_real_distribution<double> dist(0.0, 1.0);
        double r = dist(gen);

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
    double curr = M;

    double FM = 0;
    double SM = 0;
    double S = 0;
    double sig = 0;
    double rho = 0;

    // Use the current time as a random seed
    unsigned seed = std::chrono::system_clock::now().time_since_epoch().count();
    std::mt19937 gen(seed);


    // REALIZATION loop
    for (int r = 0; r < R; r++) { 

        // Initialize a vector to represent the sites
        std::vector<int> m(L, 0);

        // Distribute the particles randomly at the sites
        for (int i = 0; i < curr; i++) {
            // Generate a random index for the site
            std::uniform_int_distribution<int> site_dist(0, L - 1);
            int site_index = site_dist(gen);

            // Add a particle to the site
            m[site_index]++;
        }

            // MACRO LOOP
            for (int t = 0; t < tf; t++) {
            
                // MICRO LOOP            
                for (int tm = 0; tm < L; tm++) {

                    // Selecting a random site
                    std::uniform_int_distribution<> distrib(0, L - 1);
                    int ran_S = distrib(gen);

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
}

int main()
{
    double M = 960;
    vector<double> sigma, rhoS;

    // Open a file for writing
    ofstream outfile("MSM_v7.3.csv");

    // Write the header row
    outfile << "RHO,SIGMA SQUARED" << endl;

    int i = 0;
    while (M <= 1400) {

        func(sigma, rhoS, M);
        if ((M >= 960 && M <= 980) || (M >= 1000 && M <= 1100)) {
            M += 2;
        } 
        else {
            M += 10;
        }
        outfile << rhoS[i] << "," << sigma[i] << endl;
        std::cout << rhoS[i] << " " << sigma[i] << endl;
        i++;
    }    

    // Close the file
    outfile.close();
    
}