import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

def graph_(file, L_enters):
    plot_file = pd.read_csv(file)
    Date = plot_file['Date'].tail(L_enters)
    Withdraw = plot_file['Withdrawl'].tail(L_enters)
    Deposit = plot_file['Deposit'].tail(L_enters)

    Date_d = [0]
    Withdraw_d = []
    Deposit_d = []

    for i in range(len(Date)):
        if(Date_d[-1] != Date.iloc[i]):

            Date_d.append(Date.iloc[i])
            Withdraw_d.append(float(Withdraw.iloc[i])) 
            Deposit_d.append(float(Deposit.iloc[i]))
            pass
        else:
            Withdraw_d[-1] = Withdraw_d[-1] + float(Withdraw.iloc[i])
            Deposit_d [-1] = Deposit_d[-1] + float(Deposit.iloc[i])
            pass
        pass

    Date_d.pop(0) 
    x = np.arange(len(Date_d))
    plt.bar(x-0.2,Withdraw_d,color = 'Red',width=0.4,label = 'Withdraw')
    plt.bar(x+0.2,Deposit_d,color = 'Green',width=0.4,label = 'Deposit')
    plt.title("LAST TRANSTION",color = 'Black')
    plt.xlabel("Transtion Date", color = 'Orange')
    plt.ylabel("Amount", color = 'Blue')
    plt.xticks(x,Date_d)
    plt.legend()
    plt.show()
    pass


def view_History(account):
    os.system('cls')
    tran_file  = 'Transaction/'+ str(account) + ".csv"
    tran_rec = pd.read_csv(tran_file)
    print("Account No:",account)
    print("Total Transtions:", len(tran_rec))
    trna_no = int(input("Enter the No of Trnastion you wnat to dispaly: "))
    if(trna_no > len(tran_rec)):
        print("Please Enter Vaild Range")
        os.system('Pause')
        return
    print("The Last", trna_no, "for the account: ")
    print(tran_rec.tail(trna_no))
    graph = input("Do you want to see the graph of transtion History(Y/N): ")
    if(graph.upper() == 'Y'):
        graph_(tran_file,trna_no)
        pass
    pass
