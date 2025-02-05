public class Paper
{
  public static int paperWork(int n, int m) 
  {
    if (n < 0 || m < 0){
      return 0;
    }
    else{
      return n*m;
    }

    }
    public static void main(String[] args){
        int a=paperWork(25,50);
        System.out.println(a);
  }
}