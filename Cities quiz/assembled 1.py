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




#Creating dictionary for question and the right answer

print("                                                    ")
#set of questions that are asked
#question 1
## questions and right answers

def rounds():
    global r
    while True:
        try:
            r = int(input("\nPlease enter how many rounds you want to play : "))##asking the user how many rounds they want to play
            if 0<r<=10:
                break
            else:
                print("please enter the rounds in 1 to 10 only")
        except:
            print('please enter rounds in numbers only (The max is 10)')



rounds()


score = 0
questions=[

[
    "What is the capital of Nigeria?",
    {'answer':'a','option':'\na.Abuja \nb.Miami \nc.Belmopan \nd.Jerusalem '}
    ],

[
    "What is the captial for Spain?",
    {'answer':'b','option':'\na.Astana \nb.Madrid \nc.Kingston \nd.Bujumbura '}
    ],


[
    "What is the captial for Canada?",
    {'answer':'c','option':'\na.Philipsburg \nb.Lusaka \nc.Ottawa \nd.Lima '}
    ],    
   
[
    "What is the captial for New Zealand?",
    {'answer':'b','option':'\na.Monrovia\nb.Wellington \nc.Ottawa \nd.Suva '}
    ],    
   

[
    "What is the captial for Italy",
    {'answer':'a','option':'\na.Rome \nb.Palikir\nc.Algiers \nd.Seoul'}
    ],    
     


[
    "What is the captial for Peru?",
    {'answer':'c','option':'\na.Copenhagen \nb.Kuwait City\nc.Lima'}
    ],    
     
[
    "What is the captial for San Marino?",
    {'answer':'c','option':'\na.San Marino \nb.Pyongyang \nc.Marigot \nd.Canberra'}
    ],    

[
    "What is the captial for Mexico?",
    {'answer':'c','option':'\na.West Island \nb.Bissau \nc.Mexico City \nd.Nouakchott '}
    ],    
[
    "What is the captial for United States Of America?",
    {'answer':'b','option':'\na.Nairobi \nb.Washington DC \nc.Stanley'}
    ],    

[
    "What is the captial for Syria?",
    {'answer':'c','option':'\na.Yaren \nb.Harare \nc.Palikir \nd.Damascus'}
    ],


        ]
shuffle(questions)
## score mechanics
print("Main Routine")
while r>0:
    data = questions[0]
    q = data[0]
    data =data[1]
    answer = data['answer']
    option = data['option']

    print(q)
    print(option)
    while True:
        user_answers = input("Please enter your answer here : ").lower().replace(' ','')
        if user_answers =='a' or user_answers == 'b' or user_answers == 'c' or user_answers == 'd':
            if user_answers == answer:
                print("---------------------------")
                print("Great job, its right! ")
                print("---------------------------")
                score +=1
                print("=======")
                print("your score is",score)
                print("=======")
            else:
                print("-----------------------------------------------------------------------------")
                print("oh no sorry your answer is not correct. This is the correct answer is ",answer)    
                print("-----------------------------------------------------------------------------")
                print("your score is",score)
                print("=======")

                
                print("---------------------")
               
            


            del questions[0]
            r-=1
            break
        else:
            print("please enter the alphabet for the chosen option")
                   
#Presenting the scores to the users.
print("Your score is",score) 
print("Quiz Complete, WELL DONE :)")
exit()
      
             

    



