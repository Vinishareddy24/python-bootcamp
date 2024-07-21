#9.find the element that is  present in (k+n) index 
#k is given by user k=3,n=2
#3 6 8 4 6 2
#op:2
#-------------
#k=3
#n=4
#80 70 54 36 52
my_list=list(map(int,input().split()))
n=int(input())
k=int(input())
len=len(my_list)
if(len<k+n):
    print("error")
else:
    for i in range(0,len(my_list)):
            print(my_list[k+n],end=" ")
            break

