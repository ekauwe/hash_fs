#database.py
import sqlite3

def Init(db_name):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS file_hashes (dtime, dir, file, fullpath, md5Hash, sha1Hash, sha256Hash, fsize)''')
    conn.commit()
    return conn

def InsertData(conn, hashDict):
    c = conn.cursor()
    for key in hashDict:
        #sqldata: {timestamp, dir, file, fullpath, md5, sha1, sha256, size}
        query = "INSERT INTO file_hashes VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (hashDict[key]['time'], hashDict[key]['dir'], hashDict[key]['file'], key, hashDict[key]['md5'], hashDict[key]['sha1'], hashDict[key]['sha256'], hashDict[key]['size'])
        
        c.execute(query)
        conn.commit()
    return 0
    
