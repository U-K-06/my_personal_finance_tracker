from pathlib import Path as path

class Constants:
    PATH_CURRENT:path = path.cwd()
    DUMMY_CSV_PATH:path = './external_data/data.csv'
    JSON_IDS_PATH:path = './external_data/ids.json'
    START_RANDOM_IDS:int = 10000
    END_RANDOM_IDS:int = 100000

