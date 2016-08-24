## 374. Guess Number Higher or Lower(EASY)
##
## We are playing the Guess Game. The game is as follows:
##
## I pick a number from 1 to n. You have to guess which number I picked.
##
## Every time you guess wrong, I'll tell you whether the number is higher or lower.
##
## You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):
##
## -1 : My number is lower
##  1 : My number is higher
##  0 : Congrats! You got it!
##
## Example:
##
## n = 10, I pick 6.
##
## Return 6.
class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        end = n
        my_pick = int((start + end) / 2)
        while guess(my_pick) != 0:
            if guess(my_pick) == 1:
                start = my_pick + 1
            else:
                end = my_pick - 1
            my_pick = int((start + end) / 2)
        return my_pick
