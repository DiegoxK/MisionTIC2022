import java.text.NumberFormat;
import java.util.Scanner;

public class mortgageCalculator {
    public static void main(String[] args) throws Exception {
        
        final byte MONTHS_OF_THE_YEAR = 12;
        final byte PERCENT = 100;

        Scanner scanner = new Scanner(System.in);
        System.out.print("Principal: ");
        int principal = scanner.nextInt();

        scanner = new Scanner(System.in);
        System.out.print("Annual Interest Rate (%): ");
        float interestRate = scanner.nextFloat();

        scanner = new Scanner(System.in);
        System.out.print("Period (Years): ");
        byte period = scanner.nextByte();

        float monthlyInterest = interestRate/PERCENT/MONTHS_OF_THE_YEAR;
        double numberOfPayments = period * MONTHS_OF_THE_YEAR;

        double mortgage = principal
                        * (monthlyInterest * Math.pow(1 + monthlyInterest, numberOfPayments))
                        / (Math.pow(1 + monthlyInterest, numberOfPayments)-1);

        NumberFormat currency = NumberFormat.getCurrencyInstance();

        System.out.println("Mortgage: "+ currency.format(mortgage));
    }
}
