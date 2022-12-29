set_a={1,2,34,5,78}
set_b={1,78}
is_subset=set_b.issubset(set_a)
print(is_subset)
is_superset=set_b.issuperset(set_a)
print(is_superset)
is_disjoint=set_b.isdisjoint(set_a)
print(is_disjoint)


set_d={36,68,90,56,70}
set_e={45,80,89,70,36}
set_f={56,80,36,70,90}
intersection = set_d & set_e & set_f
ic = set_d.intersection(set_e, set_f)
print(ic)
print(intersection)

set_x={23,45,67,89,90,10,"x","t"}
set_y={45,30,90,50,60,"t","z"}
diff=set_x-set_y
print(diff)
sym_difference=set_x^set_y
print(sym_difference)

#update,delet of value
dict_a={"name":"yamani","age":22}
dict_a["age"]=20
print(dict_a)
del dict_a["name"]
print(dict_a)

#squares of key
my_name=dict()
for i in range(1,10):
    my_name[i]=i**2
print(my_name)

#rotations
A="python"
L=len(A)
P=list(A)
Q=A[0:4]
U=''
print(P)
for i in range(4,L):
    print(P[i],end="")
S=U+Q
print(S)



#perfect squares b/w m & n
list=[]
for i in range(1,10):
    for j in range(1,10):
        if j*j==i:
            list.append(i)
print(list)

#matrix
x=int(input())
y=int(input())
mat=[]
for i in range(x):
    
