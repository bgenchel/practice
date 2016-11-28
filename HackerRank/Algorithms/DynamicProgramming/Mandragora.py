"""
The evil forest is guarded by N vicious mandragoras. Each ith mandragora has Hi health
points (1 <= i <= N).

Garnet and her pet begin their journey through the evil forest with S = 1 strength points
and P = 0 experience points. For each undefeated mandragora , she can perform either of the following actions:

    1. Garnet's pet eats mandragora i. This increments S by 1 and defeats mandragora i.
    2. Garnet's pet battles mandragora i. This increases P by S*Hi experience points and defeats mandragora i.

Each mandragora can only be defeated once, and Garnet can defeat the mandragoras in any order.
Given the respective health points for each mandragora, can you find the maximum number
of experience points she can earn from defeating all N mandragoras?

Input Format

The first line contains an integer, T, denoting the number of test cases. Each test
case is described over two lines:

    1. The first line contains a single integer, N, denoting the number of
        mandragoras in the forest.
    2. The second line contains N space-separated integers describing the respective
        health points for the mandragoras (i.e., H1, H2, ..., HN).

Constraints
    * 1 <= T <= 1e5
    * 1 <= N <= 1e5
    * 1 <= Hi <= 1e7, where 1 <= i <= N
    * The sum of all Ns in a single test case is <= 1e6

Output Format

For each test case, print a single line with an integer denoting the maximum
number of experience points that Garnet can earn.

Sample Input

    1
    3
    3 2 2

Sample Output

    10

Explanation

There are N = 3 mandragoras having the following health points: H = [3, 2, 2].
Initially, S = 1 and P = 0. The following is an optimal sequence of actions for
achieving the maximum number of experience points possible:

    1. Eat the second mandragora (H1 = 2). S is increased from 1 to 2, and P is
        still 0.
    2. Battle the first mandragora (H0 = 3). S remains the same, but P increases 
        by S*H0 = 2*3 = 6 experience points.
    3. Battle the third mandragora (H2 = 2). S remains the same, but P increases 
        by S*H2 = 2*2 = 4 experience points.

Garnet earns P = 6 + 4 experience points, so we print 10 on a new line.
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

def solve(healths):
    healths.append(0)  # pad for back reference
    healths.sort()  # nlogn
    subrange_health = sum(healths)  # n

    S = 0
    exp = []
    for i in range(len(healths)):  # n
        S += 1
        subrange_health -= healths[i]
        exp.append(S*subrange_health)

    return max(exp)


num_cases = int(raw_input())
for _ in range(num_cases):
    throw_away = raw_input()
    print solve([int(n) for n in raw_input().split()])

