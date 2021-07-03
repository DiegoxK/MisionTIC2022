import java.util.Scanner;

public class doubleTriple {

    /*Write a java program that read one integer number by input and returns
      in screen the double and triple of that number
    */

    public static void main(String[] args) throws Exception {
        
        Scanner sc = new Scanner(System.in);

        try{

            System.out.print("Enter a number: ");
            int number = sc.nextInt();

            System.out.println("The double of "+number+" is: "+number*2+" and the tripe is: "+number*3);

        }
        finally{
            sc.close();
        }

    }
}
