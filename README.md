![GitHub](https://img.shields.io/github/license/rxxyxd/Site-Conn-Check) ![GitHub release (latest by date)](https://img.shields.io/github/v/release/Rxxyxd/Site-Conn-Check) ![GitHub all releases](https://img.shields.io/github/downloads/rxxyxd/Site-Conn-Check/total)
![PyPI](https://img.shields.io/pypi/v/site-conn-check)
# Site-Conn-Check
A CLI program that requests the header of a website to determine its Status Code and response time and visualizes the data in a static and dynamic table.

**Status: Finished**

If you find any issues feel free to drop them in the issues section.

## Set Up

### pip
 - `pip install Site-Conn-Check`
 
### Cloning
After cloning the repository run:
 - `py setup.py install` 

Feel free to clone the repository and make any changes that works for you.


## Commands

**NOTE: Upon adding you first site a database file will be created**
This will happen everytime you delete or lose your database file.

 - `$ site_conn_check add -n <SiteName> -u <URL>` - Adds a new Site to the database.
 - `$ site_conn_check remove -n <SiteName>` - Removes a Site from the database.
 - `$ site_conn_check update -n <SiteName>` - Updates a Site.
 - `$ site_conn_check -s` - Lists all Sites in the database.
 - `$ site_conn_check -d` - Deletes database file.
 - `$ site_conn_check --run` - Executes status and response time collection. 
