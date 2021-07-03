public class oddOrEven {
    /*Write a java program that read a integer variable and assign it a value, then show a message indicating whether
    the variable is odd or even.
    Use the conditional opertror (? : ) to solve the problem.
    */

    public static String discriminator(int number){

        String conditional = number%2 == 0 ? "even" : "odd";
        return conditional;

    }

    public static void main(String[] args) throws Exception {
        
        int number;
        number = (int)(Math.random()*100);
        System.out.println("The number: "+number+" is " + discriminator(number));

    }
}
