#1
print ("Введите два числа, значения которых вы хотите поменять")
a=int(input())
b=int(input())
c=a
d=b
print (d)
print (c)

#2
print ("Введите трехзначное число")
a=int(input())
b=a//100
c=a%10
d=(a-100*b-c)/10
x=b*c*d
print (x)

#3
print ('ведите два трехзначных числа')
a=int(input())
b=int(input())
c=1000*a+b
print (c)

#4
print ("Введите трехзначное число")
a=int(input())
b=a//100
c=a%10
x=100*b+c
print (x)

#5
print ("Введите трехзначное число")
a=int(input())
b=a//100
c=a%10
d=(a-100*b-c)/10
x=100*c+b+10*d
print (x)