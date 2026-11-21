# Last Stones Weight

class Solution(object):
    def lastStoneWeight(self, stones):
        stones.sort()
        while len(stones) > 1:
            y = stones.pop()
            x = stones.pop()

            if x != y:
                stones.append(y - x)

            stones.sort()

        return stones[0] if stones else 0
        
