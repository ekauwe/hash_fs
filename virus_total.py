#virus_total.py
import requests
import json

'''params = {'apikey': '', 'resource': '37ce1d1f37ca01eed2a723120edf877b0f3ca7c86102f1ff2d16ab091f1fe4a9'}

headers = {
      	  	"Accept-Encoding": "gzip, deflate",
      		"User-Agent" : "gzip,  My Python requests library example client or username"
          }

response = requests.get('https://www.virustotal.com/vtapi/v2/file/report',
     					 params=params, headers=headers)
data = response.json()

print ' '.join([ i for i in data['scans'] if data['scans'][i]['detected'] ])

'''
import json
import database

f = open('test.txt', 'r')
data = json.load(f)
f.close()

class Vt(object):
	def __init__(self):
		return None
	def detected(self, data):
		self.detected = [i for i in data['scans'] if data['scans'][i]['detected']]
		if self.detected:
			return self.detected
		else:
			return False

i = Vt()
print i.detected(data)
test = [[u'CAT-QuickHeal', u'McAfee'],'True','37ce1d1f37ca01eed2a723120edf877b0f3ca7c86102f1ff2d16ab091f1fe4a9']
db = database.Init("hash_fs.sqlite")
if database.VtInsert(db, test):
	print "fail"


