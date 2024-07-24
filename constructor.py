##
class Myclass:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(a,b):
        return a+b
    def sub(a,b):
        return a-b
    def mul(a,b):
        return a*b
    def mod(a,b):
        return a%b
    def div(a,b):
        return a/b
obj1=Myclass
obj2=Myclass
print(obj1.add(2,5))#methods
print(obj2.sub(12,5))

##
class Myclass:
    cls_var="im class variable"
    def add(a,b):
        ins_var_add="im instance var"
        print(ins_var_add)
        return a+b
    def sub(a,b):
        return a-b
    def mul(a,b):
        return a*b
    def mod(a,b):
        return a%b
    def div(a,b):
        return a/b
obj1=Myclass
obj2=Myclass
print(obj1.add(2,5))
print(obj2.sub(12,5)) 