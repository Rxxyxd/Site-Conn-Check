import os
from tabulate import tabulate
from urllib.parse import urlparse
import argparse
import validators

import sites_db
import conn_check


db = sites_db.Database()

parser = argparse.ArgumentParser(prog="main.py", description="This is a program to retrieve the status and response time of sites in a database")

parser.add_argument("-s", "--sites", help="Lists all sites in database", action="store_true")
parser.add_argument("--run", help="Adds a site to the database", action="store_true")

subparser = parser.add_subparsers(title="command COMMAND", dest="command", help="sub-command for help")

add_parser = subparser.add_parser("add", help="Add a new site to database", )
add_parser.add_argument("-n", "--name", help="Name of the site", required=True)
add_parser.add_argument("-u", "--url", help="URL of the site", required=True)

remove_parser = subparser.add_parser("remove", help="Remove a site from database")
remove_parser.add_argument("-n", "--name", help="Name of the site", required=True)

update_parser = subparser.add_parser("update", help="Update a site in database")
update_parser.add_argument("-n", "--name", help="Name of the site", required=True)
update_parser.add_argument("-u", "--url", help="URL of the site", required=True)

search_parser = subparser.add_parser("search", help="Search for a site from database")
search_parser.add_argument("-n", "--name", help="Name of the site")
search_parser.add_argument("-u", "--url", help="URL of the site, must start with 'https://www.'")

args = parser.parse_args()
with db as _:
    if __name__ == "__main__":
        if args.sites:
            print(tabulate(db.get_sites_detailed(), showindex="never", headers="keys", tablefmt='psql'), end="\r")
            print("\n")
        elif args.run:
            os.system("cls" if os.name == "nt" else "clear")
            while True:
                conn_check.updateDb()
                sitesList = db.get_sites(True)
                print(tabulate(sitesList, showindex="never", headers="keys", tablefmt='psql'), end="\r")
                len_sites = len(sitesList.index)
                print('\033[1A'*(len_sites+3),end="\x1b[2K")
    
        elif args.command == "add":
            valid = validators.url(args.url)
            if valid:
                success = db.add_site(args.name.capitalize(), args.url.lower())
                if success:
                    print("Site added successfully")
                else:
                    print("Supplied URL or Name already exists")
            else:
                print("URL is not valid. Please enter a valid URL")
        elif args.command == "remove":
            success = db.remove_site(args.name.capitalize())
            if success:
                print("Site removed successfully")
            else: 
                print("Site not found")






    #os.system("cls" if os.name == "nt" else "clear")
    #with db as _:
    #    sitesList = db.get_sites()

    #while True:
    #    conn_check.updateDb()
    #    with db as _:
    #        sitesList = db.get_sites()
    #    print(tabulate(sitesList, showindex="never", headers="keys", tablefmt='psql'), end="\r")
    #    len_sites = len(sitesList.index)
    #    print('\033[1A'*(len_sites+3),end="\x1b[2K")
        