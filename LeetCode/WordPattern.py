"""
Word Pattern

Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter
in pattern and a non-empty word in str.

Examples:
pattern = "abba", str = "dog cat cat dog" should return true.
pattern = "abba", str = "dog cat cat fish" should return false.
pattern = "aaaa", str = "dog cat cat dog" should return false.
pattern = "abba", str = "dog dog dog dog" should return false.
Notes:
You may assume pattern contains only lowercase letters, and str contains
lowercase letters separated by a single space.
"""
import sys


class Solution(object):
    def wordPattern(self, pattern, string):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        string_list = string.split(' ')
        if len(string_list) != len(pattern):
            return False

        forward_mapping = dict()
        reverse_mapping = dict()
        for i in range(len(pattern)):
            if pattern[i] not in forward_mapping.keys():
                forward_mapping[pattern[i]] = string_list[i]
            if string_list[i] not in reverse_mapping.keys():
                reverse_mapping[string_list[i]] = pattern[i]

            if forward_mapping[pattern[i]] != string_list[i]:
                return False
            if reverse_mapping[string_list[i]] != pattern[i]:
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    pattern = sys.argv[1]
    string = sys.argv[2]
    print s.wordPattern(pattern, string)
