import javax.swing.JOptionPane;
public class Ejercicio2{
    public static void main(String[] args) {
        String nombre_alumno=JOptionPane.showInputDialog("Ingrese el nombre del alumno");
        double nota_1=Double.parseDouble(JOptionPane.showInputDialog("Ingrese la primer nota"));
        double nota_2=Double.parseDouble(JOptionPane.showInputDialog("Ingrese la segunda nota"));
        double nota_3=Double.parseDouble(JOptionPane.showInputDialog("Ingrese la tercera nota"));

        if ((nota_1+nota_2+nota_3)/3>=3.0) {
            JOptionPane.showMessageDialog(null, nombre_alumno+ " aprobó "+ "con un promedio de"+(nota_1+nota_2+nota_3)/3);
        } else {
            JOptionPane.showMessageDialog(null,nombre_alumno+ " reprobó" + " con un promedio de: "+(nota_1+nota_2+nota_3)/3);
        }
    }
    
}