import javax.swing.JOptionPane;

public class Ejercicio6 {

    // 6. Realiza un programa que solicite el sexo (H/M) y la altura (cm) al usuario y
    // que calcule el peso ideal.
    // -peso ideal mujeres = altura - 120
    // -peso ideal hombres = altura - 110


    public static void main(String[] args) throws Exception {
        
        String[] genders = {"Male","Female"};
        String gender = (String) JOptionPane.showInputDialog(null, "What is your gender?","Select your gender",JOptionPane.QUESTION_MESSAGE,null,genders,genders[0]);
        float height = Float.parseFloat(JOptionPane.showInputDialog(null,"Enter your height (cm)"));
        float idealWeight = gender.equals("Female") ? height - 120 : height -110;
        System.out.println("Your ideal weight is: "+idealWeight);

    }
}
