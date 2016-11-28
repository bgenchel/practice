"""
Given an array A = {a1, a2, ..., aN} of N elements, find the maximum possible 
sum of a

Contiguous subarray
Non-contiguous (not necessarily contiguous) subarray.
Empty subarrays/subsequences should not be considered.

Input Format

First line of the input has an integer.  cases follow.
Each test case begins with an integer. In the next line,  integers follow 
representing the elements of array .

Constraints

The subarray and subsequences you consider should have at least one element.

Output Format

Two, space separated, integers denoting the maximum contiguous and non-contiguous 
subarray. At least one integer should be selected and put into the subarrays 
(this may be required in cases where all elements are negative).

Sample Input

2
4
1 2 3 4
6
2 -1 2 3 4 -5
Sample Output

10 10
10 11
Explanation

In the first case:
The max sum for both contiguous and non-contiguous elements is the sum of ALL 
the elements (as they are all positive).

In the second case:
[2 -1 2 3 4] --> This forms the contiguous sub-array with the maximum sum.
For the max sum of a not-necessarily-contiguous group of elements, simply add all the positive elements.
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
num_cases = int(raw_input())

inputs = []
for _ in range(num_cases):
    throw_away = raw_input()  # don't need this for python
    inputs.append([int(x) for x in raw_input().split()])

def solve(array):
    max_contiguous = kudane(array)
    max_non_contiguous = not_kudane(array)
    return max_contiguous, max_non_contiguous

def kudane(array): # max contiguous subarray
    max_ending_here = max_so_far = array[0]
    for x in array[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_ending_here, max_so_far)
    return max_so_far

def not_kudane(array): # max non contiguous subarray
    max_so_far = array[0]
    for x in array[1:]:
            max_so_far = max(x, max_so_far, max_so_far + x)
    return max_so_far

for input_array in inputs:
    contig, noncontig = solve(input_array)
    print "%d %d"%(contig, noncontig)
