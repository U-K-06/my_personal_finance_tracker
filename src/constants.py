from pathlib import Path as path

class Constants:
    PATH_CURRENT:path = path.cwd()
    DUMMY_CSV_PATH:path = './external_data/data.csv'
    JSON_IDS_PATH:path = './external_data/ids.json'
    USER_ACCOUNT_PATH:path = './external_data/user_account.json'
    START_RANDOM_IDS:int = 10000
    END_RANDOM_IDS:int = 100000
    DATA_BODY:{str,list}= {'Amount':[],'Reason':[],'Date':[],'Type':[]}

