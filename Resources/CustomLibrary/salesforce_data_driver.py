from simple_salesforce import Salesforce
from collections import OrderedDict
import PageObject.Credentails.Credentails as creds
sf = Salesforce(username=creds.sandbox['username'], password=creds.sandbox['password'], security_token=creds.sandbox['9heIwmrbgW7MHyyvr5CkIht0'],domain='test')

def ordereddict_to_dict(ordered_dict):
    if not isinstance(ordered_dict, OrderedDict):
        return ordered_dict

    return dict((k, ordereddict_to_dict(v)) for k, v in ordered_dict.items())

def fetch_contact_details():
    contact_data = []
    query = "SELECT Id, FirstName, LastName,Email,Phone,Account.Id FROM Contact"
    records = sf.query(query)['records']
    for record in records:
        row = {}
        data_key_list = list(record.keys())
        for l in data_key_list:
            if l != 'attributes' and l != 'Account':
                row[l] = record[l]
            elif l == 'Account':
                row['AccountId'] = record['Account']['Id']
        contact_data.append(row)
    return contact_data

        
        
    # return contact_data


def fetch_account_details():
    account_data = []
    query = "SELECT Id,Name,Phone From Account"
    records = sf.query(query)['records']
    for record in records:
        row = {}
        data_key_list = list(record.keys())
        for l in data_key_list:
            if l != 'attributes':
                row[l] = record[l]
            elif l == 'attributes':
                row['Id'] = record['attributes']['Id']
            account_data.append(row)
        return account_data


def metadata_copy(source_sf,target_sf):
    metadata.source_sf.describe()
    target_sf.metadata.create(metadata)

def data_copy(source_sf,target_sf,query,object):
    data = source_sf.query_all(query)['records']
    for record in data:
        target_sf.object.create(record)

