#28.ascii values for characters
print(ord("a"))
print(ord('A')+5)
print(ord("}"))
print(chr(60))


#29.check how many vowels are there in a given string
check=['a','e','i','o','u']
count=0
inp="hello world"
for i in inp:
    if(i in check):
        count+=1
print(count)

#30.for lower
check=['a','e','i','o','u']
count=0
i="hello world"
inp=i.lower()
for i in inp:
    if(i in check):
        count+=1
print(count)

#31.write a program to print all the cosonants in a given string
check=['a','e','i','o','u']
count=0
c=0
i="hello wOrld"
inp=i.lower()
for i in inp:
    if(i in check):
        count+=1
for i in inp:
    if(i not in check):
        c+=1
print(count)
print(c)

#32.all the consonants
vowel="aeiou"
consonent="bcdfghjklmnpqrstvwxyz"
count=0
c=0
i="hello wOrld"
inp=i.lower()
for i in inp:
    if(i in inp):
        count+=1
for i in inp:
    if(i not in inp):
        c+=1
print(count)
print(c)


#33.print all the vowels followed by consonents(method 1)
vowels="aeiou"
consonent="bcdfghjklmnpqrstvwxyz"
i="vinsiha"
inp=i.lower()
for i in inp:
    if(i in vowels):  
        print(i,end=" ") 
for i in inp:
    if(i in consonent):
        print(i,end=" ")

#method 2
vowel="aeiou"
consonent="bcdfghjklmnpqrstvwxyz"
ans=""
i="vinsiha"
inp=i.lower()
for i in inp:
    if(i in check):
        ans+=i
        
for i in inp:
    if(i in abc):
        ans+=i
print(ans)


#34.print the non repeating characters in a given string/unique characters in a given string
vowel="aeiou"
consonent="bcdfghjklmnpqrstvwxyz"
ans=""
i="chennugari vinisha"
inp=i.lower()
for i in inp:
    if(i not in ans):
        ans+=i
print(ans)

#35.input="hello 123"
#ouptput="6"
vowel="aeiou"
consonent="bcdfghjklmnpqrstvwxyz"
check="0123456789"
ans=0
i="hello 1234"
inp=i.lower()
for i in inp:
    if(i in check):
        ans+=int(i)
print(ans)

#36.reverse the string(HW)
vowel="aeiou"
consonent="bcdfghjklmnpqrstvwxyz"
str=[]
rev=" "
i="hello 1234world"
inp=i.lower()
for i in inp:
    if(i in str):
      print(rev)

#37.ascii value
print(ord('A'))
for i in range(0,128):
    print(chr(i),end=" ")

#38.special characters
print(ord('A'))
for i in range(32,128):
    print(chr(i),end=" ")

print(ord('A'))
for i in range(99,122):
    print(chr(i),end=" ")