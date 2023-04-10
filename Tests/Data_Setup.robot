*** Settings ***
Library    SalesforceLibrary.SalesforceLibrary
Variables  ../Credentails/Credentails.py

*** Test Cases ***
Example Test
    Set Login Credentials    ${sandbox['username']}    ${sandbox['password']}    ${sandbox['security_token']}    ${id}    Create Object    Account    Name=Test Account
    Log    ${id}
    Update Object    Account    ${id}    Name=New Test Account
    ${account}    Get Object    Account    ${id}
    Log    ${account['Name']}
    Delete Object    Account    ${id}

