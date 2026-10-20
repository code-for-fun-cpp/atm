import pandas as pd

def view_History(account):
    tran_file  = 'Transaction/'+ str(account) + ".csv"
    tran_rec = pd.read_csv(tran_file)
    
    pass