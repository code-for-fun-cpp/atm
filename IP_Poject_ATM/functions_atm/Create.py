import os
import pandas as pd
import datetime as dt
import functions_atm.Data_types as dtypes

def create_rec(Ac_No, deposit):
    record = {
        "Date":[],
        "Time":[],
        "Withdrawl":[],
        "Deposit":[],
        "End Balance":[]
    }
    file_name = str(Ac_No) + ".csv"
    rs = pd.DataFrame(record)
    date_ = dt.date.today()
    date_ = date_.strftime("%d-%m-%Y")
    time_ = dt.datetime.now()
    time_ = time_.strftime("%H:%M:%S")
    rs.loc[len(rs)] = [date_,time_,0,deposit,deposit]
    rs.to_csv("Transaction/"+file_name,index=False)
    pass

def create_acc():
    os.system('cls')
    rec = pd.read_csv("Main.csv",dtype=dtypes.datatypes)
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
    rec = rec.sort_values(by=['Card_No'],ascending=True)
    rec.to_csv("Main.csv",index=False)
    create_rec(Acc_No,depost)
    print("Registration Completed")
    os.system('pause')  
    pass
