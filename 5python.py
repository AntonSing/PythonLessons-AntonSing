#Task 1

def tang(a1, a2):

   tan = a2 / a1
   return tan
x1 = int(input())
x2 = int(input())
y1 = int(input())
y2 = int(input())
z1 = int(input())
z2 = int(input())
if tang(x1, x2) < tang(y1, y2) < tang(z1, z2):
   print(f'X({x1, x2})')
elif tang(y1, y2) < tang(x1, x2) < tang(z1, z2):
   print(f'Y({y1, y2})')
else:
   print(f'Z({z1, z2}')

#Task 2

n = int(input('Введите чило: '))
lst = [True for _ in range(n+1)]
i = 1
while 2*i*(i + 1) < n:
    j = i
    while j <= (n - i) / (2*i + 1):
        lst[2*i*j + i + j] = False
        j = j + 1
    i = i + 1
for i in range(1, n+1):
    elem = lst[i]
    if elem:
        prime = 2*i + 1
        if prime > n: break
        a = bin(prime)[2:]
        b = bin(prime)[2:][::-1]
        if a == b:
            print(prime, end=' ')