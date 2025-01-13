import pandas as pd

# Sample DataFrame
data = {
    'Amount': [100, 200, 150, 300],
    'Reason': ['Groceries', 'Rent', 'Utilities', 'Entertainment'],
    'Date': ['2024-01-01', '2024-02-01', '2024-03-01', '2024-04-01'],
    'Type': ['Given', 'Received', 'Given', 'Received']
}
df = pd.DataFrame(data)

# Filter rows where Type is 'Given'
filtered_df = df[df['Type'] == 'Given']

print(filtered_df)
