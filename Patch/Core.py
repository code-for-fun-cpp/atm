import os # used to give commands to Terminal
import pandas as pd
import datetime as dt
from Data_types import *
import History as His

def create_rec(Ac_No, deposit): #Creates a New record file for new user
    record = {
        "Date":[],
        "Time":[],
        "Withdrawl":[],
        "Deposit":[],
        "End Balance":[]
    }
    file_name = str(Ac_No) + ".csv"
    rs = pd.DataFrame(record)
    date_ = dt.date.today() # Gets the Current date
    date_ = date_.strftime("%d-%m-%Y") # change the format of the date
    time_ = dt.datetime.now() # Gets the Current time
    time_ = time_.strftime("%H:%M:%S") # change the format of the date
    rs.loc[len(rs)] = [date_,time_,0,deposit,deposit]
    rs.to_csv("Transaction/"+file_name,index=False)
    pass

def create_acc(): #Add a new user in Main.csv
    os.system('cls')
    rec = pd.read_csv("Main.csv",dtype=datatypes) #tells pandas the dtypes of Coloums
    print("Welocome to Registration Interface. Please Enter all of your Details carefull")
    F_Name = input("First Name: ")
    L_Name = input("Last Name: ")
    Card_No = input("Card No (5-digit): ")
    Acc_No = input("Account No (6-digit): ")
    Card_Pin = input("Card Pin (4-digit): ")
    print("Please Select Bank Name from below list")
    print("1. State Bank of India (SBI)")
    print("2. HDFC Bank")
    print("3. ICICI Bank")
    print("4. Bank of Baroda (BoB)")
    print("5. Punjab National Bank (PNB)")
    B_inp = input("Enter Your Bank No: ")
    if(B_inp == '1'): Bank_Name = "State Bank of India (SBI)"
    elif(B_inp == '2'): Bank_Name = "HDFC Bank"
    elif(B_inp == '3'): Bank_Name = "ICICI Bank"
    elif(B_inp == '4'): Bank_Name = "Bank of Baroda (BoB)"
    elif(B_inp == '5'): Bank_Name = "Punjab National Bank (PNB)"
    ifsc_code = input("IFSC Code: ")
    depost = float(input("Intial Depost(in Rs): "))
    rec.loc[len(rec)] = [Acc_No,Card_No,F_Name.capitalize(),L_Name.capitalize(),Card_Pin,Bank_Name,
                         ifsc_code,depost]
    rec = rec.sort_values(by=['Card_No'],ascending=True) # Sotre the values in sorted order
    rec.to_csv("Main.csv",index=False)
    create_rec(Acc_No,depost) # creating record for new user
    print("Registration Completed")
    os.system('pause')  # Pauses the Cmd/terminal windows
    pass


def Withdraw(index_no):
    os.system('cls') #Clears the Treminal 
    rec = pd.read_csv("Main.csv",dtype=datatypes) # reades main.csv with proper datatypes 
    ammount = int(input("Enter the Withdrawl ammount: "))
    transction_rec =  str(rec['Account_No'][index_no]) + '.csv'
    tran = pd.read_csv('Transaction/'+transction_rec) # Readsthe transtion record
    pin = input("Enter your pin to conform the transtion: ")
    if(pin != str(rec['Card_Pin'][index_no])): # check the Pin
        print("Invaild Pin. Try again")
        os.system('Pause') # Pause the Terminal
        return
    elif(float(ammount) > float(tran['End Balance'].iloc[-1])): # Checkes the Blance for Transtion
        print("Insufficient Funds for transaction")
        os.system('Pause')
        return
    total = float(tran['End Balance'].iloc[-1]) - float(ammount) # upadates the blaance
    date_ = dt.date.today() #Gets date
    date_ = date_.strftime("%d-%m-%Y") #Formates the Time
    time_ = dt.datetime.now() # Gets the Time
    time_ = time_.strftime("%H:%M:%S") # Formates the Time
    tran.loc[len(tran)] = [date_,time_,ammount,0,total] # date time withdarw deposit total
    tran.to_csv('Transaction/'+transction_rec,index=False) #updates the Trastion record file
    rec.loc[index_no, 'Total_Deposit'] = total # updates the total Depost
    rec.to_csv("Main.csv",index=False) # updates the Main.csv
    print("Transaction completed")
    res = input("Do you want to print receipt(Y/N): ")
    if(res.upper() == 'Y'):
            print("\t\t RECIPITE \t\t")
            print("_"*42)
            print("Card:",rec['Card_No'][index_no])
            print("Account:",rec["Account_No"][index_no])
            print("_"*42)
            print("Date:",date_)
            print("Time:",time_)
            print("_"*42)
            print("Ammount Withdraw:",ammount)
            print("_"*42)
            print("End Balance:",total)
            os.system("pause")
            pass
    pass

def deposit(index_no):
    os.system('cls') # clears the Terminal
    rec = pd.read_csv("Main.csv",dtype=datatypes) # reads the Main.csv with specified dtypes 
    ammount = int(input("Enter the Deposited ammount: "))
    pin = input("Enter your pin to conform the transtion: ")
    if(pin != str(rec['Card_Pin'][index_no])): # checks the pin
        print("Invaild Pin. Try again")
        os.system('Pause')
        return
    transction_rec =  str(rec['Account_No'][index_no]) + '.csv' #Transtion record file name
    tran = pd.read_csv('Transaction/'+transction_rec) # Reads the Trnstion file
    total = float(ammount) + float(tran['End Balance'].iloc[-1]) # Updates the blance
    date_ = dt.date.today() #gets the date
    date_ = date_.strftime("%d-%m-%Y") # formates the date
    time_ = dt.datetime.now() # gets the time
    time_ = time_.strftime("%H:%M:%S") # formates the time
    tran.loc[len(tran)] = [date_,time_,0,ammount,total] 
    tran.to_csv('Transaction/'+transction_rec,index=False) #Updates the transtion record
    rec.loc[index_no, 'Total_Deposit'] = total # Update the Total Deposit
    rec.to_csv("Main.csv",index=False) # Update the Main.csv
    print("Transaction completed")
    res = input("Do you want to print receipt(Y/N): ")
    if(res.upper() == 'Y'):
        print("\t\t RECIPITE \t\t")
        print("_"*42)
        print("Card:",rec['Card_No'][index_no])
        print("Account:",rec["Account_No"][index_no])
        print("_"*42)
        print("Date:",date_)
        print("Time:",time_)
        print("_"*42)
        print("Ammount Deposited:",ammount)
        print("_"*42)
        print("End Balance:",total)
        os.system("pause")
        pass
    pass

def Change_Pin(index_no):
    os.system("cls") # Clear the terminal
    rec  = pd.read_csv("Main.csv",dtype=datatypes)
    old_pin = input("Current Pin: ")
    new_pin = input("New Pin: ")
    conf_pin = input("Confirm the Pin: ")
    if(old_pin != str(rec['Card_Pin'][index_no])): #verifyes the Pin 
        print("Please Enter Correct Current Pin")
        os.system("pause") # To pause the terminal
        return
    elif(len(new_pin) != 4 and new_pin.isdigit()): # Check the len of the new pin
        print("Pin lenght should be 4 digits")
        os.system("pause")
        return
    elif(new_pin != conf_pin): # confirmes the New Pin
        print("New Pin does no match the confirmed Pin ")
        os.system("pause")
        return
    else:
        rec.loc[index_no, 'Card_Pin'] = new_pin # set the new pin
        print("PIN Change Sucressfully")
        rec.to_csv('Main.csv' ,index= False)
        os.system("pause") 
        pass
    pass

def Del_Acc(index_no):
    os.system('cls')
    rec = pd.read_csv("Main.csv", dtype=datatypes)
    acc = rec['Account_No'][index_no]
    u_pin = rec['Card_Pin'][index_no]
    pin  = input("Enter Your Pin to Delete Your account: ")
    if(pin != u_pin):
        print("Invailed Pin, Account Deleation Aborted")
        os.system("pause")
        return
    conf = input("DO YOU REALLY WANT TO DELECTER YOUR ACCOUNT!! (Y/N): ")
    if(conf.upper() == 'Y'):
        trns_file = "Transaction/"+ acc + ".csv"
        os.remove(trns_file)
        rec = rec.drop(index_no)
        rec.to_csv('Main.csv', index=False)
        print("Account Deleted Sussfully")
        os.system('pause')
        return False # Exits the loop and go to title screen/ logout
    return True #Keeps the Loop Runing

def login(): # Hadels login
    os.system('cls') # Clear the Terminal
    acc = str(input("Enter Card No: "))
    pin = str(input("Enter Pin: "))
    rec = pd.read_csv("Main.csv",dtype=datatypes) # read main.csv with proprer dtypes
    for i in range(len(rec['Card_No'])):
        if(str(rec['Card_No'][i]) == acc): # check the account
            if(str(rec['Card_Pin'][i] )== pin): # checks the Pin
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
        rec = pd.read_csv("Main.csv",dtype=datatypes) # read main.csv with proprer dtypes
        os.system('cls') 
        print("Welocome",rec['First_Name'][index_no],rec['Last_Name'][index_no],"to the User Interface")
        print("Name :",rec['First_Name'][index_no],rec['Last_Name'][index_no],end=('\t'*4))
        print("Account No:",rec['Account_No'][index_no])
        print("Card No:",rec['Card_No'][index_no],end=('\t'*5))
        print("Card Pin: XXXX")
        print("Bank Name:",rec['Bank_Name'][index_no],end=('\t'*4))
        print("IFSC code:",rec['IFSC_CODE'][index_no])
        print("Total Deposit:",rec['Total_Deposit'][index_no])
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
            deposit(index_no) 
            pass
        elif(com == '2'):
            Withdraw(index_no)
            pass
        elif(com == '3'):
            Change_Pin(index_no)
            pass
        elif(com == '4'):
            His.view_History(str(rec['Account_No'][index_no]))
            pass
        elif(com == '5'):
            res = Del_Acc(index_no) # Gets True or False value from Del_Acc
            if(res == False):
                break
            pass
        else:
            print("Please Enter Vaild command. Try again")
            os.system('pause')
            pass
        pass
    pass