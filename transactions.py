import pandas as pd
from matplotlib import pyplot
from pathlib import Path as path
from tkinter import filedialog
from datetime import date

PATH_CURRENT = path.cwd()

class UserAccount:
    def __init__(self,user_name:str)->None:
        self.user_name:str = user_name
        self.total_money:int|None = 0
        self.reason:str|None = None
        self.transactions:dict[str:list[int],str:list[str],str:list[date],str:list[str]] = {'Transactions':[],'Reason':[],'Date':[],'Type':[]}
        self.stats = {}

    def __str__(self)->str:
        return pd.DataFrame(self.transactions).to_string() if self.transactions  else "Account Data is Empty!"
    
    def save_data(self,file_name,path=PATH_CURRENT)->None:
        if path == PATH_CURRENT: #check weather the file in the cwd or if the path needs to made dynamically
             pd.DataFrame(self.transactions).to_csv(file_name,mode='a')
        else:
            pd.DataFrame(self.transactions).to_csv(path.joinpath(path,file_name),mode='a')

    def add_transaction(self,transaction:str,reason:str,transaction_type:str)->None:
        self.transactions['Transactions'].append(transaction)
        self.transactions['Reason'].append(reason)
        self.transactions['Date'].append(date.today())
        self.transactions['Type'].append(transaction_type.capitalize())

class TransactionMangament:
    def __init__(self):
        self.accounts:dict[str:str] = {}
    def add_account(self,user_name):
        self.accounts[user_name] = UserAccount(user_name)
    


if __name__ == '__main__':
    
