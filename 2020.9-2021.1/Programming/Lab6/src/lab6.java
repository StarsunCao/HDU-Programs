import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;
import java.util.LinkedList;
import java.util.Scanner;

public class lab6 {
  
  public static ArrayList<task> todolist = new ArrayList<task>();
  
  public static void printTask(task theTask) {
    System.out.println("Title:"+theTask.getTitle());
    System.out.println("Discription:"+theTask.getDiscription());
    System.out.println("Deadline:"+theTask.getDeadline());
    System.out.println("Tags:");
    LinkedList<String> tags = theTask.getTags();
    for(int k = 0;k < tags.size();k++) {
      System.out.println((k+1)+"."+tags.get(k));
    }
  }
  
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    Scanner scanner2 = new Scanner(System.in);
    
    Boolean run = true;
    while(run) {
      System.out.println("Enter the number of action and press [Enter]. Then follow instructions.\r\n"
          + "Menu:\r\n"
          + "1. Add task\r\n"
          + "2. Search task\r\n"
          + "3. Last tasks\r\n"
          + "4. Exit");
      int scan = scanner.nextInt();
  
      if (scan == 1) {
        
        System.out.println("Title:");
        String title = scanner2.nextLine();
        task newtask = new task(title);
  
        System.out.println("Description:");
        String description = scanner2.nextLine();
        newtask.setDescription(description);
        
        System.out.println("Deadline(yyyy-MM-dd):");
        String deadline = scanner2.nextLine();
        newtask.setDeadline(deadline);
        
        System.out.println("Tags(finish on empty line)");
        int i = 1;
        String tag;
        do {
          System.out.println(i+".");
          
          tag = scanner2.nextLine();
          
          System.out.println(tag.length());
          System.out.println("tag = " + tag);
          
          newtask.addTags(tag);
          i++;
        }while(tag.length()!= 0);
      //}while(!tag.isEmpty());
        
        
        System.out.println("Add the new task successfully!");
        System.out.println();
        
        todolist.add(newtask);
        
      }else if(scan == 2){
        System.out.println("Search by tag:");
        String inputTag = scanner.next();
        Boolean istheretask = false;
        for(int i = 0;i < todolist.size();i++) {
          LinkedList<String> tags = todolist.get(i).getTags();
          for(int j = 0;j < tags.size();j++) {
            if(tags.get(j).equals(inputTag)) {
              istheretask = true;
              printTask(todolist.get(i));
              System.out.println();
              break;
            }
          }
        }
        
        if(istheretask == false)
        System.out.println("No such tasks");
        System.out.println();
        
      }else if(scan == 3) {
        String lastDeadline = todolist.get(0).getDeadline();
        SimpleDateFormat df = new SimpleDateFormat("yyyy-MM-dd");
        for(int i = 1;i < todolist.size();i++) {
          try {
            Date sd1 = df.parse(lastDeadline);
            Date sd2 = df.parse(todolist.get(i).getDeadline());
            if(sd1.getTime() >= sd2.getTime()) {
              lastDeadline = todolist.get(i).getDeadline();
            }
          }catch(ParseException e1) {
            e1.printStackTrace();
          }
        }
        System.out.println("Actual tasks:");
        System.out.println();
        for(int i = 0;i < todolist.size();i++) {
          if(todolist.get(i).getDeadline().equals(lastDeadline)) {
            printTask(todolist.get(i));
            System.out.println();
          }
        }
      }else if(scan == 4) {
        run = false;
        System.out.println("Exited successfully!");
      }else {
        System.out.println("Please enter the correct number.");
      }
    }
  }

}