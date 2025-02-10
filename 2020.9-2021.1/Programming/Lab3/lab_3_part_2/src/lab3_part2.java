import java.util.Scanner;
public class lab3_part2 {
	
	public static int countMaximum(int m,int n,int[][] matrix) {
		int max = matrix[0][0], i = 0, j = 0, sum = 0, count = 0;
		boolean flag = true;
		
		for(int times = 0; times < m+(n-1); times ++) {
			for (;i < m && j < n;) {
				sum += matrix[i][j];
				i ++;
				j ++;
			}
			
			if (sum > max) 
				max = sum;
			sum = 0;
			count ++;
			
			if (count == n) {
				count = 1;
				flag = false;
			}
			
			if (flag == true) {
				i = 0;
				j = count;
			}else {
				i = count;
				j = 0;
			}
		}
		
		count = m - 1;
		flag = true;
		for(int times = 0; times < m+(n-1); times ++) {
			for (i = m - 1;i >= 0 && j < n;) {
				sum += matrix[i][j];
				i --;
				j ++;
			}
			
			if (sum > max) 
				max = sum;
			sum = 0;
			count --;
			
			if (count < 0) {
				count = n-1;
				flag = false;
			}
			
			if (flag == true) {
				i = count;
				j = 0;
			}else {
				i = m-1;
				j = count;
			}
		}
		
		return max;
	}

	public static void main(String[] args) {
		
		Scanner scanner = new Scanner(System.in);
		System.out.println("Enter the count of columns: ");
		int columns = scanner.nextInt();
		System.out.println("Enter the count of rows: ");
		int rows = scanner.nextInt();
		int[][] matrix = new int[rows][columns];
		
		java.util.Random random = new java.util.Random();
			for (int i = 0; i < rows; i++) {
					for (int j = 0; j < columns; j++) {
						matrix[i][j] = random.nextInt(20) - 9;
					}
		}
			
				for (int i = 0; i < rows; i++) {
			for (int j = 0; j < columns; j++)
				System.out.print(matrix[i][j] + " ");
			System.out.println();
		}	
		
		//The first request
		System.out.print("Product of elements for rows having no negative elements:");		
		System.out.println();
		int[] countByRows = new int[rows];
		boolean flag = true;
		for (int i = 0; i < rows; i++)
			countByRows[i] = 1;
		for (int i = 0; i < rows; i++) {
			int countInLine = 0;
			boolean hasNegativeElement = false;
			for (int j = 0; j < columns; j++) {
				if (matrix[i][j] < 0) {
					hasNegativeElement = true;
				}
			}
			flag = flag && hasNegativeElement;
			if (!(hasNegativeElement)) {
				for(int j = 0;j < columns;j++) 
					countByRows[i] *= matrix[i][j];
				System.out.print("Row:"+ (i+1) +"  "+"Product:"+countByRows[i] + " ");
				System.out.println();
			}
		}
		if(flag) {
			System.out.print("There is no such row that has no negative elements");
			System.out.println();
		}
		
		//The second request
		int maximum = countMaximum(rows,columns,matrix);
		System.out.print("Maximum sum of elements in diagonals is:" +" "+ maximum);

	}
}
