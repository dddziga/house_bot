import sqlite3

class BotDB:
    
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file, check_same_thread=False)
        self.cursor = self.conn.cursor()

    def avto_exists(self, avto):
        sql = "SELECT '+' || Phone FROM nomera WHERE avto=:avto"
        result = self.cursor.execute(sql,{'avto':avto})
        return result.fetchall()

    def close(self):
        self.conn.close()
