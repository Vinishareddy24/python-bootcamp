#10 print the element at a particular index and do cyclic manner
#k=8
#80 70 54 36 72
#op:36          #use mod%
my_list=list(map(int,input().split()))
k=int(input())
len=len(my_list)
a=k%len
print(my_list[a]) 