# Vanilla code to calculate 1st quartile, median and 3rd quartile of an array.

n = int(input())
x = sorted(list(map(int, input().split())))


if type((len(x)/4)) == int:
    print(x[(len(x)/4 + 1)])

if type((len(x)/4)) != int:



if len(x) % 2 != 0:
    print(x[len(x)/2])
    

# Nested lists
# https://www.hackerrank.com/challenges/nested-list/problem

if __name__ == '__main__':
    python_students = []
    scores = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        python_students.append([name, score])
        scores.append(score)

minkey = min(scores)
scores2 = set(scores)
scores2.remove(minkey)
minkey2 = min(scores2)

newlist = []
for sublists in python_students:
    for val in sublists:
        if val == minkey2:
            newlist.append(sublists[0])
        
newlist = sorted(newlist)
for i in newlist:
    print(i)

    
### Diagonal Difference algo
    # https://www.hackerrank.com/challenges/diagonal-difference/problem

def diagonalDifference(arr):
    DR = []
    DL = []
    for i in range(0, n):
        DR.append(arr[i][i])
        DL.append(arr[i][(n-1-i)])
    return abs((sum(DR) - sum(DL)))

### grade rounding up
    # https://www.hackerrank.com/challenges/grading/problem
def gradingStudents(grades):
    
    for i in range(grades_count):

        if grades[i] >= 38 and grades[i] < 40:
            grades[i] = 40

        if grades[i] > 40:
            for z in range(1,3):
                if (grades[i] + z) % 5 == 0:
                    grades[i] = (grades[i] + z)
                    break

    return grades 

### birthday cake candles,
    # https://www.hackerrank.com/challenges/birthday-cake-candles/problem
def birthdayCakeCandles(ar):
    count = 0

    sorted_ar = sorted(ar, reverse=True)
    z = sorted_ar.count(max(sorted_ar))

    for i in range(z):
        count = count + 1

    return count

### kangaroo
    # https://www.hackerrank.com/challenges/kangaroo/problem
def kangaroo(x1, v1, x2, v2):
    if (v2-v1 == 0): # parallel lines never intersect
        return("NO")
    
    if ( (x1-x2) / (v2-v1) ) > 0 and int(((x1-x2) / (v2-v1))) == ((x1-x2) / (v2-v1)):
        return ("YES") # general algebraic equality form

    else: # all other cases
        return ("NO")

### between 2  sets,
    # https://www.hackerrank.com/challenges/between-two-sets/problem
def getTotalX(a, b):

    # this is my first draft of code, definitely a challenging problem, im starting
    # to learn the basics of algorithmic complexity and O notation,
    between_counter = 0
    last_arr_counter = 0
    last_arr_counter_brr = 0
    joint_counter = 0

    # first 3 loops just checks arr[-1] for inclusive set, this code is not
    # very efficient in my opinion, definitely not generalizable as well
    for i in range(len(arr)):
        if arr[-1] % arr[i] == 0: # check last arr against every other arr for %
            last_arr_counter = last_arr_counter + 1 # counter for conditions
    
    for z in range(len(brr)):
        if brr[z] % arr[-1] == 0:
            last_arr_counter_brr = last_arr_counter_brr + 1
  
    if last_arr_counter == len(arr): 
        if last_arr_counter_brr == len(brr):
            between_counter = between_counter + 1
    
    # attempted to make this code efficient and generalizable
    # i create a list of all multiples of elements in arr that are less than
    # first element in brr so it satisfies the condition to be between 2 sets,
    arr_multiples_bet = []

    for n in range(len(arr)):
        for j in range(1, int(brr[0]/arr[n])+1):
            if (arr[n]*j) > arr[-1] and (arr[n]*j) <= brr[0]:
                arr_multiples_bet.append(arr[n]*j)
    
    arr_multiples_bet = list(set(arr_multiples_bet)) # remove duplicates
    combined = arr + brr # combine list to make iteration easier
    # debugger print(arr_multiples_bet)
    # debugger print(combined)

    # check each multiple to be a factor for both arr and brr list with combined list
    # make a counter that resets after each outer loop iteration or each multiple
    # if multiple is a factor for everything(arr+brr), it triggers counter + 1,
    # if not, it resets before going onto the next multiple to be checked,
    for k in range(len(arr_multiples_bet)):

        joint_counter = 0

        for l in range(len(combined)):

            if arr_multiples_bet[k] == combined[l]:
                joint_counter = joint_counter + 1

            if arr_multiples_bet[k] > combined[l]:
                if arr_multiples_bet[k] % combined[l] == 0:
                    joint_counter = joint_counter + 1
            
            if arr_multiples_bet[k] < combined[l]:
                if combined[l] % arr_multiples_bet[k] == 0:
                    joint_counter = joint_counter + 1
            
            if joint_counter == len(combined):
                between_counter = between_counter + 1

    return between_counter
            
### /breaking-best-and-worst-records
    # https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem
def breakingRecords(scores):
    copy = []
    least_count = 0
    high_count = 0
    for i in range(n):
        copy.append(scores[i])
        if i >= 1:
            if copy[i] == min(copy):
                if copy.count(copy[i]) == 1:
                    least_count = least_count + 1
            if copy[i] == max(copy):
                if copy.count(copy[i]) == 1:
                    high_count = high_count + 1
                    
    return high_count, least_count
