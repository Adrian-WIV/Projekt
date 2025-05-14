#imports

import mariadb
import sys

#Klassen



#connect mariadb
def mariadbconnect():
    try:
        conn = mariadb.connect(
            user = "team05",
            password = "7R25Y",
            host = "10.80.0.206",
            port = 3306,
            database = "team05")

    except mariadb.Error as e:
        print(f"Error connecting to MariaDB PLatform: {e}")
        sys.exit(1)
    
    cur = conn.cursor()
    
    return cur, conn

mariadbconnect()
