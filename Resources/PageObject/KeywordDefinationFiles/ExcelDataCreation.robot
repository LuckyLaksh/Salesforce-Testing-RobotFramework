*** Settings ***
Library    ExcelLibrary
Library    SalesforceLibrary.SalesforceLibrary
Variables  ../Credentails/Credentails.py

*** Keywords ***
Connect to Salesforce Org
Set Login Credentials    ${sandbox['username']}    ${sandbox['password']}    ${sandbox['security_token']}
Check Operator from Excel
    ${path} = 'Resources/Data/SalesforceSampleData.xlsx'
    Open Excel ${path}
    ${operator}  Read Cell Sheet1 B2
    ${object}  Read Cell Sheet1 A2     
    If '${operator}' == 'Read' Fetch Records ${object}
    ELSE If  '${operator}' == 'Create' Create Records ${object}
    ELSE If  '${operator}' == 'Update' Update Records  ${object} 
    ELSE If  '${operator}' == 'Delete' Delete Record  ${object}

Fetch Records 

Create Records {$object}

Update Records

Delete Record