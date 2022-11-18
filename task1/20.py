print('введите кол-во строк в словаре, который нужно перевернуть')
n = int(input())
i=0
dic = []
print('введите сам словарь построчно, всего', n, 'строк')
while i < n:
  ss=input().split(' - ')
  ss.reverse()
  line=' - '.join(ss)
  dic.append(line)
  i+=1
i=0
while i < n:
  print(dic[i])
  i+=1
