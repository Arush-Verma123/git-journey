while(True):
    c=int(input('''Enter 1: To add
    Enter 2: To subtract
    Enter 3: To multiply
    Enter 4: To divide
    Enter 5: To exit the calculator.
    '''))
    a=int(input("Enter the first number:"))
    b=int(input("Enter the second number:"))
    if(c==5):
        break
    elif(c==1):
        print(f"{a}+{b}=",a+b)
    elif(c==2):
        print(f"{a}-{b}=",a-b)
    elif(c==3):
        print(f"{a}*{b}=",a*b)
    elif(c==4):
        print(f"{a}/{b}=",a/b)
    else:
        print("Wrong input!")
print("Successfully exited the caluclator. :)")