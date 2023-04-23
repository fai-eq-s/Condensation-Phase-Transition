import java.util.Arrays;
import java.util.Random;
public class MonteCarlo
{
	public static void swap(int[] array, int i, int j) {
		int temp = array[j];
		array[j] = array[i];
		array[i] = temp;
	}		
	public static void main(String[] args)
	{
		
		int L = 3;                /* Number of Sites */
		int[] array = new int[L]; /* Array representing sites */
		int initial = 0;          /* Intial position of the particle */
		array[initial] = 1;             /* Putting the particle at the initial position */
		int finalP = 0;            /* Final position */
		double p = 0.5;           /* Probability */
		int tss = 50;             
		int count1 = 0, count2 = 0, count3 = 0;  // Count of how many times the particle finally lands on a site*/
		int T = 200;                              // Number of trials  
		for (int t = 0; t < T; t++) {
			for (int l = 0; l < L; l++) {
				double x = Math.random();
				if (x > p) {
					finalP = (finalP+1)%array.length;    // Shifting the particlet to the right nn
				}
				else{
					finalP = (finalP+array.length-1)%array.length;     // Shifting the particlet to the left nn
				}				
			}                                         // We get some j value where the particle lands after 3 micro loops
			swap(array, initial, finalP);              // Swapping the particle's position (e.g. if j came out to be 2, then {1, 0, 0} --> {0, 0, 1})
			initial = finalP;                          // Updating the initial position for next outer loop as it changed in the previous line.
			int tf = T-tss;
			if(t>tss){
				if(array[0]==1){
					count1++;
					//writer.writeNext(count1/tf);
				}
				if(array[1]==1){
					count2++;                         // Taking counts
				}
				if(array[2]==1){
					count3++;
				}
			}
		}	
		int tf = T-tss;
		System.out.print((double)count1/tf + "  " + (double)count2/tf + "  " + (double)count3/tf);      // Counting probability
	}
}