import java.io.*;
import java.util.*;

public class rotateArray{
    public static void main(String[] args){
        int[] nums = {1, 2};
        int k = 1;
        Solution sol = new Solution();
        sol.rotate(nums, k);
    }

    public static class Solution {

        public void rotate(int[] nums, int k) {
            if(nums.length == 1 || k == 0)
                return;
            LinkedList<Integer> q = new LinkedList<Integer>();
            int rotate_point = (nums.length - k);
            rotate_point += (rotate_point < 0 ? nums.length : 0);
            for(int i = rotate_point; i < nums.length; i++){
                System.out.println("first for loop");
                System.out.println(nums[i]);
                q.add(nums[i]);
            }
            for(int i = 0; i < rotate_point; i++){
                System.out.println("second for loop");
                System.out.println(nums[i]);
                q.add(nums[i]);
            }
            int i = 0;
            while(!q.isEmpty()){
                nums[i] = q.poll();
                System.out.println("in while loop");
                System.out.println(nums[i]);
                i++;
            }
        }

    }
}