"""
Given a sorted array of integers, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
"""

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = self.binSearch(nums, target, 0, len(nums)-1)
        if res == -1:
            return [-1, -1]
        else:
            return res
        
    def binSearch(self, array, target, left, right):
        if left == right:
            if array[left] == target:
                end = left
                while end < len(array) and array[end] == target:
                    end += 1
                return [left, end]
            else:
                return -1
    
        mid = (right + left)/2
        if array[mid] >= target:
            res = self.binSearch(array, target, left, mid)
        else:
            res = self.binSearch(array, target, mid+1, right)
        
        return res

if __name__ == '__main__':
    s = Solution()
    res = s.searchRange([1], 1)
    print res