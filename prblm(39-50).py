#39.access the values using ascii values(48-57)
inp=input()
sum=0
for i in inp:
    if(ord(i)>=48 and ord(i)<=57):
        sum+=int(i)
print(sum)

#40.write a code to print all the capital letters in a given string
inp=input()
for i in inp:
    if(ord(i)>=65 and ord(i)<=90):
        print(i)
                      


#41.remove all the brackets from the given algebric expression
inp=input()
for i in inp:
    if(ord(i)==41 or ord(i)==91 or ord(i)==93 or ord(i)==123 or ord(i)==125):
        pass
    else:
        print(i,end=" ")

#50.
#ABC,4
#EFGH
inp=input()
for i in inp:
    if(ord(i)>=65 and ord(i)<=90):
        print(chr(ord(i)+4),end="")

#51.
#input=hello-----wor----ld
#output=--------helloworld
inp=input()
count=0
ans=""
for i in inp:
    if(i=="-"):
        count+=1
    else:
        ans=ans+i
print("-"*count+ans)