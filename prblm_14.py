#find the missing number in an array
my_list=list(map(int,input().split()))
n=int(input())
t=n*(n+1/2)
miss=0
sum=0
for i in range(len(my_list)):
    sum+=my_list[i]
miss=t-sum
print(miss)

