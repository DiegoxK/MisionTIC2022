import javax.swing.JOptionPane;

public class Ejercicio3{

    // 4. Solicitar un número al usuario y mostrar la tabla de multiplicar de ese
    // número, desde el 0 hasta el 10. Truco: Usa un bucle for para recorrer la
    // tabla y mostrar los datos.
    public static void main(String[] args) {
        
        int number = Integer.parseInt(JOptionPane.showInputDialog("Ingrese el numero"));

        for(int i=0; i<=10; i++){
            JOptionPane.showMessageDialog(null,number + " x " + i + " = " + number*i);
        }
    }
    
}