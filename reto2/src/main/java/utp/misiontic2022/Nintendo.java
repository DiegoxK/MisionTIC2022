package utp.misiontic2022;

public class Nintendo extends Consola {

    private final String GENERACION_BASE = "Nintendo 64";
    private final int MICROSD = 32;
    private String generacion;
    private int microsd;

    public Nintendo(){

        microsd = MICROSD;
        generacion = GENERACION_BASE;
    
    }

    public Nintendo(double precioBase, String color) {
        super(precioBase, color);
        generacion = GENERACION_BASE;
        microsd = MICROSD;
    }

    public Nintendo(double precioBase, String color, String generacion) {
        super(precioBase, color);
        this.generacion = generacion;
        microsd = MICROSD;
    }

    public Nintendo(double precioBase, String color, String generacion, int microsd) {
        super(precioBase, color);
        this.generacion = generacion;
        this.microsd = microsd;
    }

    @Override
    public double precioFinal() {

        int adicionGeneracion = 0;
        int adicionMicrosd = 0;
        
        
        if(generacion.equals("Nintendo 64")){

            adicionGeneracion = 30_000;

        }else if(generacion.equals("Nintendo Wii")){

            adicionGeneracion = 200_000;

        }else if(generacion.equals("Nintendo switch")){

            adicionGeneracion = 500_000;

        }else{

            adicionGeneracion = 0;
        }

        if(microsd == 32){

            adicionMicrosd = 10000;

        }else if(microsd == 128){

            adicionMicrosd = 50_000;

        }

        return super.precioFinal() + adicionGeneracion + adicionMicrosd;

    }

    

}
