#Get CSV file name

def getContentFile():
	#needs a file path
	filename = input('Enter the file location: ')
	if filename == '':
		filename = 'SampleEmailData.csv' #default if no valid input
	return filename
