import csv, re
from getContentFile import *
from mailObjData import objData

#Open the CSV and read in the data
def dataLoad():
    message_content = []

    #pick a file
    filename = getContentFile.getContentFile()
	
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        try:
            re_contact_email = re.compile(r"(\w+)@(\w+).(.*)") #email format
            re_contact_phone = re.compile(r"(\d{3})-(\d{3})-(\d{4})") #phone number format (America)
            for row in reader: #iterate through each row of the csv
                if re_contact_email.search(row[1]) or re_contact_phone.search(row[1]): #if there is a phone number or email in the body
                    message_content.append(row[1].split("\r\n\r\n")) #divide the message content by intentional linebreaks
        except csv.Error as e: #rudimentary error handler
            sys.exit('file {}, line {}: {}'.format(filename, reader.line_num, e))

    contact_data = []
    for item in message_content:
        #create an object of contact info from the message body (item)
        newObj = objData(item) #create a data object of contact info
        contact_data.append(newObj) #create a list of contact data objects

    return contact_data #return that list of objects
