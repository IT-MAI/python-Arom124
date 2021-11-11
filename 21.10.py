#1
print("Введите список чисел через пробел")
a=[int(i) for i in input().split()]
print("Введите число, которое хотите удалить из списка")
k=int(input())
for it in a[:]:
    if it==k:
        a.remove(it)
print("Список без выбранного вами числа:")
print(a)

#2
a = int(input())
if a == 0:
    print(0)
else:
    fib_prev, fib_next = 0, 1
    n = 1
    while fib_next <= a:
        if fib_next == a:
            print(n)
            break
        fib_prev, fib_next = fib_next, fib_prev + fib_next
        n += 1
    else:
        print(-1)

#3
print("Введите список чисел через пробел")
l=[int(i) for i in input().split()]
l.sort()
print("Второй максимум списка равен",l[-2])

#4
b=[int(s) for s in input().split()]
par=0
for i in range(len(b)):
    for j in range(i+1, len(b)):
        if b[i]==b[j]:
            par+=1
print("Количество пар одинаковых чисел равно",p)

#5
print("Введите список чисел")
d=[int(s) for s in input().split()]
for i in range(len(d)):
    for j in range(len(d)):
        if i!=j and d[i]==d[j]:
            break
    else:
        print("Элементы встречающиеся в данном списке один раз:")
        print(d[i], end=' ')

#6
print("Введите список чисел")
e=[int(i) for i in input().split()]
for i in range(1, len(e), 2):
    e[i - 1], e[i] = e[i], e[i - 1]
print("Список с переставленными элементами:")
print(' '.join([str(i) for i in e]))

#7
print("Введите список чисел")
a = [int(s) for s in input().split()]
print("Введите индекс одного из элементов")
k = int(input())
for i in range(k + 1, len(a)):
    a[i - 1] = a[i]
a.pop()
print("Список без указанного числа:")
print(' '.join([str(i) for i in a]))

#8
print("Введите список чисел")
g=[int(s) for s in input().split()]
print("Введите индекс одного из элементов (не последнего) и число, которое хотите добавить в список через пробел")
k, C = [int(s) for s in input().split()]
g.append(0)
for i in range(len(g)-1, k, -1):
    g[i]=g[i - 1]
g[k]=C
print("Список после преобразования:")
print(' '.join([str(i) for i in g]))
