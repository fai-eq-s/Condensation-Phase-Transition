import java.util.*;
import java.io.FileWriter;
import java.io.IOException;


/*
L = 100, 200, 400, 600, 800, 1000
*/


public class cpt_4 {

    

    //    CHIPPING FUNCTION
    public static void chipping(int[] m, int i, int L){
		Random rand1 = new Random();
        int j;
        if (rand1.nextBoolean()) {
            j = (i + 1) % L;
        }
        else{
            j = (i + L - 1) % L;
        }
        m[j] = m[j] + 1;
        m[i] = m[i] - 1;
    }
    //    DIFFUSING FUNCTION
    public static void diffuse(int[] m, int i, int L){
        Random rand2 = new Random();
        
        int j;
        if (rand2.nextBoolean()) {
            j = (i + 1) % L;
        }
        else{
            j = (i + L - 1) % L;
        }
        m[j] = m[j]+m[i];
        m[i]=0;
    }

    //    FUNCTION FOR REALIZATION LOOP AND MONTE CARLO LOOP
    public static void dynamics(Vector<Double> sigmaModel, Vector<Double> rhos, double rho, Vector<Double> sigmaAnalytic, int[] m, int R, int L, int tf, int ts, FileWriter csvwriter){
    	

        double FM = 0;
        double SM = 0;
        

        //        REALIZATION LOOP
        for (int r = 0; r < R; r++) {
			int rgn = 0;
        	int curr = (int)(rho*L);
            while (curr!=0) {
				Random rand3 = new Random();
                curr = curr - rgn;
                rgn = rand3.nextInt((curr+1));
                int a = rand3.nextInt(L);
                m[a] = m[a] + rgn;
            }
            for (int t = 0; t <tf ; t++) {
                for (int tm = 0; tm < L; tm++) {
					Random rand4 = new Random();
					Random rand5 = new Random();
                    int i = rand4.nextInt(L);
                    if (m[i]>0){
                        chipping(m, i, L);
					}
					else{
						diffuse(m, i, L);
					}
                }
                if(t>ts){
                    FM = FM + m[0];
                    SM = SM + m[0]*m[0];
                    
                }
            }
        }
        FM = FM/(R*(tf-ts));
        SM = SM/(R*(tf-ts));
        double sigma2 = SM-(FM*FM);
        sigmaModel.add(sigma2);
        rhos.add(rho);
        double v = (rho * (1 + rho) * (1 + (rho*rho))) / (1 - (2 * rho) - (rho*rho));
        sigmaAnalytic.add(v);
        System.out.println("rho = " + (double)rho+ ", FM = "+FM+", SM = "+SM+", sigmaModel = " +sigma2+ ", sigmaAnalytic = " + v);
        write(rho, sigma2, v, csvwriter);
    }

    // WRITING VALUES TO CSV
    public static void write(double r, double sigma2, double v, FileWriter csvwriter){
        try{
            csvwriter.append(String.valueOf(r));
            csvwriter.append(",");
            csvwriter.append(String.valueOf(r*r));
            csvwriter.append(",");
            csvwriter.append(String.valueOf(sigma2));
            csvwriter.append(",");
            csvwriter.append(String.valueOf(v));
            csvwriter.append("\n");
            csvwriter.flush();
        } catch(IOException e){
            System.out.println("Error occurred while writing CSV file: " + e.getMessage());
        }
    }
	public static void main(String[] args) throws IOException {
        long startTime = System.nanoTime();
        Vector<Double> sigmaModel = new Vector<>();
        Vector<Double> rhos = new Vector<>();
        Vector<Double> sigmaAnalytic = new Vector<>();
        int tf= 2000000;
        int ts= 1000000;
        int L = 1000;
		
        int R=1;
		double rho = 0.0;
		

        String path = "cpt_trial6.csv";

        FileWriter csvwriter = new FileWriter(path);

		try{
            csvwriter.append("ρ");
            csvwriter.append(",");
            csvwriter.append("ρ*ρ");
            csvwriter.append(",");
            csvwriter.append("σ²-Model");
            csvwriter.append(",");
            csvwriter.append("σ²-Analytical");
            csvwriter.append("\n");
            csvwriter.flush();
        } catch(IOException e){
            System.out.println("Error occurred while writing CSV file: " + e.getMessage());
		}
        

        while(rho<0.414) {
			
			if(rho<=0.35){
				rho+=0.05;
				int[] m = new int[L];
				dynamics(sigmaModel, rhos, rho, sigmaAnalytic, m, R, L, tf, ts ,csvwriter);
			}
			else if(rho<=0.01){
				rho+=0.05;
				int[] m = new int[L];
				dynamics(sigmaModel, rhos, rho-0.014, sigmaAnalytic, m, R, L, tf, ts ,csvwriter);
			}
			else {
				rho+=0.001;
				int[] m = new int[L];
				dynamics(sigmaModel, rhos, rho, sigmaAnalytic, m, R, L, tf, ts ,csvwriter);
			} 
        }
        long endTime = System.nanoTime();
        double time =(double)(endTime - startTime)/(double)1000000000;
		
        System.out.println("Time taken to run the code is " +time+ " s");
        System.out.println("With L = " +L+ ", R = " +R);

    }


     
}



// cpt_data_ss.csv -> L=1024, tf = 12000000, ts = 6000000
// cpt_data_ss1.csv -> L=1024, tf = 25000000, ts = 10000000
// cpt_trial1.csv -> L=1000, tf = 12000000, ts = 6000000, R = 10
// cpt_trial2.csv -> L=100, tf = 1200000, ts = 600000, R = 10
// cpt_trial3.csv -> L=1000, tf = 12000000, ts = 6000000, R = 1
// cpt_trial4.csv -> L=100, tf = 6000000, ts = 3000000, R = 100