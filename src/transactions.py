import pandas as pd
from matplotlib import pyplot
from pathlib import Path as path
from datetime import date
from constants import Constants
import Generate_id
class UserAccount:
    def __init__(self,user_name:str)->None:
        self.user_name:str = user_name
        self.transactions:pd.DataFrame= pd.DataFrame({'Amount':[],'Reason':[],'Date':[],'Type':[]})
        self.id = Generate_id.generate_random_id()
        


    def __str__(self)->str:
        return self.transactions.to_string() if not self.transactions.empty  else "Account Data is Empty!"
    
    
    def save_data(self,file_name=None,path=Constants.PATH_CURRENT)->None:
        if path == Constants.PATH_CURRENT: #check weather the file in the cwd or if the path needs to made dynamically
             self.add_transaction.to_csv(file_name,mode='a')
        else:
            self.transactions.to_csv(path.joinpath(path,(file_name or self.user_name+'_user_account_data'),mode='a'))

    def add_transaction(self,transaction:str,reason:str,transaction_type:str)->None:
        self.transactions['Amount']
        self.transactions['Reason'].combine(reason)
        self.transactions['Date'].combine(date.today())
        self.transactions['Type'].combine(transaction_type.capitalize())
    
    def get_stats(self)->None:
        return f'''Total Spent: {self.transactions[self.transactions['Type'] == "Given"]}'''

# class TransactionMangament:
#     def __init__(self):
#         self.accounts:dict[str:str] = {}
#     def add_account(self,user_name:UserAccount):
#         self.accounts[user_name.user_name] = UserAccount(user_name)

if __name__ == '__main__':
    a = UserAccount("JOHN DOE")
    a.add_transaction(50,"Pens","Given")
    a.add_transaction(60,"Food","Given")
    print(a)
