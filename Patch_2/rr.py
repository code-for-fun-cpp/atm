import os, pandas as pd, numpy as np, datetime as dt, matplotlib.pyplot as plt

datatypes = {
    'Acc_No': str,
    'Card_No': str, 'Card_Pin': str,}

def title():
    os.system('cls'); Width = os.get_terminal_size().columns
    print("*"*Width); print("|","|",sep=' '*(Width-2)); print("|","CBSE IP Project 2026-27 on Topic ATM","|",sep=' '*int((Width-38)/2)); print("|","Wlecome to AUTOMATED TELLER MACHINE (ATM) ","|",sep=' '*int((Width-44)/2)); print("|","|",sep=' '*(Width-2)); print("*"*Width); pass

def about():
    os.system('cls'); Width = os.get_terminal_size().columns
    print("*"*Width); print("|","|",sep=' '*(Width-2)); print("|","CBSE IP Project 2026-27 ","|",sep=' '*int((Width-25)/2)); print("|","|",sep=' '*(Width-2)); print("*"*Width); print('\n'); print('\t project name \t\t\t\t : \t\t\t\t  AUTOMATED TELLER MACHINE (ATM)'); print('\n'); print('\t School \t\t\t\t : \t\t\t\t  St Francis Sr. Sec. School'); print('\t Address \t\t\t\t : \t\t\t\t  Alwar Gate, Ajmer'); print('\t Guided by \t\t\t\t : \t\t\t\t  Mr . Vijendar'); print('\n'); print('\t Submitted by  \t\t\t\t : \t\t\t\t  Harshit,Raghvendar,Yash'); print('\t Class : XII'); os.system('pause')

def create_rec(Ac_No, deposit):
    record = {"Date":[], "Time":[], "Withdrawl":[], "Deposit":[], "End Balance":[]}
    file_name = str(Ac_No) + ".csv"; rs = pd.DataFrame(record); date_ = dt.date.today(); date_ = date_.strftime("%d-%m-%Y")
    time_ = dt.datetime.now(); time_ = time_.strftime("%H:%M:%S")
    rs.loc[len(rs)] = [date_,time_,0,deposit,deposit]; rs.to_csv("Transaction/"+file_name,index=False); pass

def create_acc():
    os.system('cls'); rec = pd.read_csv("Main.csv",dtype=datatypes)
    print("Welocome to Registration Interface. Please Enter all of your Details carefull")
    F_Name = input("First Name: "); L_Name = input("Last Name: "); Card_No = input("Card No (5-digit): "); Acc_No = input("Account No (6-digit): "); Card_Pin = input("Card Pin (4-digit): ")
    print("Please Select Bank Name from below list\n1. State Bank of India (SBI)\n2. HDFC Bank\n3. ICICI Bank\n4. Bank of Baroda (BoB)\n5. Punjab National Bank (PNB)")
    B_inp = input("Enter Your Bank No: ")
    if(B_inp == '1'): Bank_Name = "State Bank of India (SBI)"
    elif(B_inp == '2'): Bank_Name = "HDFC Bank"
    elif(B_inp == '3'): Bank_Name = "ICICI Bank"
    elif(B_inp == '4'): Bank_Name = "Bank of Baroda (BoB)"
    elif(B_inp == '5'): Bank_Name = "Punjab National Bank (PNB)"
    ifsc_code = input("IFSC Code: "); depost = float(input("Intial Depost(in Rs): "))
    rec.loc[len(rec)] = [Acc_No,Card_No,F_Name.capitalize(),L_Name.capitalize(),Card_Pin,Bank_Name,ifsc_code,depost]
    rec = rec.sort_values(by=['Card_No'],ascending=True)
    rec.to_csv("Main.csv",index=False); create_rec(Acc_No,depost)
    print("Registration Completed"); os.system('pause'); pass

def Change_Pin(index_no):
    os.system("cls"); rec = pd.read_csv("Main.csv",dtype=datatypes); old_pin = input("Current Pin: "); new_pin = input("New Pin: "); conf_pin = input("Confirm the Pin: ")
    if(old_pin != str(rec['Card_Pin'][index_no])): print("Please Enter Correct Current Pin"); os.system("pause"); return
    elif(len(new_pin) != 4 and new_pin.isdigit()): print("Pin lenght should be 4 digits"); os.system("pause"); return
    elif(new_pin != conf_pin): print("New Pin does no match the confirmed Pin "); os.system("pause"); return
    else: rec.loc[index_no, 'Card_Pin'] = new_pin; print("PIN Change Sucressfully"); rec.to_csv('Main.csv' ,index= False); os.system("pause"); pass; pass

def deposit(index_no):
    os.system('cls'); rec = pd.read_csv("Main.csv",dtype=datatypes); ammount = int(input("Enter the Deposited ammount: ")); pin = input("Enter your pin to conform the transtion: ")
    if(pin != str(rec['Card_Pin'][index_no])): print("Invaild Pin. Try again"); os.system('Pause'); return
    transction_rec = str(rec['Account_No'][index_no]) + '.csv'; tran = pd.read_csv('Transaction/'+transction_rec)
    total = float(ammount) + float(tran['End Balance'].iloc[-1]); date_ = dt.date.today().strftime("%d-%m-%Y"); time_ = dt.datetime.now().strftime("%H:%M:%S")
    tran.loc[len(tran)] = [date_,time_,0,ammount,total]; tran.to_csv('Transaction/'+transction_rec,index=False)
    rec.loc[index_no, 'Total_Deposit'] = total; rec.to_csv("Main.csv",index=False)
    print("Transaction completed"); res = input("Do you want to print receipt(Y/N): ")
    if(res.upper() == 'Y'): print("\t\t RECIPITE \t\t\n"+"_"*42); print("Card:",rec['Card_No'][index_no]); print("Account:",rec["Account_No"][index_no]); print("_"*42); print("Date:",date_); print("Time:",time_); print("_"*42); print("Ammount Deposited:",ammount); print("_"*42); print("End Balance:",total); os.system("pause"); pass; pass

def Withdraw(index_no):
    os.system('cls'); rec = pd.read_csv("Main.csv",dtype=datatypes); ammount = int(input("Enter the Withdrawl ammount: "))
    transction_rec = str(rec['Account_No'][index_no]) + '.csv'; tran = pd.read_csv('Transaction/'+transction_rec); pin = input("Enter your pin to conform the transtion: ")
    if(pin != str(rec['Card_Pin'][index_no])): print("Invaild Pin. Try again"); os.system('Pause'); return
    elif(float(ammount) > float(tran['End Balance'].iloc[-1])): print("Insufficient Funds for transaction"); os.system('Pause'); return
    total = float(tran['End Balance'].iloc[-1]) - float(ammount); date_ = dt.date.today().strftime("%d-%m-%Y"); time_ = dt.datetime.now().strftime("%H:%M:%S")
    tran.loc[len(tran)] = [date_,time_,ammount,0,total]; tran.to_csv('Transaction/'+transction_rec,index=False); rec.loc[index_no, 'Total_Deposit'] = total; rec.to_csv("Main.csv",index=False)
    print("Transaction completed"); res = input("Do you want to print receipt(Y/N): ")
    if(res.upper() == 'Y'): print("\t\t RECIPITE \t\t\n"+"_"*42); print("Card:",rec['Card_No'][index_no]); print("Account:",rec["Account_No"][index_no]); print("_"*42); print("Date:",date_); print("Time:",time_); print("_"*42); print("Ammount Withdraw:",ammount); print("_"*42); print("End Balance:",total); os.system("pause"); pass; pass

def graph_(file, L_enters):
    plot_file = pd.read_csv(file); Date = plot_file['Date'].tail(L_enters); Withdraw = plot_file['Withdrawl'].tail(L_enters); Deposit = plot_file['Deposit'].tail(L_enters)
    Date_d = [0]; Withdraw_d = []; Deposit_d = []
    for i in range(len(Date)):
        if(Date_d[-1] != Date.iloc[i]): Date_d.append(Date.iloc[i]); Withdraw_d.append(float(Withdraw.iloc[i])); Deposit_d.append(float(Deposit.iloc[i])); pass
        else: Withdraw_d[-1] = Withdraw_d[-1] + float(Withdraw.iloc[i]); Deposit_d [-1] = Deposit_d[-1] + float(Deposit.iloc[i]); pass; pass
    Date_d.pop(0); x = np.arange(len(Date_d)); plt.bar(x-0.2,Withdraw_d,color = 'Red',width=0.4,label = 'Withdraw'); plt.bar(x+0.2,Deposit_d,color = 'Green',width=0.4,label = 'Deposit'); plt.title("LAST TRANSTION",color = 'Black'); plt.xlabel("Transtion Date", color = 'Orange'); plt.ylabel("Amount", color = 'Blue'); plt.xticks(x,Date_d); plt.legend(); plt.show(); pass

def view_History(account):
    os.system('cls'); tran_file = 'Transaction/'+ str(account) + ".csv"; tran_rec = pd.read_csv(tran_file); print("Account No:",account); print("Total Transtions:", len(tran_rec))
    trna_no = int(input("Enter the No of Trnastion you wnat to dispaly: "))
    if(trna_no > len(tran_rec)): print("Please Enter Vaild Range"); os.system('Pause'); return
    print("The Last", trna_no, "for the account: "); print(tran_rec.tail(trna_no)); graph = input("Do you want to see the graph of transtion History(Y/N): ")
    if(graph.upper() == 'Y'): graph_(tran_file,trna_no); pass; pass

def login():
    os.system('cls'); acc = str(input("Enter Card No: ")); pin = str(input("Enter Pin: ")); rf = pd.read_csv("Main.csv",dtype=datatypes)
    for i in range(len(rf['Card_No'])):
        if(str(rf['Card_No'][i]) == acc):
            if(str(rf['Card_Pin'][i] )== pin): print("Login in success Fully"); os.system('pause'); login_interface(i); break
            else: print("Invalid Pin or Card No. Please try again"); os.system('pause'); break
        pass; pass

def login_interface(index_no):
    while(True):
        rf = pd.read_csv("Main.csv",dtype=datatypes); os.system('cls') 
        print("Welocome",rf['First_Name'][index_no],rf['Last_Name'][index_no],"to the User Interface"); print("Name :",rf['First_Name'][index_no],rf['Last_Name'][index_no],end=('\t'*4)); print("Account No:",rf['Account_No'][index_no]); print("Card No:",rf['Card_No'][index_no],end=('\t'*5)); print("Card Pin: XXXX"); print("Bank Name:",rf['Bank_Name'][index_no],end=('\t'*4)); print("IFSC code:",rf['IFSC_CODE'][index_no]); print("Total Deposit:",rf['Total_Deposit'][index_no]); print("Enter commad no to execute the commad or type Logout to leave\n1. Chash Deposit\n2. Chash Withdrawal\n3. PIN Change\n4. Transaction History")
        com = input("Enter your command /> ")
        if(com.lower() == 'logout'): print("Thank You for Login"); os.system('pause'); break
        elif(com == '1'): deposit(index_no); pass
        elif(com == '2'): Withdraw(index_no); pass
        elif(com == '3'): Change_Pin(index_no); pass
        elif(com == '4'): view_History(str(rf['Account_No'][index_no])); pass
        else: print("Please Enter Vaild command. Try again"); os.system('pause'); pass; pass; pass

while(True):
    title(); print(" "); print("Enter commad no to execute the commad or type Exit to leave\n1. Create or Register Account\n2. User login\n3. About project")
    inp = input("Enter your command /> ") 
    if(inp.lower() == "exit"): print("Thank You for visiting"); break
    elif(inp == '1'): create_acc(); pass
    elif(inp == '2'): login(); pass
    elif(inp == '3'): about(); pass
    else: print("Please Enter Vaild command. Try again"); os.system('pause'); pass; pass