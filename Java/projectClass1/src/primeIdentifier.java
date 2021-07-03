import javax.swing.JOptionPane;

public class primeIdentifier {

    // Aks a number, check if the number is prime then ask if the user wants to enter another number
    public static void main(String[] args) throws Exception {
        
        int counter = 0;

        while(true){

            int number = Integer.parseInt(JOptionPane.showInputDialog(null, "Enter a number"));

            for(int i=2; i<number ;i++){

                if(number%i==0){
                    counter++;
                    break;
                }else{
                    continue;
                }
                
            }

            if(counter == 0){
                JOptionPane.showMessageDialog(null,"This number is prime");
            }else{
                JOptionPane.showMessageDialog(null,"This number is not prime");
            }

            String[] continues = {"Yes","No"};
            String dialogWindow = (String) JOptionPane.showInputDialog(null, "Do you want check another number?","Select your answer",JOptionPane.QUESTION_MESSAGE,null,continues,continues[0]);

            if(dialogWindow.equals("Yes")){
                continue;
            }else{
                break;
            }
        }

    }
}
