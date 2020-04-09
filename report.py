import webbrowser

def assessment():
    new = 2
    url = "www.google.com"
    webbrowser.open(url,new=new)

def reflection():
    print("Starting this project I was excited as I have an avid interest in programming.")
    print("Hence why I have submitted a python file.")
    print("I have previous experience with other languages but this year was my first time encountering VB.")
    print("It was my first time using a helpful editor, thank god.")
    print("But now I will use my previous experience to give you my experience with the project.")
    strVar5 = input("Do you want to continue? ")
    if (strVar5 == "yes"):
                assessment()
    elif(strVar5 == "no"):
                print("Sure look you have to say yes like")
                assessment()
                return


print("Please answer using yes or no and only lowercase")
strVar1 = input("This is my individual assessment. Continue? ")

if(strVar1 == "yes"):
    strVar3 = input("I'm going to give you my personal reflection on the project, yes/no? ")
    if (strVar3 == "yes"):
        reflection()
    elif (strVar3 == "no"):
        print("ah well you get to read it anyway")
        reflection()
        
elif(strVar1 == "no"):
    strVar4 = input("You're supposed to say yes! Say yes? ")
    if (strVar4 == "yes"):
        print("On to the personal reflection")
        reflection()
    elif (strVar4 == "no"):
        print("You get to read my personal reflection regardless of your answer")
        reflection()
else:
    strVar6 =input("Please answer using yes/no")
    if (strVar6 == "yes"):
        reflection()
    elif (strVar6 == "no"):
        print("Ah well you get to read it anyway")
        reflection()


    
