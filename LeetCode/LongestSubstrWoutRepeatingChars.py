"""
Title: Longest Substring Without Repeating Characters
Difficulty: Medium

Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer
must be a substring, "pwke" is a subsequence and not a substring.
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0

        charr = list(s)
        lastfound = {}
        begin = 0
        maxlen = 0
        for last in xrange(len(charr)):
            if charr[last] not in lastfound:
                print "{} not yet seen in substring".format(charr[last])
                lastfound[charr[last]] = last
            else:
                print "{} already in substring, moving things forward".format(charr[last])
                begin = max(begin, lastfound[charr[last]] + 1)
                lastfound[charr[last]] = last

            print "begin: {}, last: {}, lastfound: {}".format(begin, last, lastfound)
            currlen = (last - begin) + 1
            if currlen > maxlen:
                maxlen = currlen
        return maxlen

