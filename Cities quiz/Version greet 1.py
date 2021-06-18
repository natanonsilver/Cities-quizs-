def greet():
    
    while True:
        name = input("What's your name? : ")
        if name.isalpha():
            break
        print("Please enter characters A-Z only")
greet()#calling the greet function
