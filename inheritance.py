#single
class Animal:
    def Speak():
        return "Animal is speaking"
class Dog(Animal):
    def Bark():
        return "Bow..."
class Puppy(Dog):
    def Talk():
        return "puppy is speaking"
obj1=Animal
obj2=Dog
obj3=Puppy
print(obj2.Speak())
print(obj2.Bark())
print(obj3.Talk())


#multiple 
class Father:
    def father_speak():
        return "father class"
class Mother:
    def mother_speak():
        return "mother class"
class Kid(Mother,Father):
    def kid_speak():
        return "i have both parents"
obj1=Kid
print(obj1.father_speak())
print(obj1.mother_speak())
print(obj1.kid_speak())