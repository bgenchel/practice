# Given a roman numeral, convert it to an integer.
# Input is guaranteed to be within the range from 1 to 3999.

class Solution(object): 
    def romanToInt(self, s):
        print "\nconverting string " + s
        if not len(s):
            return 0
        """
        :type s: str
        :rtype: int
        """
        map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        integer = 0
        greatest = 0
        index = len(s) - 1
        substr = ""
        while index >= 0:
            print "head of while loop, on char " + s[index]
            print "current total = " + str(integer)
            print "current greatest = " + str(greatest)
            cval = map[s[index]]
            if cval < greatest:
                print "current value less than greatest"
                substr = substr + s[index]
                index = index - 1
            else:
                print "current value greater than greatest"
                integer = integer - self.romanToInt(substr)
                substr = ""

                integer = integer + cval
                index = index - 1
                greatest = cval
                
        integer = integer - self.romanToInt(substr)
        return integer
           
if __name__ == '__main__':
    s = raw_input("Enger Roman Numeral String:  ")
    sol = Solution()
    i = sol.romanToInt(s)
    print "as integer: " + str(i)