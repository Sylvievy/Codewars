package org.example;

public class five {
    public static int multiply(int number) {
        int num=Math.abs(number);
        int digitNum=String.valueOf(num).length();
        int multiplier=(int)Math.pow(5, digitNum);
        return number*multiplier;
    }

    public static void main(String[] args){
        System.out.println(multiply(3));
        System.out.println(multiply(10));
        System.out.println(multiply(200));
        System.out.println(multiply(0));
        System.out.println(multiply(-3));
    }
}
