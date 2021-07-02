import javax.swing.JOptionPane;

// Implemente un algoritmo que reciba un numero por teclado y cuente cuantas
// cifras (o digitos) contiene el imprima el mensaje en consola

public class numberDigits {
    public static void main(String[] args) throws Exception {

        int number = Integer.parseInt(JOptionPane.showInputDialog("Enter a number"));

        int digits = numberOfDigits(number);

        System.out.println("This number has "+digits+" digits");

    }
    public static int numberOfDigits(int number){

        int digits = 0;

        while(number != 0){

            number /= 10;
            digits++;

        }

        return digits;

    }
}
