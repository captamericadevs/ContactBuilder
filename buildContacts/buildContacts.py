import csv, re
from mailObjData import objData

#Write a CSV file with the extracted contact list
def buildContacts(db):
	with open('ContactList.csv', 'wt') as f:
                writer = csv.writer(f)
                for item in db:
                        writer.writerow(item.mSign)
