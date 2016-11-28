"""
Title: DUNGEON GAME
Difficulty: Hard

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

my notes (EDIT 1127116: these notes were taken prior to finding the correct, dp solution):
    Need not the shortest path, but the path along which the minimum initial positive
    does not go to zero at any point. So, need to account for large negative accumulation at the front
    even if it later balances. SO this is not a shortest path problem.

    Need a conjunction of shortest total path, with checks of periods of change from positive o negative
    to ensure a positive balance. Specifically, need to make sure that he makes it past the beginning.

    Could alternate between largest positive and

    could run djikstra's (however need to account for the possibility of negative paths
    would want the path with the lowest absolute value at the end), though shortest weighted path is not guarenteed.
        Also, could just recursively try every path and return the smallest sum.
"""


def revrange(start, end=0):
    ret = []
    s = start - 1
    while s >= end:
        ret.append(s)
        s -= 1
    return ret


class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        rows = len(dungeon)
        cols = len(dungeon[0])
        min_life = [[0]*cols for _ in xrange(rows)]

        if dungeon[rows-1][cols-1] >= 0:
            min_life[rows-1][cols-1] = 1
        else:
            min_life[rows-1][cols-1] = 1 - dungeon[rows-1][cols-1]

        for i in revrange(rows-1):
            if dungeon[i][cols-1] >= 0:
                min_life[i][cols-1] = max(min_life[i+1][cols-1] - dungeon[i][cols-1], 1)
            else:
                min_life[i][cols-1] = min_life[i+1][cols-1] - dungeon[i][cols-1]

        for j in revrange(cols-1):
            if dungeon[rows-1][j] >= 0:
                min_life[rows-1][j] = max(min_life[rows-1][j+1] - dungeon[rows-1][j], 1)
            else:
                min_life[rows-1][j] = min_life[rows-1][j+1] - dungeon[rows-1][j]

        for i in revrange(rows-1):
            for j in revrange(cols-1):
                if dungeon[i][j] >= 0:
                    r_result = max(min_life[i][j+1] - dungeon[i][j], 1)
                    d_result = max(min_life[i+1][j] - dungeon[i][j], 1)
                else:
                    r_result = min_life[i][j+1] - dungeon[i][j]
                    d_result = min_life[i+1][j] - dungeon[i][j]
                min_life[i][j] = min(r_result, d_result)

        return min_life[0][0]
