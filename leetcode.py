### Duplicates zeros (Part of Arrays Learning Module)
# https://leetcode.com/problems/duplicate-zeros/
from itertools import islice

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        # lem = 0
        nums = iter(range(len(arr)))
        for i in nums:
            
            # print(i)
            
            if arr[i] == 0:
                
                k = len(arr)-1
                
                while k > i:
                    arr[k] = arr[k-1]
                    k = k - 1
                
                # print(arr)
                # print(i)
                
                if i == len(arr)-1: 
                    break
                else:
                    next(nums)
                
                
        return arr
    
### Find numbrs with even # of digits (Part of Arrays Learning Module)
# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        
        counter = 0
        
        for i in range(len(nums)):
            var = nums[i]
            count = 0
            
            while (var > 0):
                count = count + 1
                var = var//10
                
            if count % 2 == 0:
                counter = counter + 1
                
        return counter
    


