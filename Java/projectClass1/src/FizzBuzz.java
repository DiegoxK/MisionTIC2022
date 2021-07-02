import java.util.Scanner;

public class FizzBuzz {
    public static void main(String[] args) throws Exception {

        Scanner scan = new Scanner(System.in);

        try{

            System.out.print("number: ");
            int number = scan.nextInt();

            if (number%5 == 0 && number%3 == 0)
                System.out.println("FizzBuzz");
            else if (number%3 == 0)
                System.out.println("Buzz");
            else if (number%5 == 0)
                System.out.println("Fizz");
            else
                System.out.println(number);

        }
        finally{

            scan.close();
            
        }

    }
}
