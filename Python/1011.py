# Capacity To Ship Packages Within D Days

class Solution(object):
    def shipWithinDays(self, weights, days):
        left = max(weights)
        right = sum(weights)
        while left <= right:
            mid = (left + right) // 2
            count = 1
            total = 0
            for i in weights:
                if total + i > mid:
                    count += 1
                    total = 0
                total += i
            if count > days:
                left = mid + 1
            else:
                right = mid - 1
        return left
