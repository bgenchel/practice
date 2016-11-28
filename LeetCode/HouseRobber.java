import java.io.*;
import java.util.*;

public class HouseRobber{
    public static void main(String[] args){
        int[] num = {2, 7, 9, 3, 1};
        rob(num);
    }

    public static int rob(int[] num) {
        if(num.length == 0)
            return 0;
        int[] max = new int[num.length];
        for(int i = 0; i < num.length; i++){
            System.out.println("index = " + i);
            if(i == 0)
                max[i] = num[i];
            else if(i == 1)
                max[i] = Math.max(num[0], num[i]);
            else {
                int step =  2;
                if(i - step != 0){
                    step += (num[i - step] < num[i - (step + 1)]) ? 1 : 0;
                    System.out.println("step = " + step);
                }
                System.out.println("prevmax = " + max[i - 1]);
                System.out.println("newmax = " + (num[i] + max[i - step]));
                max[i] = Math.max(max[i - 1], num[i] + max[i - step]);
            }
            System.out.println("max = " + max[i]);
        }
        return max[num.length - 1];
    }
}