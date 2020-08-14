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
    


### height checker
#https://leetcode.com/problems/height-checker/
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        
        orig_copy = heights.copy()
        
        i=0
        while i < len(heights):
            
            if min(heights[i:]) != heights[i]:
                # print(heights, i)
                
                min_ind = heights[i:].index((min(heights[i:])))
                min_ind = min_ind + i
                heights[i], heights[min_ind] = heights[min_ind], heights[i]
                
                # print(heights, i)
                
            i = i + 1
        
        counter = 0
        for z in range(len(orig_copy)):
            
            if heights[z] != orig_copy[z]:
                counter = counter + 1
                
        return counter

### find pivot index
# https://leetcode.com/problems/find-pivot-index/

        if not nums:
            return -1
        # how to grab postfix_sum from presums pre-computed array?
        # z = [1, 2, 2, 4, 6], presums = [1, 3, 5, 9, 15], postsums = [15, 14, 12, 10, 6]
        # leftsum at z[0] is 1-1, rightsum is 15-1
        # leftsum at z[1] is 3-2, rightsum is 15-3
        # leftsum at z[2] is 5-2, rightsum is 15-5
        # leftsum at z[3] is 9-4, rightsum is 15-9
        # leftsum at i is presums[i]-z[i]
        # rightsum at i is presums[len(presums)-1] - presums[i]
        presums = [nums[0]]
        for h in range(1, len(nums)):
            presums.append(nums[h]+ presums[h-1])
        # nums = [1,2,2,4,6], presums = [1]
        #, h = 1 -> nums[1]=2, presums[0] = 1, presums append 3 to presums[1]
        # h = 2, -> nums[2] = 2, presums[1] = 3, presums append 5 to presums[2]
        # h=3, -> nums[3] = 4, presums[2] = 5, presums append 9 to presums[3]
        
        def leftsum(int):
            return presums[int] - nums[int]
        def rightsum(int):
            return presums[len(presums)-1] - presums[int]
        
        for n in range(len(nums)):
            if leftsum(n) == rightsum(n):
                return n
                
        # if pivotarray empty, means we found no pivot points so return -1
        # if pivotarray not empty, return first element because that is left most pivot point
        return -1

### largest number at least 2x bigger than anything else in array
#https://leetcode.com/problems/largest-number-at-least-twice-of-others/
def dominantIndex(self, nums: List[int]) -> int:
        
        maxint = max(nums) / 2
        
        # y >= 2x -> rewrite y/2 >= x
        for i in range(len(nums)):
            
            if 2*maxint == nums[i]:
                next
            elif maxint >= nums[i]:
                next
            else: 
                return -1
        return nums.index(2*maxint)
    
    # first time search of array for max value is O(n), then we store that value
    # could make this more efficient by finding the maxint and remembering its index at same time
    # if maxint comes across itself -> next
    # if maxint satisfies constraint, move on to next one
    # if constraint not matched, exit program and return -1.
