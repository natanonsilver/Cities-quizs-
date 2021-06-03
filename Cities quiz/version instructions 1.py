#Asking the user to enter their age by using try and except.

def instructions():
    inst=input("Do you need instructions to play? : answer 'y' for Yes and 'n' for No")
    if inst=="y":
        print("=======================================================================================")
        print("You will be given a set of four or three answers and you must choose which one is right")
        print("=======================================================================================")
    else:
        print("Welcome to the quiz")

instructions()#calling instructions function


#Asking the user if they are ready for the quiz


#Asking the user for their status

ready=input("Are you ready for the quiz?:")

if ready=="y" or ready == "yes" :
    print("lets continue")
    print("------------------------------------------------------------")
    print("Please answer the questions with the the alphabets (a,b,c,d)")
    print("------------------------------------------------------------")
elif ready=="n" or ready == "No":
    print("Come back and play agin")
    exit()
