import requests
import site_conn_check.sites_db as sites_db

def getStatus(url):
    try:
        response = requests.head(url, timeout=1)
        response_time = response.elapsed.total_seconds() * 1000
        return response.status_code, response_time
    except requests.exceptions.ConnectTimeout:
        return "Timed Out", 0


def updateDb():
    sites = sites_db.Database()
    with sites as db:
        urls = sites.get_urls()
        urls = [i[0] for i in urls] 
    with sites as db:
        for url in urls:
            status_code, response_time = getStatus(url)
            if status_code is not None:
                sites.update_status_code(url, status_code, response_time)


