import pandas as pd
import functions_atm.Data_types as dt # to specify the data types of Main.csv
import os # used to give commands to cmd

def Change_Pin(index_no):
    os.system("cls") # Clear the terminal
    rec  = pd.read_csv("Main.csv",dtype=dt.datatypes)
    old_pin = input("Current Pin: ")
    new_pin = input("New Pin: ")
    conf_pin = input("Confirm the Pin: ")
    if(old_pin != str(rec['Card_Pin'][index_no])): #verifyes the Pin 
        print("Please Enter Correct Current Pin")
        os.system("pause") # To pause the terminal
        return
    elif(len(new_pin) != 4 and new_pin.isdigit()): # Check the len of the new pin
        print("Pin lenght should be 4 digits")
        os.system("pause")
        return
    elif(new_pin != conf_pin): # confirmes the New Pin
        print("New Pin does no match the confirmed Pin ")
        os.system("pause")
        return
    else:
        rec.loc[index_no, 'Card_Pin'] = new_pin # set the new pin
        print("PIN Change Sucressfully")
        rec.to_csv('Main.csv' ,index= False)
        os.system("pause") 
        pass
    pass