import requests
import sites_db

def getStatus(url):
    response = requests.head(url)
    response_time = response.elapsed.total_seconds() * 1000
    return response.status_code, response_time

def updateDb():
    sites = sites_db.Database()
    with sites as db:
        urls = sites.get_urls()
        urls = [i[0] for i in urls] 
    with sites as db:
        for url in urls:
            status_code, response_time = getStatus(url)
            sites.update_status_code(url, status_code, response_time)


