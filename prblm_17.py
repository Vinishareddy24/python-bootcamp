#find the sum of square of a digit in a given number
n=int(input())
sum=0
while n>0:
    r=n%10
    sum=sum+r**2
    n=n//10
print(sum)


#find the sum of square of even digit in a given number
n=1234
sum=0
while n>0:
    r=n%10
    if(r%2==0):
        sum=sum+r
    n=n//10
print(sum)


#reverse a number
n=1234
rev=""
while n>0:
    r=n%10
    rev=rev+str(r)
    n=n//10
print(int(rev))

#important 
n=1234
rev=""
while n>0:
    r=n%10
    rev=rev+str(r)
    n=n//10
ans=int(rev)
print(ans)
print(type(ans))