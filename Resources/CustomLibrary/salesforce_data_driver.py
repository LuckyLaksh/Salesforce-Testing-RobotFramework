from simple_salesforce import Salesforce
import os
import sys

class salesforce_data_driver:
    def fetch_contact_details(self,connection):
        contact_data = []
        sf = Salesforce(username=connection['username'],password=connection['password'],security_token=connection['security_token'],domain=connection['domain'])
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
    def fetch_account_details(self,connection):
        account_data = []
        sf = Salesforce(username=connection['username'],password=connection['password'],security_token=connection['security_token'],domain=connection['domain'])
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