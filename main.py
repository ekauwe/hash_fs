from hashlib import md5, sha1
import os
import sys

hashDict = {}

for dirName, subDir, fileList in os.walk(sys.argv[1])
	for _file in fileList:
		hfile  = open(dirName+'/'+_file,'r')
		hashDict[dirName+'/'+_file] = md5(hfile.read()).hexdigest()
		hfile.close()
print hashDict
