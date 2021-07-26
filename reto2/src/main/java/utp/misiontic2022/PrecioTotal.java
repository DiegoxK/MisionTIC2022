package utp.misiontic2022;

public class PrecioTotal {
    
    private double sumaConsola = 0;
    private double sumaXbox = 0;
    private double sumaNintendo = 0;
    private Consola[] consolas;

    public PrecioTotal(Consola consolas[]){

        this.consolas = consolas;

    }

    public void mostrarTotales(){

        for (int i = 0; i<consolas.length; i++){

            if(consolas[i] instanceof Nintendo){

                sumaNintendo += consolas[i].precioFinal();
                sumaConsola += consolas[i].precioFinal();

            }else if(consolas[i] instanceof Xbox){

                sumaXbox += consolas[i].precioFinal();
                sumaConsola += consolas[i].precioFinal();

            }else if(consolas[i] instanceof Consola){

                sumaConsola += consolas[i].precioFinal();

            }

        }

        System.out.println("La suma del precio de las Consolas es de " + sumaConsola);
        System.out.println("La suma del precio de los Xbox es de " + sumaXbox);
        System.out.println("La suma del precio de los Nintendos es de " + sumaNintendo);
        
    }

}
