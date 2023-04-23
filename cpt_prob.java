import java.util.*;
import java.io.FileWriter;
import java.io.IOException;



class CPT {
	
    Random rand = new Random();

    //    CHIPPING FUNCTION
     public void chipping (int[] m, int i, int L) {
    	
        double x = rand.nextDouble();
		int j=0;

        if (x<0.5) {
            j = (i + 1) % L;
        }
        else {
            j = (i + L - 1) % L;
        }

        m[j] = m[j] + 1;
        m[i] = m[i] - 1;
    }

    //    DIFFUSING FUNCTION
     public void diffuse (int[] m, int i, int L) {

        double x = rand.nextDouble();
        int j=0;

        if (x<0.5) {
            j = (i + 1) % L;
        }
        else{
            j = (i + L - 1) % L;
        }

        m[j] = m[j]+m[i];
        m[i]=0;
    }

    //    FUNCTION FOR REALIZATION LOOP AND MONTE CARLO LOOP
    public void dynamics (int[] m, int R, int L, int tf, int ts, double den, double[] prob) {


        Random rand = new Random();

//      REALIZATION LOOP
        for (int r = 0; r < R; r++) {
        int rgn = 0;
        int curr = (int)(den*(double)L);
            while (curr!=0) {
                curr = curr - rgn;
                rgn = rand.nextInt((curr+1));
                int a = rand.nextInt(L);
                m[a] = m[a] + rgn;
            }

            for (int t = 0; t <tf ; t++) {
                for (int tm = 0; tm < L; tm++) {
                    int i = rand.nextInt(L);
					double p = rand.nextDouble();
                    if (m[i]>0){
                        if(p<0.5){
                        	chipping(m, i, L);
						}
                        else{
                        	diffuse(m, i, L);
						}                        
                    }
                }
                if(t>ts){
                    prob[m[0]] =  prob[m[0]] + 1;
                }
            }
        }

        
	}

}

class cpt_prob{
    public static void main(String[] args) throws IOException {
        
		long startTime = System.nanoTime();
        int L =1000;
        int ts = 1000000;
        int tf = 2000000;
        int R=1;
		
        double den = 0.2;
        int[] m = new int[L];
        double[] prob = new double[(int)(den*L)+1];

		CPT cpt = new CPT();

        cpt.dynamics(m, R, L, tf, ts, den, prob);

		String path = "cpt_mass_dist_rho=0.2.csv";
		FileWriter csvwriter = new FileWriter(path);

		try{
            csvwriter.append("m");
            csvwriter.append(",");
            csvwriter.append("P(m)");
            csvwriter.append(",");
            csvwriter.append("\n");
            csvwriter.flush();
        } catch(IOException e){
            System.out.println("Error occurred while writing CSV file: " + e.getMessage());
		}

		for (int i = 0; i < (int)(den*L)+1; i++) {
			prob[i] /= (R*(tf-ts));
			System.out.print(prob[i] + ", ");
			try {
            	csvwriter.append(String.valueOf(i));
            	csvwriter.append(",");
            	csvwriter.append(String.valueOf(prob[i]));
            	csvwriter.append(",");
            	csvwriter.append("\n");
            	csvwriter.flush();
        	} catch(IOException e){
            	System.out.println("Error occurred while writing CSV file: " + e.getMessage());
			}
		}



        long endTime = System.nanoTime();
        double time =(double)(endTime - startTime)/(double)1000000000;

        System.out.println("Time taken to run the code is " +time+ " s");
    }
}