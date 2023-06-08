# Site-Conn-Check
A CLI program that requests the header of a website to determine its Status Code and response time and visualizes the data in a static and dynamic table.

**Status: Finished**

If you find any issues feel free to drop them in the issues section.

## Commands

**NOTE: Upon adding you first site a database file will be created**
This will happen everytime you delete or lose your database file.

 - `$ main.py add -n <SiteName> -u <URL>` - Adds a new Site to the database.
 - `$ main.py remove -n <SiteName>` - Removes a Site from the database.
 - `$ main.py update -n <SiteName>` - Updates a Site.
 - `$ main.py -s` - Lists all Sites in the database.
 - `$ main.py -d` - Deletes database file.
 - `$ main.py --run` - Executes status and response time collection. 
