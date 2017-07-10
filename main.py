from hashlib import md5, sha1
import os

hashDict = {}

for dirName, subDir, fileList in os.walk('/home/ekauwe/Downloads/All Tool/'):
	for _file in fileList:
		hfile  = open(dirName+'/'+_file,'r')
		hashDict[dirName+'/'+_file] = md5(hfile.read()).hexdigest()
		hfile.close()
print hashDict
