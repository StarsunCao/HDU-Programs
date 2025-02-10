import java.util.Scanner;
public class lab5 {
	
	public  static vector vectorAddition(vector vector1, vector vector2) {
		vector vector3 = new vector();
		
		double x3 = vector1.getx() + vector2.getx();
		double y3 = vector1.gety() + vector2.gety();
		double z3 = vector1.getz() + vector2.getz();
		
		vector3.setx(x3);
		vector3.sety(y3);
		vector3.setz(z3);
		
		return vector3;
	}
	
	public  static vector vectorSubtract(vector vector1, vector vector2) {
		vector vector3 = new vector();
		
		double x3 = vector1.getx() - vector2.getx();
		double y3 = vector1.gety() - vector2.gety();
		double z3 = vector1.getz() - vector2.getz();
		
		vector3.setx(x3);
		vector3.sety(y3);
		vector3.setz(z3);
		
		return vector3;
	}
	
	public  static double vectorMultiply(vector vector1, vector vector2) {

		double x3 = vector1.getx() * vector2.getx();
		double y3 = vector1.gety() * vector2.gety();
		double z3 = vector1.getz() * vector2.getz();
		
		double mult = x3 + y3 + z3;
		
		return mult;
	}
	
	public static void main(String[] args) {
		vector vector1 = new vector();
		vector vector2 = new vector();
		Scanner scanner = new Scanner(System.in);
		
		System.out.println("Enter x of vector1:");
		vector1.setx(scanner.nextInt());
		System.out.println("Enter y of vector1:");
		vector1.sety(scanner.nextInt());
		System.out.println("Enter z of vector1:");
		vector1.setz(scanner.nextInt());
		
		System.out.println("Enter x of vector2:");
		vector2.setx(scanner.nextInt());
		System.out.println("Enter y of vector2:");
		vector2.sety(scanner.nextInt());
		System.out.println("Enter z of vector2:");
		vector2.setz(scanner.nextInt());
		
		System.out.println("vector1 = " + vector1.getstr());
		System.out.println("vector2 = " + vector2.getstr());
		System.out.println("Length of vector1 = " + vector1.getlength());
		System.out.println("Length of vector2 = " + vector2.getlength());
		
		vector sum = vectorAddition(vector1,vector2);
		System.out.println("vector1 + vector2 = " + sum.getstr());
		
		vector diffrence = vectorSubtract(vector1,vector2);
		System.out.println("vector1 - vector2 = " + diffrence.getstr());
		
		double product = vectorMultiply(vector1,vector2);
		System.out.println("vector1 * vector2 = " + product);
		
	}

}
