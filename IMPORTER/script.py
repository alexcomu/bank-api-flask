from pymongo import MongoClient
import csv

client = MongoClient('mongodb://localhost:27017/')
db = client.bank

with open('bank.csv', 'r') as csvfile:
    bank_csv = csv.DictReader(csvfile)

    banks = []
    print "Collecting Data.."
    for row in bank_csv:
        db.data.insert({
            "EXPOSURE_COUNTRY": row['Sovereign exposure country'],
            "GDP_2012_EURO": row['GDP 2012 Euro'],
            "MILLIONS_EUROS": row['Millions of Euros'],
            "COUNTRY_EXPOSURE": row['Country as % of bank\'s EEA gross  exposure'],
            "BANK_COUNTRY": row['Bank origin country name'],
            "BANK": row['Bank']
        })

        if row['Bank'] not in banks:
            banks.append(row['Bank'])
    print "Data OK"
    print "Collecting Bank Names.."
    for index, bank in enumerate(banks):
        db.bank.insert({"BANK": bank, "BANK_ID": index})

print "Complete"

'''
DATA EXAMPLE

{'Sovereign exposure country': 'Moon',
'GDP 2012 Euro': '6,755.90',
'Millions of Euros': '0.00',
"Country as % of bank's EEA gross  exposure": '0.00',
'Bank origin country name': 'Mars',
'Bank': 'Pippo Bank'}
'''
