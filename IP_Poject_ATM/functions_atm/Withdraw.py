import pandas as pd
import os
import datetime as dt


def Withdraw(index_no):
    os.system('cls')
    rec = pd.read_csv("Main.csv")
    ammount = int(input("Enter the Withdrawl ammount: "))
    transction_rec =  str(rec['Account_No'][index_no]) + '.csv'
    tran = pd.read_csv('Transaction/'+transction_rec)
    pin = input("Enter your pin to conform the transtion: ")
    if(pin != str(rec['Card_Pin'][index_no])):
        print("Invaild Pin. Try again")
        os.system('Pause')
        return
    elif(float(ammount) > float(tran['End Balance'][len(tran)-1])):
        print("Insufficient Funds for transaction")
        os.system('Pause')
        return
    total = float(tran['End Balance'][len(tran)-1]) - float(ammount)
    date_ = dt.date.today()
    date_ = date_.strftime("%d-%m-%Y")
    time_ = dt.datetime.now()
    time_ = time_.strftime("%H:%M:%S")
    tran.loc[len(tran)] = [date_,time_,ammount,0,total] # date time withdarw deposit total
    tran.to_csv('Transaction/'+transction_rec,index=False)
    rec.loc[index_no, 'Total_Deposit'] = total
    rec.to_csv("Main.csv",index=False)
    print("Transions completed")
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