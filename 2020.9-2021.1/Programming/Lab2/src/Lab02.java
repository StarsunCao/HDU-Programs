import java.lang.Math;
import java.util.Scanner;
public class Lab02 {
	public static double getValue(double x) {

		double result = Double.NaN;
		
		if (x >= -3 && x <= -2) {
				result = -x - 2;
		}
		else if (x > -2 && x < 0) {
			result = Math.sqrt(1 - (x + 1) * (x + 1));
		}
		else if (x >= 0 && x <= 4) {
			result = -Math.sqrt(4 - (x - 2) * (x - 2));
		}
		else if (x > 4 && x <= 6) {
			result = -0.5 * x + 2;
		}
		else if (x > 6 && x <= 7) {
			result = -1;
		}
		return result;
	}
	
	public static double readDouble(String message) {
		System.out.print(message);
		Scanner scanner = new Scanner(System.in);
		double val = scanner.nextDouble();
		return val;
	}
	
	public static void main(String[] args) {
		double min = readDouble("Enter the minimum value of the range of X: ");
		double max = readDouble("Enter the maximum value of the range of X: ");
		double dx = readDouble("Enter the step (dx): ");
		for (double x = min; x < max; x += dx) {
			double y = getValue(x);
			System.out.println(String.format("Y = f(%.2f) = %.2f", x, y));
		}
	}
}
