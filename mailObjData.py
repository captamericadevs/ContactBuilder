import re

#objData Class
class objData:
    mSign = []

    def __init__(self, rawData):
        parsed_fields = []
        re_sig = re.compile(r"\r\n")
        for lines in rawData:
            #already confirmed rawData includes some contact info from dataLoad.py
            signature = re_sig.search(str(lines)) #look for hard returns
            if signature:
                element = lines.split("\r\n") #split there
                #build a single list of the strings that make up each line
                for parts in element:
                    parsed_fields.append(parts)
        
        #use a regular expression to help remove residual metadata from email chains
        junk_words = re.compile("\\b(From:|To:|Cc:|Sent:|Subject:)",re.I) #note: To, From, and Cc could potentially be sources for more contact info not implemented here

        #use list comprehension to build a list of strings that most likely contain contact information (and not metadata)
        self.mSign = [line for line in parsed_fields if (not junk_words.search(line) and ("-----Original Message-----" not in line) and (len(line) > 3))]
            

                                

                
				

