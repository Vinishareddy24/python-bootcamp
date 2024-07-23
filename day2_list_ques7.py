my_list=list(map(int,input().split("@")))
print(*my_list)
#append
my_list=list(map(int,input().split(" ")))
my_list.append(20)
print(*my_list)
#printing list
my_list=[1,2,3,4]
print(*my_list)
#sdfghj
my_list=[1,2,3,4]
print(my_list)
#append to insert
my_list=[1,2,3,4]
my_list.append(9999)
print(*my_list)
#append to insert at particular index
my_list=[1,2,3,4,5,6,7,8,9]
my_list.append(9999)
my_list.insert(8,999)
print(*my_list)
#insert at particular index
my_list=[1,2,3,4]
my_list.append(9999)
my_list.insert(8000,999)
print(len(my_list))
print(*my_list)
#deletion using pop
my_list=[1,2,3,4]
my_list.pop()
#deletion at particular index
my_list=[1,2,3,4]
my_list.pop(2)
#adding to lists
my_list=[1,2,3,4]
my_list_2=[5,6,7,8]
new_list=my_list+my_list_2
print(*new_list)
#add
my_list=[1,2,3,4]
my_list_2=[5,6,7,8]
new_list=my_list.copy()
print(*new_list)
print(*my_list)
#count
cnt=my_list.count(2)
print(cnt)
#sort
my_list=[1,3,-4,77,23]
my_list.sort()
# ascending sort
my_list=[1,3,-4,77,23]
print(my_list.sort())
#dfghjjn
my_list=[1,2,3,4,5]
my_list.pop()
print(my_list)
#fghjk
my_list=[1,2,3,4,5]
my_list.pop(98)
print(my_list)
#list
my_list=list(map(int,input().split("@")))
print(*my_list)
#append
my_list=list(map(int,input().split(" ")))
my_list.append(20)
print(*my_list)
# printing by user choice
my_list=list(map(int,input().split(" ")))
choice=int(input())
print(*my_list)
if(choice==0):
  my_list.append(1)
  print(my_list)
elif(choice==1):
  my_list.pop(2)
  print(my_list)
elif(choice==2):
   my_list.sort(3)
   print(my_list)
elif(choice==3):
   my_list.len(4)
   print(my_list)

#for loop
my_list=list(map(int,input().split("@")))
for i in range(len(my_list)):
    print(my_list[i],end=" ")
    
    print("\n-------------")
for i in my_list:
    print(i,end=" ")

#for loop for strings
s="swec"
for i in range(len(s)):
    print(s[i],end=" ")
    print("\n")
for i in s:
    print(i,end=" ") 

#6.take a space separated input from the user and print alternate elements
my_list=list(map(int,input().split()))
for i in range(0,len(my_list),2):
   print(my_list[i])

#7.given with a comma separatednatural numbers  1 to 10 print only the even numbers
my_list=list(map(int,input().split(",")))
for i in range(1,len(my_list),2):
   print(my_list[i])

#7.2how many even numbers are there in the above question
my_list=list(map(int,input().split()))
count=0
for i in range(1,len(my_list),2):
   count+=1
   print(count)

 #7.3 given with a space separator integer list find the no.of even number and odd number
my_list=list(map(int,input().split()))
even=0
odd=0
for i in range(0,len(my_list)):
   if(n[i]%2==0):
      even+=1
   else:
      odd+=1
print(number)

#8.given with a space separator integer list find the avg of elements present in the even index
my_list=list(map(int,input().split(",")))
count=0
sum=0
n=len(my_list)
for i in range(len(my_list)):
   if(i%2==0):
      sum+=my_list[i]
      count+=1
      print(sum/count)
  












