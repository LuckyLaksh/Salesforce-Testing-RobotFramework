*** Settings ***
Library  SeleniumLibrary
Variables  ../Locators/Locators.py

*** Keywords ***
Check App Title
    Element Should Be Visible  ${core_connect_xp}
