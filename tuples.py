#write a program to remove duplicate numbers in the list
list_a=[1,2,3,45,4,3,1]
print(set(list_a))

#program to remove a list of numbers if presnt in the set read input as comma separeted


#remove elements otherthen numbers in the list
list_b=[1,2,3,4,"$",8,"*"]
list_c=[]
for i in list_b:
    if i.isdigit()==True:
        list_c.append(i)
        print(list_b)


#program for checking superset,subset,disjoint set

set_a={1,2,34,5,78}
set_b={1,78}
is_subset=set_b.issubset(set_a)
print(is_subset)
is_superset=set_b.issuperset(set_a)
print(is_superset)
is_disjoint=set_b.isdisjoint(set_a)
print(is_disjoint)
