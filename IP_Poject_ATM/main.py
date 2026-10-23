import os #used to give commands to cmd 
from functions_atm import Create,login # gets Create and lofin function 


def title(): #Handels the title printing of main Window
    os.system('cls') # clears the terminal
    Width = os.get_terminal_size().columns #gets the width of the terminal
    print("*"*Width)
    print("|","|",sep=' '*(Width-2))
    print("|","CBSE IP Project 2026-27 on Topic ATM","|",sep=' '*int((Width-38)/2))
    print("|","Wlecome to AUTOMATED TELLER MACHINE (ATM) ","|",sep=' '*int((Width-44)/2))
    print("|","|",sep=' '*(Width-2))
    print("*"*Width)
    pass


def about():
    os.system('cls')
    Width = os.get_terminal_size().columns #gets the width of the terminal
    print("*"*Width)
    print("|","|",sep=' '*(Width-2))
    print("|","CBSE IP Project 2026-27 ","|",sep=' '*int((Width-25)/2))
    print("|","|",sep=' '*(Width-2))
    print("*"*Width)
    print('\n')
    print('\t project name \t\t\t\t : \t\t\t\t  AUTOMATED TELLER MACHINE (ATM)')
    print('\n')
    print('\t School \t\t\t\t : \t\t\t\t  St Francis Sr. Sec. School')
    print('\t Address \t\t\t\t : \t\t\t\t  Alwar Gate, Ajmer')
    print('\t Guided by \t\t\t\t : \t\t\t\t  Mr . Vijendar')
    print('\n')
    print('\t Submitted by  \t\t\t\t : \t\t\t\t  Harshit,Raghvendar,Yash')
    print('\t Class : XII')
    os.system('pause')

while(True):
    title()
    print(" ")
    print("Enter commad no to execute the commad or type Exit to leave")    
    print("1. Create or Register Account")
    print("2. User login")
    print("3. About project")
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
    elif(inp == '3'):
        about()
        pass
    else:
        print("Please Enter Vaild command. Try again")
        os.system('pause')
        pass
    pass
