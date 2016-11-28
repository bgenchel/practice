import sys


class Solution(object):
    seen = set()

    def sum_of_digit_squares(self, n):
        ret = 0
        for digit in [int(digit) for digit in str(n)]:
            ret += digit**2
        return ret

    def isHappy(self, n, depth=0):
        """
        :type n: int
        :rtype: bool
        """
        if depth == 0:
            self.seen.clear()
        # print n
        if n in self.seen:
            return False
        else:
            self.seen.add(n)

        s = self.sum_of_digit_squares(n)
        if s == 1:
            return True
        else:
            return self.isHappy(s, depth=depth+1)


if __name__ == '__main__':
    s = Solution()
    print s.isHappy(sys.argv[1])
