import sites_db
import conn_check
import os
import time
from tabulate import tabulate

db = sites_db.Database()

if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    with db as _:
        sitesList = db.get_sites()

    while True:
        conn_check.GetStatus().run()
        with db as _:
            sitesList = db.get_sites()
        print(tabulate(sitesList, showindex="never", headers="keys", tablefmt='psql'), end="\r")
        len_sites = len(sitesList.index)
        print('\033[1A'*(len_sites+3),end="\x1b[2K")
        