import javax.swing.JOptionPane;

public class Ejercicio1 {

    // Realizar la suma, la resta, la división y la multiplicación de dos números
    // leídos por teclado y mostrar en pantalla “La <operación> de <número 1>
    // y <número 2> es igual a <resultado> ”.


    public static void main(String[] args) throws Exception {

        int number1 = Integer.parseInt(JOptionPane.showInputDialog(null, "Enter the first number"));
        int number2 = Integer.parseInt(JOptionPane.showInputDialog(null, "Enter the second number"));

        int sum = number1 + number2;
        int subtraction = number1 - number2;
        int division = number1 / number2;
        int multiplication = number1 * number2;

        System.out.println("The sum of "+number1+" and "+number2+" is: "+sum);
        System.out.println("The subtraction of "+number1+" and "+number2+" is: "+subtraction);
        System.out.println("The division of "+number1+" and "+number2+" is: "+division);
        System.out.println("The multiplication of "+number1+" and "+number2+" is: "+multiplication);
    }
}
