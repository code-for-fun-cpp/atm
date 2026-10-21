import pandas as pd 
import os # used to give commands to cmd
import datetime as dt # used to get date and time for record cration
import functions_atm.Data_types as dtypes # to specify the data types of Main.csv

def deposit(index_no):
    os.system('cls') # clears the Terminal
    rec = pd.read_csv("Main.csv",dtype=dtypes.datatypes) # reads the Main.csv with specified dtypes 
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