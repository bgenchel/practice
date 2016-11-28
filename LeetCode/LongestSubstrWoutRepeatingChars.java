/**
 * Title: Longest Substring IWthout Repeating Characters
 * Difficulty: Medium
 *
 * Given a string, find the length of the longest substring without repeating characters.
 * Examples:
 *  Given "abcabcbb", the answer is "abc", which is length 3
 *  Given "bbbb", the answer is "b", with the length of 1
 *  Given "pwwkew", the answer is "wke", with a the length of 3.
 *      note that "pwke" is a subsequence, not a substring.
*/

import java.util.*;

public class LSSWROC{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();
        System.out.println(lengthOfLongestSubstring(input));
    }

    public static int lengthOfLongestSubstring(String s){
        char[] charr = s.toCharArray();
        if(charr.length == 0)
            return 0;

        HashMap<Character, Integer> lastfound = new HashMap<Character, Integer>();
        int begin = 0, length = 0;
        for(int last = 0; last < charr.length; last++){
            System.out.println("begin: " + begin + " last: " + last);
            System.out.println("charr[last] = " + charr[last]);
            if(!lastfound.containsKey(charr[last]))
                lastfound.put(charr[last], last);
            else{
                System.out.println("found reocurring character");
                begin = Math.max(begin, lastfound.get(charr[last]) + 1);
                lastfound.put(charr[last], last);
            }
            int curr_length = (last - begin) + 1;
            System.out.println("lenght = " + length);
            System.out.println("(last - begin) + 1 = " + curr_length);
            if(curr_length > length)
                length = curr_length;
            System.out.print('\n');
        }
        return length;
    }
}
