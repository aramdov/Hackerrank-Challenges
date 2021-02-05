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

### Word Pattern
# https://leetcode.com/problems/word-pattern/
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        
        # count the number of characters in the "pattern" variable
        # match with the number of spaced words in "str" variable
        # this will be the first passover check, also to see if any are NULL to return False
        
        # create a hash table (dictionary) for the pattern for each unique character
        # iterate through the str and identify the value pairs for the hash table
        
        # iterate through the abba and check the matching INDEX in str for the hash value
        
        strsplit = str[0:len(str)].split(" ")
        
        mydict = {}
        indexer = 0 # turn str into an array of elements and index it with this
        
        if len(pattern) != len(strsplit):
            return False
        
        for e in pattern:
            
            if e in mydict: # avoid duplicate keys in our dict
                indexer = indexer + 1
                next
                
            elif strsplit[indexer] in mydict.values():
                    return False
                
            else: 
                mydict[e] = strsplit[indexer] # add unique char in pattern as a key
                indexer = indexer + 1
        
        for i in range(len(pattern)):
            
        
            if strsplit[i] == mydict[pattern[i]]:
                # print("it worked")
                next
            
            else:
                return False
        
        return True
            
#### Find minimum in rotated sorted array https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
## O(n) linear approach and O(log n) binary search approach

# Linear approach
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        position = 0
        sorted_counter = 0
        
        if len(nums) == 1:
            return 1
        
        while position < len(nums):
            
            if position > 0 and nums[position] < nums[position-1]:
                return nums[position]
            
            elif position > 0 and nums[position] > nums[position-1]:
                sorted_counter += 1
            
            position += 1
            
        
        if len(nums) > 1 and sorted_counter == (len(nums)-1):
            return nums[0]
        else:
            return 0    

