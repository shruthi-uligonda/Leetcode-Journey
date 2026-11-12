# Relative Sort Array

class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        arr1.sort()
        result = []
        for i in arr2:
            while i in arr1:
                result.append(i)
                arr1.remove(i)
        return result + arr1
        
