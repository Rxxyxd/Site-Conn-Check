import os
from tabulate import tabulate
import argparse
import validators

import sites_db
import conn_check

def main():
    db = sites_db.Database()

    parser = argparse.ArgumentParser(prog="main.py", description="This is a program to retrieve the status and response time of sites in a database")

    parser.add_argument("-s", "--sites", help="Lists all sites in database", action="store_true")
    parser.add_argument("--run", help="Adds a site to the database", action="store_true")
    parser.add_argument("-d", "--delete", help="Deletes the Database", action="store_true")

    subparser = parser.add_subparsers(title="command COMMAND", dest="command", help="sub-command for help")

    add_parser = subparser.add_parser("add", help="Add a new site to database", )
    add_parser.add_argument("-n", "--name", help="Name of the site", required=True)
    add_parser.add_argument("-u", "--url", help="URL of the site", required=True)

    remove_parser = subparser.add_parser("remove", help="Remove a site from database")
    remove_parser.add_argument("-n", "--name", help="Name of the site", required=True)

    update_parser = subparser.add_parser("update", help="Update a site in database")
    update_parser.add_argument("-n", "--name", help="Name of the site", required=True)
    update_parser.add_argument("-u", "--url", help="URL of the site", required=True)

    args = parser.parse_args()
    with db as _:
    
        if args.sites:
            print(tabulate(db.get_sites(), showindex="never", headers="keys", tablefmt='psql'), end="\r")
            print("\n")
        elif args.run:
            os.system("cls" if os.name == "nt" else "clear")
            try:
                while True:
                    conn_check.updateDb()
                    sitesList = db.get_sites(True)
                    print(tabulate(sitesList, showindex="never", headers="keys", tablefmt='psql'), end="\r")
                    len_sites = len(sitesList.index)
                    print('\033[1A'*(len_sites+3),end="\x1b[2K")
            except KeyboardInterrupt:
                os.system("cls" if os.name == "nt" else "clear")
                print("Exiting...")
                
        elif args.delete:
            db.delete_database()
            print("Database deleted successfully")
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
        elif args.command == "update":
            valid = validators.url(args.url)
            if valid:
                success = db.update_site(args.name.capitalize(), args.url.lower())
                if success:
                    print("Site updated successfully")
                else:
                    print("Site not found")
            else:
                print("URL is not valid. Please enter a valid URL")

if __name__ == "__main__":
    main()