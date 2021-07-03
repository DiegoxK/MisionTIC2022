import java.util.Scanner;

public class celciusToFarenheit {

    /*Write a program that reads a number of degrees celcius and converts them to degrees fahrenheit 
      the formula is:  F = 32 + ( 9 * C / 5)
    */

    public static void main(String[] args) throws Exception {
        
        Scanner sc = new Scanner(System.in);
        
        try{

            System.out.println("Enter a degree celcius: ");
            float celcius = sc.nextFloat();
            

            System.out.println("Your degree celcius: "+ celcius+ "° To fahrenheit is: " + (32+(9*celcius/5))+"°f");

        }
        finally{
            sc.close();
        }
    }
}
