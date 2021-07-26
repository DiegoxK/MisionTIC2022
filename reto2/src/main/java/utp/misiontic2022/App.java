package utp.misiontic2022;
public class App 
{
    public static void main( String[] args )
    {
       
        Consola consolas1[] = new Consola[7];
        consolas1[0] = new Consola(0.0, "blanco");
        consolas1[1] = new Xbox(1500000.0, "rojo", "Xbox");
        consolas1[2] = new Nintendo(1000000.0, "rojo", "Nintendo 64", 32);
        consolas1[3] = new Consola();
        consolas1[4] = new Consola(600000.0, "rojo");
        consolas1[5] = new Xbox();
        consolas1[6] = new Nintendo();
        PrecioTotal precio1 = new PrecioTotal(consolas1);
        precio1.mostrarTotales();


    }
}
