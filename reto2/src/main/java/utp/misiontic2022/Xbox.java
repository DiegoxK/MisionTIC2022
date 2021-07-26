package utp.misiontic2022;

public class Xbox extends Consola {

    private final String VERSION_BASE = "Xbox";
    private String version;

    public Xbox(){

        version = VERSION_BASE;

    }

    public Xbox(double precioBase, String color) {

        super(precioBase, color);
        version = VERSION_BASE;

    }

    public Xbox(double precioBase, String precioFinal, String version) {

        super(precioBase, precioFinal);
        this.version = version;

    }

    @Override
    public double precioFinal() {

        int adicion;

        if(version.equals("Xbox")){

            adicion = 50_000;

        }else if(version.equals("Xbox 360")){

            adicion = 100_000;

        }else if(version.equals("Xbox One")){

            adicion = 300_000;

        }else{

            adicion = 0;

        }

        return super.precioFinal()+ adicion;
    }
    
}
