import os #used to give commands to cmd 
from functions_atm import Create,login # gets Create and lofin function 


def title(): #Handels the title printing of main Window
    os.system('cls') # clears the terminal
    Width = os.get_terminal_size().columns #gets the width of the terminal
    print("*"*Width)
    print("|","|",sep=' '*(Width-2))
    print("|","Wlecome to AUTOMATED TALLER MACHINE (ATM) ","|",sep=' '*int((Width-44)/2))
    print("|","|",sep=' '*(Width-2))
    print("*"*Width)
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
        Create.create_acc() # Handels the Account Cration
        pass
    elif(inp == '2'):
        login.login() #Handels the login process
        pass
    else:
        print("Please Enter Vaild command. Try again")
        os.system('pause')
        pass
    pass
