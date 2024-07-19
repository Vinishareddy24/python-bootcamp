name=input("enter your name")
var1="python"
print("good morning",var1)
print("hello",name)
print("HELLO SWEC")


#output formats
name=input("enter your name")
age=int(input())
print(f"Hello{name}your {age} years old")

#1to print avg marks
name=input("enter your name")
s1=int(input())
s2=int(input())
s3=int(input())
s4=int(input())
avg=0
print("avg marks")
print(f"hi {name} the avg marks are {(s1+s2+s3+s4)/6}")


#2to print insame line
name=input()
print(name,end="")
print(name)

#four and two wheeler
age=25
if(age>=18 and age<24):
    print("only two wheeler")
elif(age>=24 and age<45):
    print("two and four wheeler")
else:
    print("all")

#3write a program for voting eligibility criteria
name=input("enter your name")
age=int(input())
if(age>=18):
    print(f"hey,{name} above 18 eligible for voting")
else:
    print(f"hey,{name} below 18 eligible for voting")

#4arthemetic operator
n1=int(input())
n2=int(input())
print("n1+n2 is",n1+n2)
print("n1-n2 is",n1-n2)
print("n1*n2 is",n1*n2)
print("n1/n2 is",n1/n2)
print("n1%n2 is",n1%n2)
print("n1*n2 is",n1*n2)
print("n1//n2 is",n1//n2)

#x goes to market buy 10 apples,2 dozen bananas,8 oranges the cost of 1 apple is 15rup,1 banana 4,1 orange 5
#y gave money to x-700
a=int(input())
b=int(input())
c=int(input())
amount=a*15+b*4+c*5
if(amount<=700):
    print("amount is left over")
else:
    print("amount will not left")


#6positive,negative ,even,odd
n=int(input())
if(n>0 and n%2==0):
    print("positive and even")
elif(n<0 and n%2==0):
    print("negative and even")
elif(n>0 and n%2!=0):
    print("possitive and odd")
elif(n<0 and n%2!=0):
    print("negative and odd")
else:
    print("number is zero")

##7mr "z" is selected for Olympics is participating in swimming competition   only one winner is selected among them and he got selected x and y are frnds of z ,x is participated in badminton and y is participated in table tennis. according to the selection committee the req of badminton players are 140cm height, weight factors of 2 ,body fat is less than 12%.according to selection committee req for table tennis are height min 118cm to 148cm,weight is the factors of no.of medals won by z, body fat=14%.according to the previous history z participated in 14 games out of its he is having success rate of 65%.write a program to check whether x,y and z from india travel in a same plane or not .**

n=int(input())
x="swimming"
y="badminton"
z="table tennis"
height=int(input())
weight=int(input())
body_fat=int(input())
x_medals=int(input())
if(height>=140 and weight>=n%2 and body_fat<12):
    print("y will travel")
    if(height>=118 and height<=140 and weight==x_medals and body_fat<12):
        print("z will travel")
        print("xyz will travel")
else:
    print("not travel")