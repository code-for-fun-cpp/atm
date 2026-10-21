import pandas as pd
import os # used to give commands to cmd
import datetime as dt # used to get date and time for record cration
import functions_atm.Data_types as dtypes # to specify the data types of Main.csv

def Withdraw(index_no):
    os.system('cls') #Clears the Treminal 
    rec = pd.read_csv("Main.csv",dtype=dtypes.datatypes) # reades main.csv with proper datatypes 
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