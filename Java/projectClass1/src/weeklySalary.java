import javax.swing.JOptionPane;

public class weeklySalary {

    // Hacer un programa que calcule e imprima
    // el salario semanal de un empleado a partir de
    // sus horas trabajadas y de su salario por hora

    public static void main(String[] args) throws Exception {

        final byte week = 7;
        double weeklySalary;
        int workHours = Integer.parseInt(JOptionPane.showInputDialog("Enter the work hours"));
        int hourSalary = Integer.parseInt(JOptionPane.showInputDialog("Enter your hour salary"));

        weeklySalary = (workHours*hourSalary)*week;

        JOptionPane.showMessageDialog(null,"Your Weekly Salary is: "+weeklySalary);
    }
}
