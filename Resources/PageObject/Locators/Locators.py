#login page locators 
login_page = {
    "username":"xpath://input[@id='username']",
    "password":"xpath://input[@id='password']",
    "login":"xpath://input[@id='Login']"
    }

#Salesforce setup Home Page

setup_home_page = { 
    "urlprefix":"/lightning/setup/SetupOneHome/home",
    "setupHometab":"(//a[@title='Home'])[1]",
    "objectManager":"(//a[@title='Object Manager'])[1]",
    "objectmangersdbtn":"//a[@title='Object Manager']/parent::li//a[@role='button']",
    "newObjectbtn":"New Object"
}

#salesforce records list view page
records_list_page = {
    "newRecord":"//div[@title='New']/parent::a"
}

#save and edit modal 
record_modal = {
    "savenNew":"//button[text()='Save & New']",
    "save": "//button[text()='Save']",
    "cancel" : "//button[text()='Cancel']"
}

core_connect_xp = "xpath://span[@title='Core Connect']"