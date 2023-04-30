#include <iostream>
#include <ctime>
#include <vector>
#include <random>
#include <chrono>
#include <fstream>
using namespace std;


void chipping(int size, int site, vector<int> &m){
	double r = (double)rand() / RAND_MAX;
    int j;
    if (r<0.5) {
		j = (site + 1) % size;
    }
    else{
        j = (site + size - 1) % size;
        }
    m[j] = m[j] + 1;
	m[site] = m[site] - 1;      
}

void diffuse(int size, int site, vector<int> &m){
	double r = (double)rand() / RAND_MAX;
    int j;
    if (r<0.5) {
    	j = (site + 1) % size;
    }
    else{
        j = (site + size - 1) % size;
    }
    m[j] = m[j]+m[site];
	m[site] = 0;
}



//Ddynamics function
void func(vector<double> &sigma, vector<double> &rhoS, double rho, vector<double> &sigmaA) 
{ 
    const int tf = 200000;
    const int ts = 100000;
    const int L = 100;
    const int R = 1;
    int curr = (int)(rho*L);

    double FM = 0;
    double SM = 0;
    double S = 0;
    double sig = 0;
    

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

                int ran_S = (int)(L * ((double)rand() / RAND_MAX));

                // Check for active sites and topple if active
                
                if (m[ran_S]>0){
                    chipping(L, ran_S, m);
				}
				else{
					diffuse(L, ran_S, m);
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
    double v = (rho * (1 + rho) * (1 + (rho*rho))) / (1 - (2 * rho) - (rho*rho));
    sigma.push_back(sig);
    rhoS.push_back(rho);
	sigmaA.push_back(v);
    cout << "rho = " << rho <<  ", FM = " << FM << ", SM = " << SM << ", Sigma Square Model = " << sig << ", Sigma Square Analytical = " << v << endl;
    
}

int main()
{
	auto start_time = chrono::high_resolution_clock::now();
    srand(time(0));
    double rho = 0.0;
    vector<double> sigma, rhoS, sigmaA;

    // Open a file for writing
    ofstream outfile("cpt_sigmasq.csv");

    // Write the header row
    outfile << "Rho,Sigma Squared Model,Sigma Square Analytical" << endl;


	for(int i=1; i<18; i++){
		if(i<8){
			rho = rho + 0.05;
			func(sigma, rhoS, rho, sigmaA);
			outfile << rhoS[i] << "," << sigma[i] << "," << sigmaA[i] << endl;
		}
		else{
			rho = rho + 0.01;
			func(sigma, rhoS, rho, sigmaA);
			outfile << rhoS[i] << "," << sigma[i] << "," << sigmaA[i] << endl;
		}
		//else{
		//	rho = rho + 0.001;
		//	func(sigma, rhoS, rho, sigmaA);
		//	outfile << rhoS[i] << "," << sigma[i] << "," << sigmaA[i] << endl;
		//}
	}

    // Close the file
    outfile.close(); 

    auto end_time = chrono::high_resolution_clock::now();
    auto duration = chrono::duration_cast<chrono::seconds>(end_time - start_time).count();

    cout << "Runtime: " << duration << " seconds" << endl;

	return 0;
  
}