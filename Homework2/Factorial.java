public class Factorial {
	public static void main(String args[]) {
		
	}
	public static int fact(int n){
		if (n == 0) 
			return 1;	
		else
			return n * fact(n-1);
	}
}
