import java.io.FileWriter;
import java.io.IOException;
import java.util.Arrays;
import java.util.Random;
import java.util.Vector;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;

public class cpt_multithreading {
    private static final int NUM_THREADS = 4;
    private static final Object lock = new Object();
    private static class dynamics implements Runnable {

        private Vector<Double> sigmaModel;
        private Vector<Double> rhos;
        private Vector<Double> sigmaAnalytic;
        private static int tf;
        private static int ts;

        private static int R;
        private double rho;
        private static int L ;
        private int[] m;
        private FileWriter csvwriter;
        private double FM;
        private double SM;

        private final Random rand = new Random();

        public dynamics(Vector<Double> sigmaModel, Vector<Double> rhos, Vector<Double> sigmaAnalytic, int tf, int ts, int R, double rho, int L, int[] m, FileWriter csvwriter, double FM, double SM) {
            this.sigmaModel = sigmaModel;
            this.sigmaAnalytic = sigmaAnalytic;
            this.rhos = rhos;
            this.tf = tf;
            this.ts = ts;
            this.R = R;
            this.rho = rho;
            this.m = m;
            this.L = L;
            this.csvwriter = csvwriter;
            this.FM = FM;
            this.SM = SM;
        }

        @Override
        public void run() {

            Random rand = new Random();

            //        REALIZATION LOOP
            for (int r = 0; r < R; r++) {
                Arrays.fill(m, 0);
                int rgn = 0;
                int curr = (int)(rho*L);
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
            System.out.println("rho = " +rho+", FM = "+FM+", SM = "+SM+", sigmaModel = " +sigma2+ ", sigmaAnalytic = " + v);
            write(rho, sigma2, v, csvwriter);
        }
    }
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
    static Random rand = new Random();

    public static void main(String[] args) throws IOException {


        double FM = 0;
        double SM = 0;
        Vector<Double> sigmaModel = new Vector<>();
        Vector<Double> rhos = new Vector<>();
        Vector<Double> sigmaAnalytic = new Vector<>();
        int tf= 5000000;
        int ts= 2000000;
        int L = 1000;
        int R=5;
        double rho = 0.0;

        int[] m = new int[L];



        long startTime = System.nanoTime();


        String path = "cpt_sigma_MultiThreading.csv";

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
        ExecutorService pool = Executors.newFixedThreadPool(NUM_THREADS);
        for (int i = 0; i < NUM_THREADS; i++) {
            while(rho<0.414) {

                if(rho<0.35) {
                    rho = rho + 0.05;
                    pool.submit(new dynamics(sigmaModel, rhos, sigmaAnalytic, tf, ts, R, rho, L, m, csvwriter, FM, SM));
                }
				else if(rho<0.4){
                    rho = rho + 0.01;
                    pool.submit(new dynamics(sigmaModel, rhos, sigmaAnalytic, tf, ts, R, rho, L, m, csvwriter, FM, SM));
                }
                else{
                    rho = rho + 0.001;
                    pool.submit(new dynamics(sigmaModel, rhos, sigmaAnalytic, tf, ts, R, rho, L, m, csvwriter, FM, SM));
                }


            }

        }
        pool.shutdown();
        try {
            pool.awaitTermination(Long.MAX_VALUE, TimeUnit.NANOSECONDS);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        long endTime = System.nanoTime();
        double time =(double)(endTime - startTime)/(double)1000000000;

        System.out.println("Time taken to run the code is " +time+ " s");
        System.out.println("With L = " +L+ ", R = " +R);



    }

    public static void chipping(int[] m, int i, int L){

        double x = rand.nextDouble();
        int j;
        if (x<0.5) {
            j = (i + 1) % L;
        }
        else{
            j = (i + L - 1) % L;
        }
        synchronized (lock){
            m[j] = m[j] + 1;
            m[i] = m[i] - 1;
        }
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
        synchronized (lock){
            m[j] = m[j]+m[i];
            m[i]=0;
        }
    }
}