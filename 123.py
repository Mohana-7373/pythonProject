print(2+3+5)
print((len("yamani")))
print("python\nis        amazing")
a="yamani"
b="charan"
print(len(a + b))
print(24%5)
print(60//5)
print(type(3))
print(type("type"))
list=[1,2,3,4,5]
print(type(list))
z=(5,8,9,10)
print(type(z))
x={a,b}
print(type(x))
d={"a":"mohana"}
print(type(d))
print(id("yamani"))
list_a=[1,2,3,4]
list_b=list_a
print(id(list_a))
print(id(list_b))
list_b[3]=5
print(list_a)
print(list_b)
list_c=[1,2]
list_d=list_c
list_c=list_c+[6,7]
print(str(list_c))
print(str(list_d))
list_e=[1,2]
list_f=list_e
list_e += [6,7]
print(str(list_e))
print(str(list_f))
list_g=[1,2]
list_h=[3,list_g]
list_g[1]=4
print(list_g)
print(list_h)
numbers ="1 2 3    4"
num_list=numbers.split()
print(num_list)
numbers ="1,2,34"
num_list=numbers.split(',')
print(num_list)
numbers ="1   2 3 4"
num_list=numbers.split(" ")
print(num_list)
string_a="python is astonishing"
list_a=string_a.split('a')
print(list_a)
list_a=['python is','progr','mming l','ngu','ge']
string_a="a".join(list_a)
print(string_a)
list_i=[1,2,3,4,5]
print(list_i[4])
print(list_i[-1])
list_b=list_i[-5:-1]
print(list_b)
list_a=[5,4,3,2,1]
list_b=list_a[4:0:-2]
print(list_b)
list_b=list_a[1:4:-1]
print(list_b)
list_b=list_a[::-1]
print(list_b)
string_1="program"
string_2=string_1[6:0:-2]
print(string_2)
list_a=[1,2,3,4,5]
list_b=list_a[-4:-1:3]
print(list_b)
#write a program to read N inputs and print a list containing the first and last three inputs
N=[2,3,4,5,6,7,8,9]
B=N[0:3]
C=N[-3:]
print(B+C)

#take two integers M and N write a program to create a list with element M repeated by N times
m="10"
n=5
list_a=[m*n]
print(list_a)
#check if the first three characters of a string are same or not
a="apple"
b="Apple"
if (a[0:3]==b[0:3]):
    print(True)
else:
    print(False)
#write a program that reads two 3 digit numbers and check if the first digit of A is lessthan last digit of B
g=["532"]
h=["789"]
if(g[0]<h[-1]):
    print(True)
else:
    print(False)
#write a program to read marks in M P C.check if any of the conditions is satisfied.M>=70 and P>=60 and C>=60.M+P+C>=180.
M=70
P=60
C=60
if(M>=70 and P>=60 and C>=60):
    print("ok")
else:
    print("not ok")
if(M+P+C>=180):
    print("satisfied")
else:
    print("not satisfied")
#SWAP CASE
A="PyThOn"
B=A.swapcase()
print(B)

#REPLACE
C="dd-mm-yy"
D=C.replace("-","/")
print(D)

#PALINDROME
Cat="madam"
print(Cat[::-1]==Cat)
#password programm
import re
p="Sruthi@123"
x=True
while x:
    if (len(p)<6 or len(p)>12):
        break
    elif not re.search("[a-z]",p):
        break
    elif not re.search("[A-Z]",p):
        break
    elif not re.search("[0-9]",p):
        break
    elif not re.search("[@]", p):
        break
    else:
        print("it is a valid password")
        x=False
        break
if x:
    print("it is not a valid pw")

#print digit in ones place of a number
lst=3456
digit_at_ones_place = n % 10
print(digit_at_ones_place)
#sum of given numbers
list=[1,2,3,45,6,]
print(sum(list))
#sum of given natural numbers
N=5
sum=0
for i in range(1,6):
    sum += i
print(sum)

#product of given numbers
Z = 10
product = 1
for i in range (0,11):
    i += 1
    product = product*i
print(product)

#solid square
for i in range (0,5):
    for j in range (0,5):
        print("* ", end = ' ')
    print()
print("\n")

#solid rectangle
for i in range (0,6):
    for j in range (0,8):
        print("* ",end=' ')
    print()
print("\n")

#daigonal
for i in range(0,4):
    for j in range (0,4):
        if(i==j):
            print("* ",end=' ')
        else:
            print(" ",end=' ')
    print()
print("\n")

#mirrorr traingle
for i in range (n):
    for j in range(n-i+1):
        print(" ",end=' ')
    for j in range (i):
        print("*",end=' ')
    print()
print("\n")

#sequence, immutable and multiple datatypes


