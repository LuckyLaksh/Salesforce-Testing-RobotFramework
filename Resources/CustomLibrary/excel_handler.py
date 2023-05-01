import pandas as pd

def excel_to_json(filepath):
    df = pd.read_excel('/Users/adusumilli/Documents/GitHub/Salesforce-Testing-RobotFramework/Resources/Data/ReadData.xlsx')
    df_json = df.to_json()
    return df_json


# Read data from the a sheet  (Only parameter excel sheet location,consider first row as header)
# Write the data to a sheet (Only parameter excel sheet)
# Read data from multiple sheet and store it
# Writw data to multiple sheet from the stored data

# Specify the header row and data row for a single sheet
# Specify the location of data and store it 

