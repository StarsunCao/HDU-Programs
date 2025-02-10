import java.util.Arrays;
import java.util.Random;
import java.util.Scanner;

public class lab3_part1 {
	
	public static int readSize(String message) {
		
		System.out.print(message);
		
		Scanner scanner = new Scanner(System.in);
		int size = scanner.nextInt();
		
		return size;
	}
	
	public static void printArray(int[] array) {
		for (int i = 0; i < array.length; i++) {
			System.out.print(array[i] + " ");
		}
	}
	
	public static void fillArrayByRandom(int[] array) {
		Random random = new Random();
		for (int i = 0; i < array.length; i++) {
			array[i] = random.nextInt(20)-9;
		}
	}
	
	public static void fillArrayByUser(int[] array) {
		
		Scanner scanner = new Scanner(System.in);
		
		for (int i = 0; i < array.length; i++) {
			System.out.print("Enter the " + (i + 1) + " element of " + array.length);
			array[i] = scanner.nextInt();
		}
	}
	

	public static void main(String[] args) {
		
		int size = readSize("Count of elements: ");
		
		int[] array = new int[size];
		
		fillArrayByRandom(array);
		
		System.out.println("Array:");
		printArray(array);
		System.out.println();
		
		//The first request
		int product = 1;
		for (int i = 0; i < array.length; i++) {
			if (i % 2 == 1) {
				product = product * array[i];
			}
		}
		
		System.out.println("The Product of elements with even indices is: " + product);

		//The second request
		int first, last, i = 0, j = size - 1;
		
		do {
			first = array[i];
			
			i++;
			
		}while(first == 0);
		
		do {
			last = array[j];
			
			j--;
			
		}while(last == 0);
		
		int sum = first + last;
		
		System.out.println("The sum of elements resided between first and last non-zero elements is: " + sum);

		//The third request
		Arrays.sort(array);
		for (i = 0; i < array.length / 2; i++) {
			int tmp = array[i];
			array[i] = array[array.length - 1 - i];
			array[array.length - 1 - i] = tmp;
		}
		
		System.out.println("Reversed array:");
		for (i = 0; i < array.length; i++) {
			System.out.print(array[i] + " ");
		}
	}
}
