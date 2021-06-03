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
