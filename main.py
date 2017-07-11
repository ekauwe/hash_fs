#main.py
from hashlib import md5, sha1, sha256
import json
import os
import database
import sys
import time


#check to see if error on dir is thrown, default to usage 
def check():
    try:
        hashes = hashFiles(sys.argv[1])
        return hashes
    except:
            usage()
            return 0

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
            hfile  = open(dirName+'/'+_file,'r')
            #add key -> value into hashDict
            hashDict[dirName+'/'+_file] = {}
            hashDict[dirName+'/'+_file]['time'] = time.ctime()
            hashDict[dirName+'/'+_file]['md5'] = md5(hfile.read()).hexdigest()
            hashDict[dirName+'/'+_file]['sha1'] = sha1(hfile.read()).hexdigest()
            hashDict[dirName+'/'+_file]['file'] = _file
            hashDict[dirName+'/'+_file]['dir'] = dirName
            hashDict[dirName+'/'+_file]['sha256'] = sha256(hfile.read()).hexdigest()
            hashDict[dirName+'/'+_file]['size'] = 'wip_size'

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