#!/usr/bin/python3
# Lists all states from the database hbtn_0e_0_usa.
#!/usr/bin/python3.8
# Lists all states from the database hbtn_0e_0_usa.
# Usage: ./0-select_states.py <mysql username> \
#                             <mysql password> \
#                             <database name>

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect( host = "localhost", user=sys.argv[1], passwd=sys.argv[2],db=sys.argv[3], port = 3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    rows = cur.fetchall()

    for row in rows:
        print(row)
    cur.close()
    db.close()



