import java.lang.*;
public class Lab01 {
	public static double readValue(String message) {
		java.util.Scanner s = new java.util.Scanner(System.in);
		
		System.out.print(message);
		
		return s.nextDouble();
	}
	
	public static double calcZ1(double a) {
		double numerator = Math.sin(2 * a) + Math.sin(5 * a) - Math.sin(3 * a);
		double denominator = Math.cos(a) + 1 - 2 * Math.sin(2 * a) * Math.sin(2 * a);
		
		double z1 = numerator / denominator;
		
		return z1;
	}
	
	public static double calcZ2(double a) {
		double z2 = 2 * Math.sin(a);	
		return z2;
	}
	
	public static void main(String[] args) {
		double a = readValue("Enter ¦Á: ");
		
		double z1 = calcZ1(a);
		double z2 = calcZ2(a);
		
		System.out.println("Z1 = " + z1);
		System.out.println("Z2 = " + z2);
	}

}
