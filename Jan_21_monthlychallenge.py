# January 2021 -> Week 1. https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/579/week-1-january-1st-january-7th/3589/
class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        
        # each subarray in pieces of >1 int has to maintain its order in the "arr" array,
        # if the subarray in pieces is 1 element, easy to check if it exists in arr
        # if the subarray > 1 integer, have to check if the order is the same for pieces[i]
        # if concatenate all subarrays in pieces, all the integers are distinct (easier for us)
        # hash tables could be helpful here, get keys for arr, check pieces (length 1 sub array, and len>1   subarays). For len==1 subarray, will be easy to check for key match in dictionary. for len>1, will have to check if all the elements in the sub-array are also in order in the "Arr" array.
        
        arr_dict = {x: 0 for x in range(len(arr))} # initialize keys as integers and all values to 0
        dict_key_counter = 0 # counter throughout looping
        
        # Approach #1, get key-value pairs from arr, not the pieces array
        for element in arr:
            if element != arr_dict.get(dict_key_counter):
                arr_dict[dict_key_counter] = element
            dict_key_counter += 1
        
        # no need to check edge cases for NULL or empty input
        
        for subarray in pieces:
            if len(subarray) == 1:
                # check if it exists in arr, this is the easy case
                if subarray[0] in arr_dict.values():
                    continue
                else: return False
                
            # no need to check if len == 0, can't be < 0 either. this is from problem description
            if len(subarray) > 1:
                
                # handle edge cases if the value in pieces subarray isnt in arr
                if subarray[0] not in arr:
                    return False
                
                # find index of first element of subarray in the "arr" array
                start_index_arr = list(arr_dict.values()).index(subarray[0])
                
                #print(start_index_arr)
                #print(len(subarray))
                
                check_counter = 0
                for subelement in range(len(subarray)):
                    #print(arr[start_index_arr], subarray[subelement])
                    
                    if (start_index_arr > len(arr)-1):
                        break
                        
                    if arr[start_index_arr] == subarray[subelement]:
                        check_counter += 1
                        start_index_arr += 1
                    else:
                        return False
                    
                if check_counter == len(subarray):
                    continue
                else:
                    return False
                
        return True
        
        
########################################################

### Day 3

class Solution:
    
    def countArrangement(self, n: int) -> int:
        
        # define what is a permutation
        # either condition is true:
            # 1. Perm[i] is divisible by i (there is trivial case if permutation is ordered 1...n)
            # 2. i is divisible by perm[i] (same trivial case applies if order is ascending)
            
        # n = 3 -> {1,2,3}, {3,2,1}, {1,3,2}, {2,3,1}, {2,1,3}, {3,1,2}
            # {1,2,3} is trivial case
            # {3,2,1} -> 1. 3/1, 2/2, 1!/3. Check 2nd condition. 2. 1!/3, nope. Neither works
        
        # partial brute force by stopping computation if the permutation violates 1 of the conditions
        
        def count_beautiful_arranges(N: int, counter):
            numbers = [0]*N

            # start index at 1
            # loop creates the array of 1 to N for initial list
            for i in range(1, N+1):
                numbers[(i-1)] = i
            
            #print(counts, "inside beautiful arrange")
            # call recursive permutation function
            permutation(numbers, 0)

            
        def permutation(numbers: list, L: int):
               
            #print(counts, "inside permutation")
            # check each recursive call
            #print(L)
            #print(len(numbers))
            
            if L == len(numbers):
                permutation.countser += 1
                #print(permutation.countser, "permutation countser")
                #print("if l == len condition met")
            
            for j in range(L, len(numbers)):

                swap(numbers, j, L)
                if numbers[L] % (L+1) == 0 or (L+1) % numbers[L] == 0:
                    permutation(numbers, L+1)
                swap(numbers, j, L)
                

        
        def swap(numbers: list, x: int, y: int):
            
            #pythonic code
            numbers[x], numbers[y] = numbers[y], numbers[x]
            
        
        permutation.countser = 0
        count_beautiful_arranges(n, 0)
        return permutation.countser
    
###########################################
# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/580/week-2-january-8th-january-14th/3597/
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        
        
        word1_concat = ""
        for substring in word1:
            
            word1_concat += substring
        
        word2_concat = ""
        for substring2 in word2:
            
            word2_concat += substring2
                
        
        if len(word1_concat) != len(word2_concat):
            # obvious if length is not equal that they arent the same string
            # also prevents bugs with the approach in the next for loop iterating with indexes
            # and traversing 2 arrays of characters in parallel
            return False
        
        for char_idx in range(len(word1_concat)):
            
            if word1_concat[char_idx] != word2_concat[char_idx]:
                return False
            
        # if got to here then strings must be equal
        return True
