class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last, now = 0, 0
        for i in nums:
            print("i={0} last={1} now={2}".format(i, last, now))
            last, now = now, max(last + i, now)
        return now


s = Solution()
a = [1, 2, 3, 4]
print("robbed: ", s.rob(a))

## new test## new test