from random import shuffle
# In this version I will be using dictionaries and list to create my sports quiz.
print("Welcome To General Cites Quiz")
import datetime
x=datetime.datetime.now()
print(x)
print("--------------------------------------------------------------")

#Using functions to greet the user.

def greet():
    
    while True:
        name = input("What's your name? : ")
        if name.replace(' ','').isalpha():
            break
        print("Please enter characters A-Z only")
greet()#calling the greet function

