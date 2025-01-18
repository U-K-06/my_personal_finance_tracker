import pandas as pd
from matplotlib import pyplot
from pathlib import Path as path
from datetime import date
from constants import Constants
import Generate_id
import json

class UserAccount:
    def __init__(self,user_name:str)->None:
        self.user_name:str = user_name
        self.transactions:pd.DataFrame= pd.DataFrame(Constants.DATA_BODY)
        self.id = Generate_id.generate_random_id()
        

    def __str__(self)->str:
        return self.transactions.to_string() if not self.transactions.empty  else "Account Data is Empty!"
    
    
    def save_data(self)->None:
        with open(Constants.USER_ACCOUNT_PATH,'r') as read_user_data:
            read_json_data = json.load(read_user_data)
        

        data = {"ID":self.id,
                "Name":self.user_name,
                "History":self.transactions.to_dict(orient="list")
                } 
        print(data | read_json_data)
        # with open(Constants.USER_ACCOUNT_PATH,'a') as user_account:
        #     json.dump(data,user_account,indent=4)
        
    def add_transaction(self,transaction:str,reason:str,transaction_type:str)->None:
        data = Constants.DATA_BODY
        data['Amount'].append(transaction)
        data['Reason'].append(reason)
        data['Date'].append(str(date.today()))
        data['Type'].append(transaction_type)
        self.transactions = pd.concat([self.transactions,pd.DataFrame(data)],ignore_index=True)
    
    def get_stats(self)->None:
        return f'''Total Spent: {self.transactions[self.transactions['Type'] == "Given"]}'''



if __name__ == '__main__':
    a = UserAccount("JOHN DOE")
    # a.add_transaction(50,"Pens","Given")
    # a.add_transaction(60,"Food","Given")
    a.add_transaction(200,"eat praku","Taken")
    a.save_data()
