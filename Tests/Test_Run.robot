*** Settings ***
Documentation     Simple example using SeleniumLibrary.
Library           SeleniumLibrary
Resource          ../Resources/PageObject/KeywordDefinationFiles/Login.robot
Resource          ../Resources/PageObject/KeywordDefinationFiles/SalesforceHomePage.robot

*** Variables ***
${LOGIN URL}      https://test.salesforce.com
${BROWSER}        Chrome

*** Test Cases ***
Validate Login
    Open Browser     ${LOGIN URL}    ${BROWSER}
    Login to Salesforce 
    Sleep  5s
    Check App Title
    Sleep  10s
    Close Browser