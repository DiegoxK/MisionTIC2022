package utp.misiontic2022;


public class Consola {

    protected final String COLOR_BASE = "negro";
    protected final double PRECIO_BASE = 500000.0;
    protected double precioBase;
    protected String color;

    public Consola() {

        precioBase = PRECIO_BASE;
        color = COLOR_BASE;

    }

    public Consola(double precioBase, String color) {
        
        this.precioBase = precioBase;
        this.color = color;

        comprobarColor();

    }

    public void comprobarColor(){

        //Menuda depresion c;

    }

    public double getPrecioBase() {

        return precioBase;

    }

    public String getColor() {

        return color;

    }

    public double precioFinal(){

        int adicion = 100_000;

        if(color.equals("blanco")){

            adicion = 70_000;

        }else if(color.equals("rojo")){

            adicion = 50_000;

        }

        double precioFinal = precioBase + adicion;

        return precioFinal;
        
    }

}
