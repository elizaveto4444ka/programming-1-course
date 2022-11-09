print('Введите одно число n (n ≤ 100) – количество членов последовательности.')
n = int(input())
s1 = 1
s2 = 1
f = ''
for i in range(n):
 f = f + ' ' + str(s1)
s3 = s1 + s2
s1 = s2
s2 = s3
print(f)
