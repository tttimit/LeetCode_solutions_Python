## 258. Add Digits(EASY)
##
## Given a non-negative integer num, repeatedly add all its digits
## until the result has only one digit.
##
## For example:
##
## Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since
## 2 has only one digit, return it.
##
## Follow up:
## Could you do it without any loop/recursion in O(1) runtime?
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        str_of_num = str(num)
        while(len(str_of_num) > 1):
            result = 0
            for letter in str_of_num:
                result += int(letter)
            str_of_num = str(result)
        return int(str_of_num)

# O(1) version
class Solution1(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        
