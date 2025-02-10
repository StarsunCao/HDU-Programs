import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.Scanner;

public class lab4 { 

	public static void main(String[] args) {
		String path = args[0];
		File file = new File(path);
		FileReader fr = null;
		try {
			fr = new FileReader(file);
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}
		BufferedReader br = new BufferedReader(fr);
		String line;
		String[] slist = null;
		try {
			while((line = br.readLine()) != null){
				slist = line.split(" ");
			}
			for(int i = slist.length - 1; i >= 0; i--) {
				System.out.print(slist[i]+" ");
			}
		} catch (IOException e) {
			e.printStackTrace();
		}
		
		}

}
