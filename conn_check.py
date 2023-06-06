import requests
#import threading
import sites_db

sites = sites_db.Database()

def getStatusCode(url):

    response = requests.head(url)
    response_time = response.elapsed.total_seconds()
    return response.status_code, response_time
    
def update_sites_db():
    with sites as db:
        urls = sites.get_urls()
        urls = [i[0] for i in urls] # adds urls to a list
        rows = sites.get_number_of_rows()
    print(urls, rows)
    with sites as db:
        for x in range(rows):
            status_code, response_time = getStatusCode(urls[x])
            print(status_code, x)
            sites.update_status_code(urls[x], status_code, response_time)

update_sites_db()
with sites as db:
    print(sites.get_sites())