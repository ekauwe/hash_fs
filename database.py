#database.py
import sqlite3
import time

def Init(db_name):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS file_hashes (date, file, md5Hash, sha1Hash, sha256Hash)''')
    conn.commit()
    return conn

def InsertData(conn, hashDict):
    c = conn.cursor()
    for key in hashDict:
        query = "INSERT INTO file_hashes VALUES ('%s', '%s', '%s', 0, 0)" % (time.ctime(), key, hashDict[key])
        c.execute(query)
        conn.commit()
    c.execute("select * from file_hashes")
    return 0
    
