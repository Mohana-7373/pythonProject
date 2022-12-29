def greetings():
    print("hello")

greetings()



#arguments
def greet(word):
    msg="hello" + word
    print(msg)



#divisible by 7
def divisible(number):
    print(number)
number=21
if (number%7==0):
    print("True")
else:
    print("False")

#marco polo
def three(num):
    if num%3==0 and num%5!=0:
        print("Marco")
    elif num%5==0 and num%3!=0:
        print("Polo")
    elif num%3==0 and num%5==0:
        print("Marco Polo")
    else:
        print("no")
    return num

input = int(input())
three(input)


#discount
def bill_amount(amount):
    print(amount)
amount=560
if amount<500:
    print(amount*0.05)
elif amount>=500 & amount<2500:
    print(amount*0.1)
elif amount>=2500:
    print(amount*0.2)
bill_amount(amount)

#list
def occurence(no):
    list_a=[1,2,3,4,56,4,3,1]
    if i in list_a



