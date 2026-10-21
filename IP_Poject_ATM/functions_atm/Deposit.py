import pandas as pd
import os
import datetime as dt
import functions_atm.Data_types as dtypes

def deposit(index_no):
    os.system('cls')
    rec = pd.read_csv("Main.csv",dtype=dtypes.datatypes)
    ammount = int(input("Enter the Deposited ammount: "))
    pin = input("Enter your pin to conform the transtion: ")
    if(pin != str(rec['Card_Pin'][index_no])):
        print("Invaild Pin. Try again")
        os.system('Pause')
        return
    transction_rec =  str(rec['Account_No'][index_no]) + '.csv'
    tran = pd.read_csv('Transaction/'+transction_rec)
    total = float(ammount) + float(tran['End Balance'][len(tran)-1])
    date_ = dt.date.today()
    date_ = date_.strftime("%d-%m-%Y")
    time_ = dt.datetime.now()
    time_ = time_.strftime("%H:%M:%S")
    tran.loc[len(tran)] = [date_,time_,0,ammount,total]
    tran.to_csv('Transaction/'+transction_rec,index=False)
    rec.loc[index_no, 'Total_Deposit'] = total
    rec.to_csv("Main.csv",index=False)
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