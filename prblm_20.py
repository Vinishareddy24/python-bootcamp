#peak element****
my_list=list(map(int,input().split()))
count=0
for i in range(1,len(my_list)-1):
    if my_list[i]>my_list[i-1] and my_list[i]>my_list[i+1]:
        count+=i
        break
print(my_list[count]) 

#important****
my_list=list(map(int,input().split()))
count=0
for i in range(1,len(my_list)-1):
    if my_list[i]>my_list[i-1] and my_list[i]>my_list[i+1]:
        #count=i
        print(my_list[i],end=" ")


#important
my_list=list(map(int,input().split()))
count=0
for i in range(1,len(my_list)-1):
    if my_list[i]>my_list[i-1] and my_list[i]>my_list[i+1]:
        count=i
        #print(my_list[i],end="")
if(my_list[-1]>my_list[-2] and my_list[-1]>count):
    count=len(my_list)-1
print(my_list[count])



