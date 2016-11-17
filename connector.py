import urllib2
import json

class BankConnector(object):
    @classmethod
    def get_all(cls):
        try:
            request = urllib2.urlopen('http://URL-TO-SERVER/banks')
            data = json.loads(request.read())
        except Exception as e:
            raise Exception('Request Error: %s' % e)
        return data

    @classmethod
    def get(cls, BANK_ID=None):
        if BANK_ID is None:
            raise Exception('BANK_ID can not be None')
        try:
            request = urllib2.urlopen('http://URL-TO-SERVER/data/%s' % BANK_ID)
            data = json.loads(request.read())
        except Exception as e:
            raise Exception('Request Error: %s' % e)
        return data


# Usage Example
import pprint

## GET ALL BANKS

banks = BankConnector.get_all()

print "GET_ALL result: ", type(banks), " -- DATA:\n", pprint.pprint(banks)

## GET BANK WITH ID = 0

bank_record = BankConnector.get(0)
print "GET result: ", type(bank_record), " -- DATA:\n", pprint.pprint(bank_record)
