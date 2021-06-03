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
