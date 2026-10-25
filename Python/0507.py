# Perfect Number

class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 1:
            return False
        value = 1
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                value += i
                if i != num // i:
                    value += num // i
        if num == value:
            return True
        else:
            return False
