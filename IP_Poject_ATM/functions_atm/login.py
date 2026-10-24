import os # used to give commands to Terminal
import pandas as pd
import functions_atm.Deposit as Deposit #Handels the Deposit Process
import functions_atm.Withdraw as Withdraw # Handels the Withdrawl
import functions_atm.change_pin as Pin # Changes the Pin
import functions_atm.History as His # Show the transtion history
import functions_atm.D as D
import functions_atm.Data_types as dtypes # tell pnadas the dtypes of column of Main.csv


def login(): # Hadels login
    os.system('cls') # Clear the Terminal
    acc = str(input("Enter Card No: "))
    pin = str(input("Enter Pin: "))
    rf = pd.read_csv("Main.csv",dtype=dtypes.datatypes) # read main.csv with proprer dtypes
    for i in range(len(rf['Card_No'])):
        if(str(rf['Card_No'][i]) == acc): # check the account
            if(str(rf['Card_Pin'][i] )== pin): # checks the Pin
                print("Login in success Fully")
                os.system('pause') #Paues the Terminal
                login_interface(i) # Takes to Login Interface
                break
            else:
                print("Invalid Pin or Card No. Please try again")
                os.system('pause')
                break
        pass
    pass

def login_interface(index_no):
    while(True):
        rf = pd.read_csv("Main.csv",dtype=dtypes.datatypes) # read main.csv with proprer dtypes
        os.system('cls') 
        print("Welocome",rf['First_Name'][index_no],rf['Last_Name'][index_no],"to the User Interface")
        print("Name :",rf['First_Name'][index_no],rf['Last_Name'][index_no],end=('\t'*4))
        print("Account No:",rf['Account_No'][index_no])
        print("Card No:",rf['Card_No'][index_no],end=('\t'*5))
        print("Card Pin: XXXX")
        print("Bank Name:",rf['Bank_Name'][index_no],end=('\t'*4))
        print("IFSC code:",rf['IFSC_CODE'][index_no])
        print("Total Deposit:",rf['Total_Deposit'][index_no])
        print("Enter commad no to execute the commad or type Logout to leave")
        print("1. Chash Deposit")
        print("2. Chash Withdrawal")
        print("3. PIN Change")
        print("4. Transaction History")
        print("5. Close or Delete Account")
        com = input("Enter your command /> ")
        if(com.lower() == 'logout'): #Handles the Logout
            print("Thank You for Login")
            os.system('pause')
            break
        elif(com == '1'):
            Deposit.deposit(index_no) 
            pass
        elif(com == '2'):
            Withdraw.Withdraw(index_no)
            pass
        elif(com == '3'):
            Pin.Change_Pin(index_no)
            pass
        elif(com == '4'):
            His.view_History(str(rf['Account_No'][index_no]))
            pass
        elif(com == '5'):
            res = D.Del_Acc(index_no)
            if(res == False):
                break
            pass
        else:
            print("Please Enter Vaild command. Try again")
            os.system('pause')
            pass
        pass
    pass