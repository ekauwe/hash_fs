#database.py
import sqlite3

def Init(db_name):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS file_hashes (date, file, md5Hash, sha1Hash, sha256Hash)''')
    conn.commit()
    return conn

def InsertData(conn, hashDict):
    c = conn.cursor()
    for key in hashDict:
        query = "INSERT INTO file_hashes VALUES ('%s', '%s', '%s', '%s', 0)" % (hashDict[key]['time'], key, hashDict[key]['md5'], hashDict[key]['sha1'])
        #print query
        c.execute(query)
        conn.commit()
    return 0
    
