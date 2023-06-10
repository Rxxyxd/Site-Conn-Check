import os
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine, Column, Integer, String
import pandas as pd

engine = create_engine("sqlite:///sites.db")
conn = engine.connect()
Base = declarative_base()

class Sites(Base):
    __tablename__ = "Sites"

    id = Column(Integer, primary_key=True)
    site_name = Column(String(100))
    site_url = Column(String(100))
    response_time = Column(Integer)
    status_code = Column(String(100))

Base.metadata.create_all(engine)

class Database():


    def __init__(self):
        self.Session = None
        self.session = None


    def __enter__(self):
        self.Session = sessionmaker(bind = engine)
        self.session = self.Session()


    def add_site(self, name, url):
        result_name = self.session.query(Sites).filter(Sites.site_name == name).first()
        result_url = self.session.query(Sites).filter(Sites.site_url == url).first()
        if result_name or result_url:
            return False
        if not result_url and not result_name:
            s1 = Sites(site_name=name, site_url=url)
            self.session.add(s1)
            return True


    def remove_site(self, name):
        result_name = self.session.query(Sites).filter(Sites.site_name == name).first()
        if result_name:
            self.session.query(Sites).filter(Sites.site_name == name).delete()
            return True
        else:
            return False


    def get_sites(self, detailed=False):
        if not isinstance(detailed, bool):
            raise TypeError('detailed argument must be a bool')
        if detailed:
            df = pd.read_sql(self.session.query(Sites).with_entities(Sites.site_name, Sites.site_url, Sites.response_time, Sites.status_code).statement, self.session.bind)
            return df
        else:
            sites = pd.read_sql(self.session.query(Sites).with_entities(Sites.site_name, Sites.site_url).statement, self.session.bind)
            return sites
        

    def get_urls(self):
        all_url = self.session.query(Sites.site_url).all() 
        return all_url
   
    def update_site(self, name, url):
        result_name = self.session.query(Sites).filter(Sites.site_name == name).first()
        if result_name:
            self.session.query(Sites).filter(Sites.site_name == name).update({'site_name': name, 'site_url': url})
            return True
        else:
            return False

    def update_status_code(self, url, code, response_time):
        self.session.query(Sites).filter(Sites.site_url == url).update({'status_code': code, 'response_time': response_time})

#    def get_number_of_rows(self):
#        self.cursor.execute('''
#            SELECT COUNT(*) FROM sites
#        ''')
#        return self.cursor.fetchone()[0]
    
#    def get_status_code(self, name):
#        self.cursor.execute('''
#            SELECT status FROM sites
#            WHERE name = ?
#        ''', (name,))
#        return self.cursor.fetchone()[0]
#    
    def delete_database(self):
        conn.close()
        os.remove("sites.db")
#
    def update_response(self, url, response):
        self.session.query(Sites).filter(Sites.site_url == url).update({'response_time': response})
#
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.commit()