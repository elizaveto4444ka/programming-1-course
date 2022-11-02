#6
a = input()
b = input()
if a == b:
print('Пароль принят')
else:
print('Пароль не принят')
#7
a = input()

if a % 2 == 0:
print('Четное')
else:
print('Нечетное')
#8
n = int(input())
c = 'детство' if n <= 13 else 'молодость' if n <= 24 else 'зрелость' if n <= 59 else 'старость'
print (c)
#9
y=int(input())
if y % 4 == 0:
print('YES')
else:
print('NO')
#10
n= int(input())
k = int(input())
if n > k:
print('NO')
elif k > n:
print('YES')
else:
print("Don't know")
