import javax.swing.JOptionPane;

public class Ejercicio9 {

    // Pide por teclado el nombre, edad y salario y muestra el salario
    // Si es menor de 16 no tiene edad para trabajar
    // Entre 19 y 50 años el salario es un 5 por ciento más
    // Entre 51 y 60 años el salario es un 10 por ciento más
    // Si es mayor de 60 el salario es un 15 por ciento más

    public static void main(String[] args) throws Exception {
        
        JOptionPane.showInputDialog(null,"Enter your name");
        int age = Integer.parseInt(JOptionPane.showInputDialog(null, "Enter your age")); 
        int salary = Integer.parseInt(JOptionPane.showInputDialog(null, "Enter your salary"));

        if(age < 16){

            JOptionPane.showMessageDialog(null,"You are not old enought to work");

        }else if(age < 19){

            JOptionPane.showMessageDialog(null,"Yoursalary is: "+salary);

        }else if(age <= 50){

            JOptionPane.showMessageDialog(null,"Your new salary is: "+(salary+salary*0.05));

        }else if(age <= 60){

            JOptionPane.showMessageDialog(null,"Your new salary is: "+(salary+salary*0.1));

        }else if(age > 60){

            JOptionPane.showMessageDialog(null,"Your new salary is: "+(salary+salary*0.15));

        }

    }
}
