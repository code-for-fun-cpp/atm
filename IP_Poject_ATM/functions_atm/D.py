import os
import pandas as pd
import functions_atm.Data_types as dt

def Del_Acc(index_no):
    os.system('cls')
    rec = pd.read_csv("Main.csv", dtype=dt.datatypes)
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
        return False # Ecits the loop and go to title screen/ logout
    return True #Keeps the Loop Runing