# Additive Number

# Additive number is a string whose digits can form additive sequence.

# A valid additive sequence should contain at least three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.

# For example:
# "112358" is an additive number because the digits can form an additive sequence: 1, 1, 2, 3, 5, 8.

# 1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
# "199100199" is also an additive number, the additive sequence is: 1, 99, 100, 199.
# 1 + 99 = 100, 99 + 100 = 199
# Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.

# Given a string containing only digits '0'-'9', write a function to determine if it's an additive number.

# Follow up:
# How would you handle overflow for very large input integers?

import sys

class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """

        length = len(num) #3
        for i in range((length - 1)/2):
            print "reached this point"
            if num[0] == '0' and i >= 1: # no leading 0's!
                break

            for j in range(i + 1, min(length - (i+1), (length+i)/2) + 1):
                if num[i+1] == '0' and j - i > 1:
                    break

                init1 = int(num[:i+1])
                # print "init1 = %d"%init1
                init2 = int(num[i+1:j+1])
                # print "init2 = %d"%init2
                remaining = num[j+1:]
                # print "remaining = %s"%remaining

                if self.isAdditive(remaining, init1, init2):
                    return True
        return False

    def isAdditive(self, remain, num1, num2):
        if remain == "":
            return True 

        net = num1 + num2
        net_str = str(net)
        if not remain[:len(net_str)] == net_str:
            return False

        return self.isAdditive(remain[len(net_str):], num2, net)


if __name__ == '__main__':
    num = str(sys.argv[1])
    s = Solution()
    print s.isAdditiveNumber(num)

