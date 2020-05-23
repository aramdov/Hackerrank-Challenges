Vanilla code to calculate 1st quartile, median and 3rd quartile of an array.

n = int(input())
x = sorted(list(map(int, input().split())))


if type((len(x)/4)) == int:
    print(x[(len(x)/4 + 1)])

if type((len(x)/4)) != int:



if len(x) % 2 != 0:
    print(x[len(x)/2])
    

Nested lists
https://www.hackerrank.com/challenges/nested-list/problem

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
