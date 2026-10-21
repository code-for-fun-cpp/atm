import os

from functions_atm import Create,login


def title():
    os.system('cls')
    height = os.get_terminal_size().columns
    print("*"*height)
    print("|","|",sep=' '*(height-2))
    print("|","Wlecome to AUTOMATED TALLER MACHINE (ATM) ","|",sep=' '*int((height-44)/2))
    print("|","|",sep=' '*(height-2))
    print("*"*height)
    pass



while(True):
    title()
    print(" ")
    print("Enter commad no to execute the commad or type Exit to leave")    
    print("1. Create or Register Account")
    print("2. User login")
    inp = input("Enter your command /> ")
    if(inp.lower() == "exit"):
        print("Thank You for visiting")
        break
    elif(inp == '1'):
        Create.create_acc()
        pass
    elif(inp == '2'):
        login.login()
        pass
    else:
        print("Please Enter Vaild command. Try again")
        os.system('pause')
        pass
    pass
