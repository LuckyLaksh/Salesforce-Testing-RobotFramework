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
#salesforce app launcher wraffle
app_launcher = {
    "wraffle":"//div[contains(@class,'appLauncher')]//button",
    "searchApp":"//input[@placeholder='Search apps and items...']",
    "Accounts":"//*[text()='Accounts']/ancestor::a",
    "Contacts":"//*[text()='Contacts']/ancestor::a"
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

#account creation modal
accounts_modal = {
"modalTitle":"//h2[text()='New Account']",
"accountName":"//label[text()='Account Name']/ancestor::lightning-input//div/input[@name='Name']",
"phone":"//label[text()='Phone']/ancestor::lightning-input//div/input[@name='Phone']"
}

#contact creation modal
contacts_modal = {
"modalTitle":"//h2[text()='New Contact']",
"firstname":"//label[text()='First Name']/ancestor::lightning-input//div/input[@name='firstName']",
"lastname":"//label[text()='Last Name']/ancestor::lightning-input//div/input[@name='lastName']",
"phone":"//label[text()='Phone']/ancestor::lightning-input//div/input[@name='Phone']",
"email":"//label[text()='Email']/ancestor::lightning-input//div/input[@name='Email']",
"accountName":"//label[text()='Account Name']/ancestor::lightning-grouped-combobox//input",
"accountNamefirstValue":"(//lightning-base-combobox-formatted-text)[1]"
}
