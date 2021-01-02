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

