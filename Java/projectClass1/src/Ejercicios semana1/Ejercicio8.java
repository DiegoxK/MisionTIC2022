import java.util.HashSet;
import java.util.Set;
import javax.swing.JOptionPane;

public class Ejercicio8 {

    // 8. Realizar un programa que permita controlar el juego de piedra, papel, tijera
    // introduciendo P para piedra, L para papel y T para tijera por cada jugador.El sistema debe indicar qué jugador gana la ronda o si hay empate. Al final
    // de cada ronda preguntar si desea volver a jugar.

    public static void main(String[] args) throws Exception {
        
        while(true){

            String[] game = {"Stone","Paper","Scissors"};
            String player1 = (String) JOptionPane.showInputDialog(null, "What are you going to choose?","Player1",JOptionPane.QUESTION_MESSAGE,null,game,game[0]);
            String player2 = (String) JOptionPane.showInputDialog(null, "What are you going to choose?","Player2",JOptionPane.QUESTION_MESSAGE,null,game,game[0]);

            Set<String> set = new HashSet<>();
            set.add(player1);
            set.add(player2);

            if(set.size() == 1){

                JOptionPane.showMessageDialog(null,"Draw!");

            }else if (player1.equals("Stone") && player2.equals("Paper")){

                JOptionPane.showMessageDialog(null,"Player 2 Won!");

            }else if (player1.equals("Stone") && player2.equals("Scissors")){

                JOptionPane.showMessageDialog(null,"Player 1 Won!");

            }else if (player1.equals("Paper") && player2.equals("Stone")){

                JOptionPane.showMessageDialog(null,"Player 1 Won!");

            }else if (player1.equals("Paper") && player2.equals("Scissors")){

                JOptionPane.showMessageDialog(null,"Player 2 Won!");

            }else if (player1.equals("Scissors") && player2.equals("Stone")){

                JOptionPane.showMessageDialog(null,"Player 2 Won!");

            }else if (player1.equals("scissors") && player2.equals("Paper")){

                JOptionPane.showMessageDialog(null,"Player 1 Won!");
            }

            String[] continues = {"Yes","No"};
            String dialogWindow = (String) JOptionPane.showInputDialog(null, "Do you want to play again?","Select your answer",JOptionPane.QUESTION_MESSAGE,null,continues,continues[0]);

            if(dialogWindow.equals("Yes")){
                continue;
            }else{
                break;
            }

        }

    }
}
