import os
import pandas as pd
import functions_atm.Deposit as Deposit
import functions_atm.Withdraw as Withdraw
import functions_atm.change_pin as Pin
import functions_atm.History as His
import functions_atm.Data_types as dtypes


def login():
    os.system('cls')
    acc = str(input("Enter Card No: "))
    pin = str(input("Enter Pin: "))
    rf = pd.read_csv("Main.csv",dtype=dtypes.datatypes)
    for i in range(len(rf['Card_No'])):
        if(str(rf['Card_No'][i]) == acc):
            if(str(rf['Card_Pin'][i] )== pin):
                print("Login in success Fully")
                os.system('pause')
                login_interface(i)
                break
            else:
                print("Invalid Pin or Card No. Please try again")
                os.system('pause')
                break
        pass
    pass

def login_interface(index_no):
    while(True):
        rf = pd.read_csv("Main.csv",dtype=dtypes.datatypes)
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
        com = input("Enter your command /> ")
        if(com.lower() == 'logout'):
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
        else:
            print("Please Enter Vaild command. Try again")
            os.system('pause')
            pass
        pass
    pass