import sqlite3
import os
import pandas as pd

class Database():
    def __init__(self):
        self.connection = None
        self.cursor = None
    
    def __enter__(self):
        self.connection = sqlite3.connect('sites.db', check_same_thread=False)
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
        self.cursor.execute('SELECT name FROM sites WHERE name=?', (name,))
        result_name = self.cursor.fetchone()
        self.cursor.execute('SELECT url FROM sites WHERE url=?', (url,))
        result_url = self.cursor.fetchone()

        if result_name or result_url:
            return False
        if not result_url and not result_name:
            self.cursor.execute('''
                INSERT INTO sites (name, url)
                VALUES (?, ?)
            ''', (name, url))
            return True
    
    def remove_site(self, name):
        self.cursor.execute('SELECT name FROM sites WHERE name =?', (name,))
        result = self.cursor.fetchone()
        if result:
            self.cursor.execute('''
                DELETE FROM sites
                WHERE name = ?
            ''', (name,))
            return True
        else:
            return False

    def get_sites(self, detailed=False):
        if not isinstance(detailed, bool):
            raise TypeError('detailed argument must be a bool')
        if detailed:
            sites = pd.read_sql_query('SELECT name, url, response, status FROM sites', self.connection)
            return sites
        else:
            sites = pd.read_sql_query('SELECT name, url FROM sites', self.connection)
            return sites
        

    def get_urls(self):
        self.cursor.execute('''
            SELECT url FROM sites
        ''')
        return self.cursor.fetchall()
    
    def update_site(self, name, url):
        self.cursor.execute('SELECT name FROM sites WHERE name =?', (name,))
        exists = self.cursor.fetchone()
        if exists:
            self.cursor.execute('''
                        UPDATE sites
                        SET url = ?
                        WHERE name = ?
                    ''', (url, name))
            return True
        else:
            return False

    def update_status_code(self, url, code, response_time):
        self.cursor.execute('''
            UPDATE sites
            SET status = ?, response =?
            WHERE url = ?
        ''', (code, response_time, url))

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