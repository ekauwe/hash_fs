from hashlib import md5, sha1
import os
import sys

def check():
    try:
        hashes = hashFiles(sys.argv[1])
        print hashes
    except:
            usage()


def usage():
    print '''
        Usage: 
            ./%s <dir>
        ''' % sys.argv[0]

def hashFiles(_dir):
    hashDict = {}
    for dirName, subDir, fileList in os.walk(_dir):
        for _file in fileList:
            hfile  = open(dirName+'/'+_file,'r')
            hashDict[dirName+'/'+_file] = md5(hfile.read()).hexdigest()
            hfile.close()
    return hashDict

if __name__ == '__main__':
    check()