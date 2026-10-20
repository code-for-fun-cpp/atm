import pandas as pd

# dic = {"Account_No":[],
#        "Card_No":[],
#        "First_Name":[],
#        "Last_Name":[],
#        "Card_Pin":[],
#        "Bank_Name":[],
#        "IFSC_CODE":[],
#        "Total_Deposit":[]
#     }
# df = pd.DataFrame(dic)
# df.to_csv("Main.csv", index= False)
# print(df)
df = pd.read_csv('Main.csv')
df = df.sort_values(by=['Card_No'],ascending=True)
for i in range(len(df['Card_No'])):
    if (df['Card_No'][i] == 65432):
        if(df['Card_Pin'][i] == 7781):
            print("Lofing in Sus")
            pass
    pass
#df.to_csv('Main.csv',index=False)
print(df['Total_Deposit'])