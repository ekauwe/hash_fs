#hash_fs.py
import argparse
import hashlib
import database
import os
import sys
import textwrap
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
    parser = parser = argparse.ArgumentParser(
     prog='hash_fs',
     formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent('''\
        Hash_fs:
            Generic hashing script. Hashes files and saves it 
            to a SQLite3 database.
        ------------------------------------------------------------------
            Recursively hash files starting in "/etc" directory: [default pwd]
            %s -d /etc, %s --directory /etc 

            Hash "/etc/hosts" file:
            %s -f /etc/hosts, %s --file /etc/hosts
        
            Specify database: [defaults to hash_fs.sqlite]
            %s -d /etc --db new_hash_fs.sqlite3
        
            Output to file: (in lieu of using db)
            %s -f /etc/hosts -o results.txt, %s -f/etc/hosts --output results.txt
         ''' % (sys.argv[0], sys.argv[0], sys.argv[0], sys.argv[0], sys.argv[0], sys.argv[0], sys.argv[0])))


    parser.add_argument('--directory','-d', dest='dir', action='store',
                    default=os.getcwd(), help='')
    parser.add_argument('--file','-f', dest='file', action='store',
                    default=False, help='')
    parser.add_argument('--db', dest='db', action='store',
                    default='hash_fs.sqlite3', help='')
    parser.add_argument('-o', '--output', dest='output', action='store',
                    default=False, help='')

    args = parser.parse_args()

    if args.file:
        test = Hash_fs(args.file, args.dir)
        results = test.run()
    else:
        for dir, subDir, fileList in os.walk(args.dir):
            test = Hash_fs(fileList, dir)
            results = test.run()
    if args.output:
        print 'insert into file: %s' % args.output
        with open(args.output, 'w') as f:
            f.write(results)
    else:
        print 'insert into db: %s' % args.db
        print results 