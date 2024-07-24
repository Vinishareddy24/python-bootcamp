#method over riding(run time)
class Animal:
    def Speak():
        return "Speaking..."
class Dog(Animal):
    def Speak():
        return "Dog is Speaking...."
class Puppy(Dog):
    def Speak():
        return "Puppy is Speaking...."
obj3=Dog
print(obj3.Speak())

#method over_loading(increasing the capacity&complie time)
class cal:
    def add(self,*args):
        return sum(args)
obj1=cal() #taking inputs
print(obj1.add(1,2))
print(obj1.add(1,2,3))
print(obj1.add(1,2,3,4))#when it is dynamic we need to keep paranthesis if static no need of paranthesis(obj1=cal()) 