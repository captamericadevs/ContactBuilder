from dataLoad import *
from buildContacts import *
from mailObjData import objData

db = []

db = dataLoad.dataLoad()
buildContacts.buildContacts(db)
