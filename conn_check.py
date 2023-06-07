import requests
import threading
import sites_db
import time


class GetStatus():
    def __init__(self):
        self.lock = threading.Lock()

    def getStatus(self, url):
        response = requests.head(url)
        response_time = response.elapsed.total_seconds()
        return response.status_code, response_time

    def updateDb(self):
        try:
            sites = sites_db.Database()
            with sites as db:
                urls = sites.get_urls()
                urls = [i[0] for i in urls] 
            def multiThreadRequest():
                with sites as db:
                    for url in urls:
                        status_code, response_time = self.getStatus(url)
                        #print(status_code, x)
                        sites.update_status_code(urls[x], status_code, response_time)
            def singleThreadRequest():
                with sites as db:
                    for url in urls:
                            status_code, response_time = self.getStatus(url)
                            print(status_code, url)
                            sites.update_status_code(url, status_code, response_time)
            return multiThreadRequest, singleThreadRequest
        finally:
            
            print("process finished")

    def run(self,multiThread=False, threadsCount=10):
        multi, single = self.updateDb()
        if not isinstance(multiThread, bool):
            raise TypeError("multiThread arguement must be a boolean")
        elif multiThread:
            threads = []
            for x in range(threadsCount):
                print(f"thread {x+1} started")
                time.sleep(5)
                t = threading.Thread(target=multi)
                threads.append(t) 
                t.start()
            for thread in threads:
                thread.join()
        else:
            single()

x=True
GetStatus().run(True)