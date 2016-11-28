# Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.

# Below is one possible representation of s1 = "great":

#     great
#    /    \
#   gr    eat
#  / \    /  \
# g   r  e   at
#            / \
#           a   t
# To scramble the string, we may choose any non-leaf node and swap its two children.

# For example, if we choose the node "gr" and swap its two children, it produces a scrambled string "rgeat".

#     rgeat
#    /    \
#   rg    eat
#  / \    /  \
# r   g  e   at
#            / \
#           a   t
# We say that "rgeat" is a scrambled string of "great".

# Similarly, if we continue to swap the children of nodes "eat" and "at", it produces a scrambled string "rgtae".

#     rgtae
#    /    \
#   rg    tae
#  / \    /  \
# r   g  ta  e
#        / \
#       t   a
# We say that "rgtae" is a scrambled string of "great".

# Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.

class Solution(object):
    class Node:
        def __init__(self, string):
            self.size = len(string)
            self.string = string
            self.left = None
            self.right = None 

        def setLeft(self, node):
            self.left = node

        def setRight(self, node):
            self.right = node

    def cutInHalf(self, string):
        hp = len(string)/2
        return string[:hp], string[hp:]

    def makeTree(self, string):
        print "tree node: " + string
        n = self.Node(string)
        if n.size == 1:
            return n

        hp = len(string)/2
        leftstring, rightstring = string[:hp], string[hp:]
        n.setLeft(self.makeTree(leftstring))
        n.setRight(self.makeTree(rightstring))

        return n
    
    def sameLetters(self, s1, s2):
        print "sameLetters(" + s1 + ", " + s2 + ")"
        dict1 = {}
        for letter in s1:
            if letter in dict1:
                dict1[letter] = dict1[letter] + 1
            else:
                dict1[letter] = 1

        for letter in s2:
            if letter not in dict1:
                return False
            else:
                dict1[letter] = dict1[letter] - 1
                if dict1[letter] == 0:
                    del dict1[letter]
        
        if len(dict1) == 0:
            return True
        else:
            return False

    # def compareTrees(self, p1, p2):
    #     print "comparing " + p1.string + " and " + p2.string

    #     if p1.size == 1 and p2.size == 1:
    #         return True

    #     if not self.self.sameLetters(p1.string, p2.string):
    #         return False
    #     else:
    #         if not self.compareTrees(p1.left, p2.left):

    def checkTheTree(self, pnode, string):
        print "comparing " + pnode.string + " and " + string
        if pnode.size == 1 and len(string) == 1:
            return True

        hp1 = len(string)/2
        hp2 = (len(string) + 1)/2

        left1, right1 = string[:hp1], string[hp1:]
        left2, right2 = string[:hp2], string[hp2:]

        print "left1 = " + left1
        print "right1 = " + right1
        print "left2 = " + left2
        print "right2 = " + right2 + '\n'

        if self.sameLetters(pnode.left.string, left1) and self.sameLetters(pnode.right.string, right1):
            return self.checkTheTree(pnode.left, left1) and self.checkTheTree(pnode.right, right1)
        elif self.sameLetters(pnode.left.string, right1) and self.sameLetters(pnode.right.string, left1):
            return self.checkTheTree(pnode.left, right1) and self.checkTheTree(pnode.right, left1)
        elif self.sameLetters(pnode.left.string, left2) and self.sameLetters(pnode.right.string, right2):
            return self.checkTheTree(pnode.left, left2) and self.checkTheTree(pnode.right, right2)
        elif self.sameLetters(pnode.left.string, right2) and self.sameLetters(pnode.right.string, left2):
            return self.checkTheTree(pnode.left, right2) and self.checkTheTree(pnode.right, left2)

        return False



    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if not self.sameLetters(s1, s2):
            return False

        parent = self.makeTree(s1)
        return self.checkTheTree(parent, s2)


if __name__ == '__main__':
    sol = Solution()
    print sol.sameLetters('great', 'rgtae')
    # print sol.isScramble('great', 'rgtae')