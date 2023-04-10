*** Settings ***
Library    SeleniumLibrary
Variables  ../Locators/Locators.py
Variables  ../Credentails/Credentails.py

# Library    Locators
# Library    Credentails

*** Keywords ***
Login to Salesforce 
    Input Text  ${login_page['username']}  ${sandbox['username']}
    Input Text  ${login_page['password']}  ${sandbox['password']}
    Click Element  ${login_page['login']}


# Reference Links :  https://testersdock.com/robot-framework-page-object-model/
