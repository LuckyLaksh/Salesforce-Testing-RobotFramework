from simple_salesforce import Salesforce

sf = Salesforce(username='your_username', password='your_password', security_token='your_security_token')

def fetch_contact_details():
    query = "SELECT Id, FirstName, LastName,Email,Phone,Account.Id FROM Contact"
    return sf.query(query)

def fetch_account_details():
    query = "SELECT Id,Name,Phone From Account"
    return sf.query(query)

def metadata_copy(source_sf,target_sf):
    metadata.source_sf.describe()
    target_sf.metadata.create(metadata)

def data_copy(source_sf,target_sf,query,object):
    data = source_sf.query_all(query)['records']
    for record in data:
        target_sf.object.create(record)

