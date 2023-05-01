*** Settings ***
Library  SeleniumLibrary
Variables  ../Locators/Locators.py
Resource    ../../../venv/lib/python3.9/site-packages/cumulusci/robotframework/perftests/short/collection_perf.robot

*** Keywords ***
Go to Account Page
    Click Element  ${app_launcher['wraffle']}
    Wait Until Element Is Visible  ${app_launcher['searchApp']}
    Input Text  ${app_launcher['searchApp']}  Accounts
    Sleep  5s
    # Mouse Over  ${app_launcher['Accounts']}
    # Click Element  ${app_launcher['Accounts']}
    # Sleep  5s
    Press Keys  ${app_launcher['searchApp']}  RETURN

Create a New Account
    [Arguments]  ${accountName}  ${accountPhone}
    Click Element  ${records_list_page['newRecord']}
    Sleep  3s
    Input Text  ${accounts_modal['accountName']}  ${accountName}
    Input Text  ${accounts_modal['phone']}  ${accountPhone}
    Click Element  ${record_modal['save']}

Create Multiple Accounts
    [Arguments]  ${accountName}  ${accountPhone}
    Click Element  ${records_list_page['newRecord']}
    Input Text ${accounts_modal['accountName']}  ${accountName}
    Input Text ${accounts_modal['phone']}  ${accountPhone}
    Click Element ${record_modal['savenNew']}
