import excel_data_driver as ed
excel_path = '/Users/adusumilli/Documents/GitHub/Salesforce-Testing-RobotFramework/Resources/Data/ReadData.xlsx'
# print(ed.read_data(excel_path))

data = [
    {"Name": "John", "Age": 30, "Gender": "Male"},
    {"Name": "Jane", "Age": 25, "Gender": "Female"},
    {"Name": "Bob", "Age": 35, "Gender": "Male"}
]
file='/Users/adusumilli/Documents/GitHub/Salesforce-Testing-RobotFramework/Resources/Data/SampleData.xlsx'
ed.write_data(data,file,'data')
print('Success 1')
ed.write_data(data)
print('Success 2')