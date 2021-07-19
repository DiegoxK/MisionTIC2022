public class ProyectoInversion {
    
    private int tiempo = 0;
    private double capital = 0;
    private double interes = 0;

    public ProyectoInversion(){

    }

    public ProyectoInversion(int pTiempo, double pCapital, double pInteres){
        
        tiempo = pTiempo;
        capital = pCapital;
        interes = pInteres;
        
    }

    public double calcularInteresSimple(){

        double interesSimple = Math.round(capital*(interes/100)*tiempo);
        
        return interesSimple;

    }

    public double calcularInteresCompuesto(){

        double interesCompuesto = Math.round(capital * (Math.pow((1 + (interes/100)), tiempo)-1));
        
        return interesCompuesto;

    }

    public double verificarInversion(int pTiempo, int pCapital, int pInteres){

        tiempo = pTiempo;
        capital = pCapital;
        interes = pInteres;

        double diferencia = Math.round(calcularInteresCompuesto() - calcularInteresSimple());

        return diferencia;

    }

    public double verificarInversion(){
        
        double diferencia = Math.round(calcularInteresCompuesto() - calcularInteresSimple());

        return diferencia;

    }

}