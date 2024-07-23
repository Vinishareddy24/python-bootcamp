#26.string methods are
#is aplha
#is digit
#is alum(alphanumeric)
#is upper 
#is lower
#convert with lower 
#caseconvert with upper case
#title case 
#swap case


str="Hello world"
print(str.upper())


inp="Hellaalo world"
print(inp.upper())
print(inp.lower())
print(inp.title())
print(inp.swapcase())
print(inp.strip())
print(inp.capitalize())
print(inp.replace('a','z'))
print(inp.split())
print(inp.split('a'))


#27.to check string methods
inp="123 hello world"
print(inp.isalpha()) #used for the spaces
print(inp.isnumeric())
print(inp.issalnum())
print(inp.isascii())
print(inp.islower())
print(inp.isupper())
print(inp.istitle())
print(inp.isnumeric())
print(inp.isdigit())