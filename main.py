#main.py
import hashlib
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
                hfile  = open(path,'rb')
            except:
                print 'Could not open %s' % path
                continue    

            md5 = hashlib.md5()
            sha1 = hashlib.sha1()
            sha256 = hashlib.sha256()

            #read file in chunks -> definitely a better way to do this
            while True:
                data = hfile.read(128)
                if not data:
                    break
                md5.update(data)
                sha1.update(data)
                sha256.update(data)


            #add key -> value into hashDict
            hashDict[path] = {}
            hashDict[path]['time'] = time.ctime()
            hashDict[path]['md5'] = md5.hexdigest()
            hashDict[path]['sha1'] = sha1.hexdigest()
            hashDict[path]['file'] = _file
            hashDict[path]['dir'] = dirName
            hashDict[path]['sha256'] = sha256.hexdigest()
            hashDict[path]['size'] = os.stat(path)[6] #os.stat size

    #returns the hash dict, key(dir) -> values(hash) Note: md5 hash values for now
    return hashDict

#database -> first attempt will be with sqlite3
#def saveDatabase():

if __name__ == '__main__':
    hashDict = check()
    if hashDict:
        db = database.Init("hash_fs.sqlite")
        result = database.InsertData(db, hashDict)