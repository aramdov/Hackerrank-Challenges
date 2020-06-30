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
