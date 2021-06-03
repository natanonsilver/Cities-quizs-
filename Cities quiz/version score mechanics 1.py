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
      
