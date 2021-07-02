import java.util.Scanner;

public class Ejercicio5{

    // 5. Generar un número aleatorio entre el 1 y el 100, el usuario lo tiene que
    // adivinar introduciendo el número por teclado. En el caso que el número a
    // adivinar sea mayor al ingresado, decirle al usuario “El número que busca es
    // mayor”, de lo contrario, “El número que busca es menor”. El programa
    // finalizará cuando se introduzca el número correcto. Nota: usar la clase
    // Random para generar el número aleatorio.

    public static void main(String[] args) {

        int number = (int) (Math.random()* 100);
        Scanner scan = new Scanner(System.in);

        while(true){

            System.out.print("Ingrese su numero: ");
            int userNumber = scan.nextInt();

            if (number < userNumber){

                System.out.print("El numero que busca es menor!\n");

            } else if (number > userNumber){

                System.out.print("El número que busca es mayor!\n");
                
            } else if (number == userNumber){

                System.out.print("Felicidades!");

                break;

        }
    }

    }
    
}