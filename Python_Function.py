#1
#***The len() function is used tp determine the length or number of items in a collection such as string,
# tuple, sets, dictionaries or lists. It returns an integer representing the length of the given object***
from tkinter import Variable

l1=list(range(1,7))
print(l1,type(l1),len(l1))

#2
def greet(name):print(f'Hello,{name}!')
name=str(input('Enter the name:'))
greet(name)


#3
def find_maximum(numbers):
    max_value=numbers[0]
    for number in numbers:
        if number>max_value:
            max_value=number
    return max_value
numbers=[4,6,3,11,2]
print(find_maximum(numbers))


#4
#***
# Global Variables:-
# Global Variables are those which are not defined inside any function and have a global scope.
# They are defined outside any function and are accessible throughout the program.
#Local Variable:-
# Local Variables are defined inside a function and their scope is limited inside that function
# alone. They are only accessible inside the function
# ***

x=10 #global Variable
def my_function():
    x=20 #local variable
    print('Local x:', x)
my_function()
print('Global x:', x)

#5
def area_of_rectangle(length, width=5):
    area=length * width
    return(area)
area_with_width=area_of_rectangle(15,3)
print(f'The area of rectangle with length and width is {area_with_width}square units.')

area_with_default_width=area_of_rectangle(15)
print(f'The area of rectangle with length and default width is{area_with_default_width}square units.')







