#in this version, it is the assembled 
print("Welcome To General Cities Quiz!")
import datetime
x=datetime.datetime.now()
print(x)
print("=============================================================")
     
#Using functions to greet the user.

def greet():
    
    while True:
        name = input("What's your name? : ")
        if name.isalpha():
            break
        print("Please enter characters A-Z only")
greet()#calling the greet function

def age():
    while True:
        age = input("Please enter your age : ")
        if age.replace(' ','').isnumeric():#using replace to allow spaces after the answer
            if 3< int(age)<100: #allowing age, 3 to 100 only
                break
            else:
                print("=========================================================")
                print('Sorry you have to between 3 and 100 to play this quiz! ')
                print("Thank you come again!")
                print("=========================================================")
                exit()
               
        else:
            print("The data type you have used is invalid data type.\n")
age()
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
ready=input("Are you ready for the quiz?: press y to continue or x to exit:")

if ready=="y" or ready == "yes" :
    print("lets continue")
    print("------------------------------------------------------------")
    print("Please answer the questions with the the alphabets (a,b,c,d)")
    print("------------------------------------------------------------")

#Creating dictionary for question and the right answer

citesquiz={
'1.What is the captial for Nigeria' : 'a',
'2.What is the captial for Spain' :'b',
'3.What is the captial for Canada' :'c',
'4.What is the captial for New Zealand' :'b',
'5.What is the captial for Italy' :'a',
'6.What is the captial for Peru' :'c',
'7.What is the captial for San Marino' :'a',
'8.What is the captial for Mexico' : 'c',
'9.What is the captial for United States Of America' : 'b',
'10.What is the captial for Syria' :'d'


}

#Creating list of answer options
optlist=[
'a)Abuja:b)Miami:c)Belmopan:d)Jerusalem',
'a)Astana:b)Madrid:c)Kingston:d)Bujumbura',
'a)Philipsburg:b)Lusaka:c)Ottawa:d)Lima',
'a)Monrovia:b)Wellington:c)Ottawa:d)Suva',
'a)Rome:Palikir:b)Algiers:c)Seoul',
'a)Copenhagen:b)Kuwait City:c)Lima',
'a)San Marino:b)Pyongyang:c)Marigot:d)Canberra',
'a)West Island:b)Bissau:c)Mexico City:d)Nouakchott',
'a)Nairobi:b)Washington DC:c)Stanley:d)Phnom Penh',
'a)Yaren:b)Harare:c)Palikir:d)Damascus',
]
index=0
score=0
optnum=0
    
        #Questions for Cites Quiz.
for q in citesquiz.keys():
        print(q) #Printing one question at a time in order.
        print(optlist[index]) #Print first option.
        index=index+1
        print("            ")
        
        user_ans=input("Enter your answer:")
        answer = citesquiz[q] # Finding answer to the question in the dictionary.

        if user_ans==answer:
            print("That is correct, Keep up the good work")
            print("---------------------")
            score=score+1
            print("Score",score+0)
        else:
            print("That is not correct. The answer is", answer)


             

            print("---------------------")
               
            print("Your score is",score,"out of 10 points")  #Presenting the scores to the users.
            print("Quiz Complete, WELL DONE :)")

            

    
if ready== "x" :  #If the user inputs x or no, when they are asked if they want to contiue the quiz or not.
    print("Consider playing later")
elif ready== "no":
    print ("Consider playing later ")
exit()
