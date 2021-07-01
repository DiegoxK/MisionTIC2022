import java.text.NumberFormat;
import java.util.Scanner;

public class mortgageCalculator {
    public static void main(String[] args) throws Exception {
        
        final byte MONTHS_OF_THE_YEAR = 12;
        final byte PERCENT = 100;

        Scanner scanner = new Scanner(System.in);
        
        int principal;
        while (true) {

            System.out.print("Principal ($1K - $1M): ");
            principal = scanner.nextInt();

            if (principal >= 1000 && principal <= 1_000_000)
                break;

            System.out.println("Enter a number between 1,000 and 1,000,000.");
        }

        float interestRate;
        while(true){

            System.out.print("Annual Interest Rate (%): ");
            interestRate = scanner.nextFloat();

            if (interestRate > 0 && interestRate <= 30)
                    break;

            System.out.println("Enter a value greater than 0 and less than or equal to 30");
        }

        byte period;
        while(true){

            System.out.print("Period (Years): ");
            period = scanner.nextByte();

            if (period > 0 && period <= 30)
                    break;

            System.out.println("Enter a value between 1 and 30");
        }

        float monthlyInterest = interestRate/PERCENT/MONTHS_OF_THE_YEAR;
        double numberOfPayments = period * MONTHS_OF_THE_YEAR;

        double mortgage = principal
                        * (monthlyInterest * Math.pow(1 + monthlyInterest, numberOfPayments))
                        / (Math.pow(1 + monthlyInterest, numberOfPayments)-1);

        NumberFormat currency = NumberFormat.getCurrencyInstance();

        System.out.println("Mortgage: "+ currency.format(mortgage));
    }
}
