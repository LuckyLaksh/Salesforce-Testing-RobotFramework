*** Settings ***
Documentation     Simple example using SeleniumLibrary.
Library           SeleniumLibrary
Library           /Users/adusumilli/Documents/GitHub/Salesforce-Testing-RobotFramework/Resources/CustomLibrary/utility.py
Resource          ../Resources/PageObject/KeywordDefinationFiles/Login.robot
Resource          ../Resources/PageObject/KeywordDefinationFiles/SalesforceHomePage.robot
Resource          ../Resources/PageObject/KeywordBusinessFlows/ContactsPage.robot
Resource          ../Resources/PageObject/KeywordBusinessFlows/AccountsPage.robot

*** Variables ***
${LOGIN URL}      https://test.salesforce.com
${BROWSER}        Chrome

*** Test Cases ***
Validate Login
    ${driver_path}=    utility.Get Driver Path With Browser        ${BROWSER}
    Open Browser     ${LOGIN URL}    ${BROWSER}    executable_path=${driver_path}
    # Open Browser     ${LOGIN URL}    ${BROWSER}
    Login to Salesforce 
    Sleep  10s
    Go to Account Page
    Sleep  5s
    Create a New Account  Test001  8979695431
    Close Browser