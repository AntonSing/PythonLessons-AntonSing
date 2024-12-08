# Task 1

import random
s=[]
matrix = [[random.randint(-10, 10) for _ in range(10)] for _ in range(10)]
for i in range(len(matrix)):
    s.append(sum(matrix[i]))
print(matrix[s.index(max(s))],max(s), matrix[s.index(min(s))],min(s))

# Task 2

from random import randint
m, n = map(int,input().split())
arr = [[randint(1, 10) for i in range(m)] for j in range(n)]
for i in arr :
    print(*i)
print()
for row in arr :
    rmin = min(row)
    row = [(1 if rmin % 2 else 0) if j == rmin else j for j in row]
    print(*row)