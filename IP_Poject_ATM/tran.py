import pandas as pd

tran = {
    "Date":[],
    "Time":[],
    "Withdrawl":[],
    "Deposit":[],
    "End Balance":[]
}

tr = pd.DataFrame(tran)
df = pd.read_csv("Main.csv")
r = df['Account_No']
for i in range(len(r)):
    c  = str(df['Account_No'][i]) + ".csv"
    tr['End Balance'] = df['Total_Deposit'][i]
    tr.to_csv("Transaction/"+c,index=False)
