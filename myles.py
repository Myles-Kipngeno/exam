# 1. a)Define a variable? A variable is one of python's key properties used to asign a value.
#    b)List 4  data types used in python? int,bool,list,dictionary,tuple,set
# 
# 2. Write a python program that adds two numbers provided by the user?
# numbers = eval(input("Enter a nummber: "))
# number = eval(input("Enter a nummber: "))
# sum = numbers + number
# print(sum)

# 3. Write a program that asks a user to give a number and test if that number is an even number?
# number = int(input("Enter a number: "))
# if number % 2 == 0:
#     print("even number")
# else:
#     print("not an even number.")

# 4. a) Write aprogram that asks a user to enter their name and prints the given name in uppercase.
# user_input = input("Enter your name: ").upper()
# print(user_input)
    # B) Print the last 0f the name given by the user.
# name = input("Enter a name: ").title()
# print(name[-1])

# 5. Write a function that finds the sum of any three given numbers.
# num1 = int(input("enter a number: "))
# num2 = int(input("enter a number: "))
# num3 = int(input("enter a number: "))

# def sum ( num1 , num2 , num3):
#     return num1 + num2 + num3
# print(sum(num1, num2, num3))

# 6. Create a list of five integers.
# int = [1, 2, 3, 4, 5]
# int.append(10)
# int.append([11, 12, 13])
# int.pop(0)
# print(int)

# 7. Using a for loop, find and print the sum of the list created in question 6.

# sum =0
# for numbers in range(1,21):
#     sum += numbers
# print(sum)

# 8. Create an empty dictionary called student.
# student={
#     "name" : "Myles",
#     "age" : "40",
#     "marks" : "50",

# }
# print(student.get("name"))
# print(student["age"])

# 9. Create a class called animal with attributes :name,age,habitat.Define a class method called describe_animalthat prints the information about the animal
class Animal:
    def __init__(self, name, age, habitat):
        self.name = name
        self.age = age
        self.habitat = habitat
    def describe_animal(self):
        print(f"{self.name}, {self.age}, {self.habitat}")
    
#  10. Create three instances of the class in question 9 and call on the method describe animal.
dog = Animal("SImba", 34, "Kennel")
print(dog.name, dog.age, dog.habitat)
dog.describe_animal()
elephant = Animal("Elephant", 70, "forest")
elephant.describe_animal()
bird = Animal("parrot", 14, "cage")
bird.describe_animal()


    




