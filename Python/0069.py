# LeetCode 0069 - Sqrt(x)

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x
        low = 0
        high = x // 2
        ans = 1
        while low <= high:
            mid = (low + high) // 2
            sqaure = mid * mid
            if sqaure == x:
                return mid
            elif sqaure < x:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans
        
