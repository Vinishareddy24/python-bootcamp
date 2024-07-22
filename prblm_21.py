 #GCD of 2 numbers
#euclidean division lemma #a=21,b=14
a=int(input("enter a number: "))
b=int(input("enter a number: "))
while b!=0:
    a,b=b,a%b
print("GCD of 2 number is: ",a)

