#leap year
n=int(input())
if(n%4==0 and n%400==0):
    print("leap year")
else:
    print("not a leap year")

#all leap years in a given range
n1=int(input())
n2=int(input())
for i in range(2000,2025):
    if(i%4==0 and i%100!=0):
        print(i)



