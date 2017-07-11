#main.py
from hashlib import md5, sha1, sha256
import json
import os
import database
import sys
import time


#check to see if error on dir is thrown, default to usage 
def check():
    if len(sys.argv) > 2:
        usage()
        return 0
    else:
        hashes = hashFiles(sys.argv[1])
        return hashes

#generic usage, will replace with argparse or something later
def usage():
    print '''
        Usage: 
            ./%s <dir>
        ''' % sys.argv[0]

#main hashing function, takes in directory
def hashFiles(_dir):
    hashDict = {}
    for dirName, subDir, fileList in os.walk(_dir):
        for _file in fileList:
            #read the file 
            path = os.path.join(dirName, _file)
            try:
                hfile  = open(path,'r')
                data = hfile.read()
            except:
                print 'Could not open %s' % path
                continue    
            #add key -> value into hashDict
            hashDict[path] = {}
            hashDict[path]['time'] = time.ctime()
            hashDict[path]['md5'] = md5(data).hexdigest()
            hashDict[path]['sha1'] = sha1(data).hexdigest()
            hashDict[path]['file'] = _file
            hashDict[path]['dir'] = dirName
            hashDict[path]['sha256'] = sha256(data).hexdigest()
            hashDict[path]['size'] = os.stat(path)[6] #os.stat size

            hfile.close()
    #returns the hash dict, key(dir) -> values(hash) Note: md5 hash values for now
    return hashDict

#database -> first attempt will be with sqlite3
#def saveDatabase():

if __name__ == '__main__':
    hashDict = check()
    if hashDict:
        db = database.Init("hash_fs.sqlite")
        result = database.InsertData(db, hashDict)