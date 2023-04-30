import java.util.*;
import java.io.FileWriter;
import java.io.IOException;

public class cpt_SS_SubSys {

    //	CHIPPING FUNCTION
    public static void chipping(int[] m, int i, int L){
		Random rand = new Random();
        int j;
        if (rand.nextBoolean()) {
            j = (i + 1) % L;
        }
        else{
            j = (i + L - 1) % L;
        }
        m[j] = m[j] + 1;
		m[i] = m[i] - 1;
    }

    //	DIFFUSING FUNCTION
    public static void diffuse(int[] m, int i, int L){
        Random rand = new Random();
        int j;
        if (rand.nextBoolean()) {
            j = (i + 1) % L;
        }
        else{
            j = (i + L - 1) % L;
        }
        m[j] = m[j]+m[i];
		m[i]=0;
    }


    //	DYNAMICS
    public static void dynamics(Vector<Double> sigmaModel, Vector<Double> rhos, double rho, Vector<Double> sigmaAnalytic, int[] m, int R, int L, int tf, int ts, FileWriter csvwriter){
    	

        double FM = 0;
        double SM = 0;
        Random rand = new Random();

        //	REALIZATION LOOP
        for (int r = 0; r < R; r++) {
			int rgn = 0;
        	int curr = (int)(rho*L);
			Arrays.fill(m, 0);
            while (curr!=0) {
				curr = curr - rgn;
                rgn = rand.nextInt((curr+1));
                int a = rand.nextInt(L);
                m[a] = m[a] + rgn;
            }
		
			//	MONTE CARLO LOOP
            for (int t = 0; t <tf ; t++) {
                for (int tm = 0; tm < L; tm++) {
                    int i = rand.nextInt(L);
                    if (m[i]>0){
                        double x = rand.nextDouble();
						if(x>0.5){
							chipping(m, i, L);
						}
						else{
							diffuse(m, i, L); 
						}
					}
                }
                if(t>ts){
                    FM = FM + m[0] + m[1] + m[2] + m[3] + m[3] + m[4] + m[5] + m[6] + m[7] + m[8] + m[9];
                    SM = SM + (m[0]*m[0]) + (m[1]*m[1]) + (m[2]*m[2]) + (m[3]*m[3]) + (m[4]*m[4]) + (m[5]*m[5]) + (m[6]*m[6]) + (m[7]*m[7]) + (m[8]*m[8]) + (m[9]*m[9]);
                    
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
        int tf= 2;
        int ts= 1;
        int L = 1000;
        int R=1;
		double rho = 0.0;
		int[] m = new int[L];

        String path = "cpt_SS_SubSys.csv";

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
        
		for(int i=1; i<27; i++){
			if(i<8){
				rho = rho + 0.05;
				dynamics(sigmaModel, rhos, rho, sigmaAnalytic, m, R, L, tf, ts ,csvwriter);
			}
			else if (i<13){
				rho = rho + 0.01;
				dynamics(sigmaModel, rhos, rho, sigmaAnalytic, m, R, L, tf, ts ,csvwriter);
			}
			else {
				rho = rho + 0.001;
				dynamics(sigmaModel, rhos, rho, sigmaAnalytic, m, R, L, tf, ts ,csvwriter);
			}
		}
        
        long endTime = System.nanoTime();
        double time =(double)(endTime - startTime)/(double)1000000000;
        System.out.println("Time taken to run the code is " +time+ " s");
        System.out.println("With L = " +L+ ", R = " +R);

    }
}

