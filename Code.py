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
