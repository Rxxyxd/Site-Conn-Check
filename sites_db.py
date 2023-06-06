import sqlite3
import os

class Database():
    def __init__(self):
        self.connection = None
        self.cursor = None
    
    def __enter__(self):
        self.connection = sqlite3.connect('sites.db')
        self.cursor = self.connection.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS sites (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                url TEXT NOT NULL,
                response INT,
                status integer,
                UNIQUE(name,url)
            )
        ''')
        self.connection.commit()
    
    def add_site(self, name, url):
        self.cursor.execute('''
            INSERT INTO sites (name, url)
            VALUES (?, ?)
        ''', (name, url))
    
    def remove_site(self, name):
        self.cursor.execute('''
            DELETE FROM sites
            WHERE name = ?
        ''', (name,))

    def get_sites(self):
        self.cursor.execute('''
            SELECT name, url, response, status FROM sites
        ''')
        return self.cursor.fetchall()
    
    def update_site(self, name, url):
        self.cursor.execute('''
                    UPDATE sites
                    SET url = ?
                    WHERE name = ?
                ''', (url, name))

    def update_status_code(self, url, code):
        self.cursor.execute('''
            UPDATE sites
            SET status = ?
            WHERE url = ?
        ''', (code, url))

    def get_number_of_rows(self):
        self.cursor.execute('''
            SELECT COUNT(*) FROM sites
        ''')
        return self.cursor.fetchone()[0]
    
    def get_status_code(self, name):
        self.cursor.execute('''
            SELECT status FROM sites
            WHERE name = ?
        ''', (name,))
        return self.cursor.fetchone()[0]
    
    def delete_database(self):
        self.connection.close()
        os.remove('sites.db')

    def update_response(self, url, response):
        self.cursor.execute('''
            UPDATE sites
            SET response = ?
            WHERE url = ?
        ''', (response, url))

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.commit()
        self.connection.close()