/* DUNGEON GAME (hard)

The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon. 
The dungeon consists of M x N rooms laid out in a 3D grid. Our valiant knight (K) was initially 
positioned in the top-left room and must fight his way through the dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer. If at any point his health
point drops to 0 or below, he dies immediately.

Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering
these rooms; other rooms are either empty (0's) or contain magic orbs that increase the knight's 
health (positive integers).

In order to reach the princess as quickly as possible, the knight decides to move only rightward or
downward in each step.

Write a function to determine the knight's minimum initial health so that he is able to rescue 
the princess.

For example, given the dungeon below, the initial health of the knight must be at least 7 if he 
follows the optimal path RIGHT-> RIGHT -> DOWN -> DOWN.

-2(K)   -3     3
-5	    -10    1
10      30	  -5(P)


Notes:

The knight's health has no upper bound.
Any room can contain threats or power-ups, even the first room the knight enters and the bottom-right 
room where the princess is imprisoned.

Credits:
Special thanks to @stellari for adding this problem and creating all test cases. */

/*my notes:
	Need not the shortest path, but the path along which the minimum initial positive
	does not go to zero at any point. So, need to account for large negative accumulation at the front
	even if it later balances. SO this is not a shortest path problem.

	Need a conjunction of shortest total path, with checks of periods of change from positive o negative
	to ensure a positive balance. Specifically, need to make sure that he makes it past the beginning.

	Could alternate between largest positive and

	could run djikstra's (however need to account for the possibility of negative paths
	would want the path with the lowest absolute value at the end), though shortest weighted path is not guarenteed.
	Also, could just recursively try every path and return the smallest sum.
*/


import java.io.*;
import java.util.*;
import java.Collections.*;


public class Solution {
    public int calculateMinimumHP(int[][] dungeon) {
        int rows = dungeon.length, cols = dungeon[0].length;
        //dynamic programming array
        int[][] min_life = new int[rows][cols];

        if(dungeon[rows - 1][cols - 1] >= 0)
            min_life[rows - 1][cols - 1] = 1;
        else
            min_life[rows - 1][cols - 1] = 1 - dungeon[rows - 1][cols - 1];
        for(int i = rows - 2; i >=0; i--){
            if(dungeon[i][cols-1] >= 0)
                min_life[i][cols-1] = Math.max(min_life[i+1][cols-1] - dungeon[i][cols-1], 1);
            else
                min_life[i][cols-1] = min_life[i+1][cols-1] - dungeon[i][cols-1];
        }

        for(int j = cols - 2; j >=0; j--){
            if(dungeon[rows-1][j] >= 0)
                min_life[rows-1][j] = Math.max(min_life[rows-1][j+1] - dungeon[rows-1][j], 1);
            else
                min_life[rows-1][j] = min_life[rows-1][j+1] - dungeon[rows-1][j];
        }

        for(int i = rows - 2; i >= 0; i--){
            for(int j = cols - 2; j >= 0; j--){
                int r_result = 0, d_result = 0;
                if(dungeon[i][j] >= 0){
                    r_result = Math.max(min_life[i][j+1] - dungeon[i][j], 1);
                    d_result = Math.max(min_life[i+1][j] - dungeon[i][j], 1);
                } else {
                    r_result = min_life[i][j+1] - dungeon[i][j];
                    d_result = min_life[i+1][j] - dungeon[i][j];
                }
                min_life[i][j] = Math.min(r_result, d_result);
            }
        }

        return min_life[0][0];
    }
}

