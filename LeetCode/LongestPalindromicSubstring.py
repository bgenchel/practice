"""
Given a string S, find the longest palindromic substring in S. You may assume that the
maximum length of S is 1000, and there exists one unique longest palindromic substring.
"""

class SolutionTwo(object):
    """
    based on the more efficient solution in the comments here:
    http://codereview.stackexchange.com/questions/110079/find-all-distinct-palindromic-sub-strings-for-a-given-string/110395#110395?newreg=b4b0d21131194b6ea1541fe764260557
    this solution, like Manacher's algorithm, checks odd and even palindromes
    starting from each character in the string.

    Since it only revisits characters when they are part of a palindrome, the worst
    case time complexity is:
        O(n + n*m) = O(n*(m + 1)) = O(n*m)
    where m is the number of palindromic substrings, and the extra n is because
    you always go through the string at least one time.
    """
    def longestPalindrome(self, string):
        longest = ""
        for i, char in enumerate(string):
            # check odd palindromes
            start = end = i
            while start >= 0 and end < len(string):
                if string[start] != string[end]:
                    break
                if (end - start + 1) > len(longest):
                    longest = string[start:end + 1]
                start -= 1
                end += 1

            # check even palindromes
            start, end = i, i + 1
            while start >= 0 and end < len(string):
                if string[start] != string[end]:
                    break
                if (end - start + 1) > len(longest):
                    longest = string[start:end+1]
                start -= 1
                end += 1

        return longest



class SolutionOne(object):
    """
    My first solution, based on my idea for finding the number of palindromic
    subsequences. Getting TLE for large test cases, but the algorithm itself
    seems to be sound. I would guess O(n^2)
    """
    def checkPalindrome(self, lst, start, end):
        if end - start < 0:
            return False
        if end - start == 0:
            return True

        while start < end:
            if lst[start] != lst[end]:
                return False
            start += 1
            end -= 1
        return True

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2:
            return s

        slist = list(s)
        indices = {}
        for i in xrange(len(slist)):
            if slist[i] not in indices:
                indices[slist[i]] = []
            indices[slist[i]].append(i)

        longest_palindrome = ""
        i = 0
        while i < len(slist):
            j = len(indices[slist[i]]) - 1
            while j > 0 and indices[slist[i]][j] >= i:
                if self.checkPalindrome(slist, i, indices[slist[i]][j]):
                    if len(slist[i:indices[slist[i]][j] + 1]) > len(longest_palindrome):
                        longest_palindrome = ''.join(slist[i:indices[slist[i]][j] + 1])
                j -= 1
            i += 1

        return longest_palindrome

if __name__ == '__main__':
    inpt = raw_input("enter string:  ")
    # sol = SolutionOne()
    sol = SolutionTwo()
    print "longest palindromic substring: %s"%sol.longestPalindrome(inpt)
