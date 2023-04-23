import java.util.*;
import java.io.FileWriter;
import java.io.IOException;


/*
L = 100, 200, 400, 600, 800, 1000
*/


public class cpt_corr {
	
	 // cv = m[50]*m[j]
    static Random rand = new Random();
    //    CHIPPING FUNCTION
    public static void chipping(int[] m, int i, int L){
    	
        double x = rand.nextDouble();
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
    //    DIFFUSING FUNCTION
    public static void diffuse(int[] m, int i, int L){
        Random rand = new Random();
        double x = rand.nextDouble();
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

    //    FUNCTION FOR REALIZATION LOOP AND MONTE CARLO LOOP
    public static void dynamics(int[] m, int R, int L, int tf, int ts, FileWriter csvwriter, double den, double[] cv){
        
        double FM = 0;
        double SM = 0;
        Random rand = new Random();
//        REALIZATION LOOP
        for (int r = 0; r < R; r++) {
			Arrays.fill(m, 0);
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
                    if (m[i]>0){
                        double p = rand.nextDouble();
                        if (p<0.5){
                            chipping(m, i, L);
                        }
                        else{
                            diffuse(m, i, L);
                        }
                    }
                }
                if(t>ts){
                    for(int j = 0; j< L; j++){
                    	cv[j] += m[L/2]*m[j];
                    }
                }
            }
        }
        for(int j = 0; j< L; j++){
        	cv[j] /= (R*(tf-ts));
        	cv[j] -= (den*den);
        	System.out.println(cv[j]+" ");
        	try{
        		csvwriter.append(String.valueOf(L/2 - j));
        		csvwriter.append(",");
            	csvwriter.append(String.valueOf(cv[j]));
            	csvwriter.append("\n");
            	csvwriter.flush();
        	} catch(IOException ex){
            System.out.println("Error occurred while writing CSV file: " + ex.getMessage());
        	}
        }
    }



    public static void main(String[] args) throws IOException {
        long startTime = System.nanoTime();
        
        int L =1000;
        int ts = 1200000;
        int tf = 2000000;
        int R=1;

        String path = "cpt_data_corr_(L=1000, tf=2000000 , ts=1200000, R=1).csv";

        FileWriter csvwriter = new FileWriter(path);

		try{
            csvwriter.append("r");
            csvwriter.append(",");
            csvwriter.append("Cij");
            csvwriter.append(",");
            csvwriter.append("\n");
            csvwriter.flush();
        } catch(IOException e){
            System.out.println("Error occurred while writing CSV file: " + e.getMessage());
		}
        int M = 0;
        double den = 0.414;
        int[] m = new int[L];
        double[] cv = new double[L];
        dynamics(m, R, L, tf, ts ,csvwriter, den, cv);
       
        long endTime = System.nanoTime();
        double time =(double)(endTime - startTime)/(double)1000000000;
        System.out.println("Time taken to run the code is " +time+ " s");
    }
}