#database.py
import sqlite3

class Sql_hashfs(object):
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        c = self.conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS file_hashes (dtime, dir, file, fullpath, md5Hash, sha1Hash, sha256Hash, fsize, hits, av)''')
        self.conn.commit()
        return None
    
    def InsertData(self, hashDict):
        c = self.conn.cursor()
        for key in hashDict:
            #sqldata: {timestamp, dir, file, fullpath, md5, sha1, sha256, size}
            query = "INSERT INTO file_hashes VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '[]', 'false')" % (hashDict[key]['time'], hashDict[key]['dir'], hashDict[key]['file'], key, hashDict[key]['md5'], hashDict[key]['sha1'], hashDict[key]['sha256'], hashDict[key]['size'])
            c.execute(query)
            self.conn.commit()
        return 0
    
    def VtInsert(self, data):
        c = self.conn.cursor()
        query = "UPDATE file_hashes set hits = \"%s\", av = \"%s\" WHERE sha256Hash='%s'" % (data[0], data[1], data[2])
        c.execute(query)
        self.conn.commit()
        return 0
