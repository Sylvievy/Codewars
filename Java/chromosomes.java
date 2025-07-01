package org.example;

public class chromosomes {
    public static String chromosomeCheck(String sperm) {
        sperm.trim();
        if (sperm.equalsIgnoreCase("XY")){
            return ( "Congratulations! You're going to have a son.");
        } else if (sperm.equalsIgnoreCase("XX")) {
            return ( "Congratulations! You're going to have a daughter.");
        }
        return "Invalid!";
    }


    public static void main(String[] args){
        System.out.println(chromosomeCheck("xX"));
        System.out.println(chromosomeCheck("xY"));
        System.out.println(chromosomeCheck("a"));
    }

}
