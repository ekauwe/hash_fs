#main.py
import hashlib
import json
import os
import database
import sys
import time

class Hash_fs(object):
    def __init__(self, file, dir='./'):
        if isinstance(file, list):
            self.dir = dir
            self.file = enumerate(file)
        else:
            self.dir = dir
            self.file = file

    def run(self):
        if isinstance(self.file, enumerate):
            output = {}
            for i, f in self.file:
                path = os.path.join(self.dir,f)
                output[path] = self.getHashes(path)
            if output:
                return output
            return None

        else:
            path = os.path.join(self.dir, self.file)
            return self.getHashes(path)

    def getHashes(self, path):
         #read the file 
        try:
            hfile  = open(path,'rb')
        except:
            print 'Could not open %s' % path
            return    

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
        hashDict = {}
        hashDict[path] = {}
        hashDict[path]['time'] = time.ctime()
        hashDict[path]['md5'] = md5.hexdigest()
        hashDict[path]['sha1'] = sha1.hexdigest()
        hashDict[path]['file'] = self.file
        hashDict[path]['dir'] = self.dir
        hashDict[path]['sha256'] = sha256.hexdigest()
        hashDict[path]['size'] = os.stat(path)[6] #os.stat size

        #returns the hash dict, key(dir) -> values(hash) Note: md5 hash values for now
        return hashDict

if __name__ == '__main__':
    for dir, subDir, fileList in os.walk(sys.argv[1]):
        test = Hash_fs(fileList, dir)
        print test.run()