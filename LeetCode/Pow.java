//Problem Statement: 
// Implement pow(x, n).

import java.util.*;

public class Pow{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        double x = sc.nextDouble();
        int n = sc.nextInt();

        myPow p = new myPow();
        System.out.println(p.myPow(x, n));
    }
}

class myPow{
    HashMap<Integer, Double> dp = new HashMap<Integer, Double>();
    
    public double myPow(double x, int n) {
        if(n == 0)
            return 1;
        if(n == 1)
            return x;
        if(n == -1)
            return 1/x;
            
        if(!dp.containsKey(n/2))
            dp.put(n/2, myPow(x, n/2));
            
        if(n%2 == 0)
            return dp.get(n/2)*dp.get(n/2);
        else if(n < 0){
            if(!dp.containsKey(n/2 - 1));
                dp.put(n/2 - 1, myPow(x, n/2 - 1));
                
            return dp.get(n/2)*dp.get(n/2 - 1);
        }
        else{
            if(!dp.containsKey(n/2 + 1))
                dp.put(n/2 + 1, myPow(x, n/2 + 1));
                
            return dp.get(n/2)*dp.get(n/2 + 1);
        }
    }
}