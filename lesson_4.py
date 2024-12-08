#Task 1

string = input('Введите строку: ')
a = 0
b = 0
c = ""
for i in string:
    if i == 'н':
        b += 1
    if b > a:
        a = b
        c = 'н' * a
    else:
        b = 0
for n in string:
    if n == 'н':
        string = string.replace('н', "!")
print("Самая длинная послдовательность букв 'н':", c)
print("Преобразованная строка:", string)

#Task 2

s = input('Введите строку: ')
for i in '[{':
  s=s.replace(i,'(')
for i in '}]':
  s=s.replace(i,')')
for i in range(len(s)):
    if s[i]=='(':
        a=i
    elif s[i]==')':
        b=i
print(s[a+1:b])


# Task 3

s = input('Введите строку: ')
s=s.split()
a=''
for i in s:
    if i[0].lower()=='а'and i[-1]=='я':
        a+= i + ' '
print(a)
