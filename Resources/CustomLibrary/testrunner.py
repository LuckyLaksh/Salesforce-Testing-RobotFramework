from excel_data_driver import excel_data_driver as ed
from salesforce_data_driver import salesforce_data_driver as sd
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'PageObject','Credentails')))
from Credentails import sandbox
excel_path = '/Users/adusumilli/Documents/GitHub/Salesforce-Testing-RobotFramework/Resources/Data/ReadData.xlsx'
# print(ed.read_data(excel_path))
file='/Users/adusumilli/Documents/GitHub/Salesforce-Testing-RobotFramework/Resources/Data/SampleData.xlsx'
sdobj = sd()
data = sdobj.fetch_contact_details(sandbox)
excelobj = ed()
excelobj.write_data(data)


