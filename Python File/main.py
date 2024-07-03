import sqlite3

#function to define database
class Database:
    def __init__(self, db_name='student.db'):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS STUD_REGISTRATION (
            STU_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            STU_NAME TEXT,
            STU_CONTACT TEXT,
            STU_EMAIL TEXT,
            STU_REGNO TEXT,
            STU_DEPARTMENT TEXT
        )''')
        self.conn.commit()

    def execute_query(self, query, params=()):
        self.cursor.execute(query, params)
        self.conn.commit()

    def fetch_all(self, query, params=()):
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.conn.close()
