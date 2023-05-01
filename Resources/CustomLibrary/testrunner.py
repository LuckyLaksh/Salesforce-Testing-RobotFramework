import excel_data_driver as ed
import salesforce_data_driver as sd

excel_path = '/Users/adusumilli/Documents/GitHub/Salesforce-Testing-RobotFramework/Resources/Data/ReadData.xlsx'
# print(ed.read_data(excel_path))
file='/Users/adusumilli/Documents/GitHub/Salesforce-Testing-RobotFramework/Resources/Data/SampleData.xlsx'
data = sd.fetch_contact_details()
ed.write_data(data)


