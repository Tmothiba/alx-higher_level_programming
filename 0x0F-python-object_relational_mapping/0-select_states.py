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
    if len(sys.argv) != 4:
        print("Usage: ./0-select_states.py <mysql username> <mysql password> <database name>")
        sys.exit(1)

    try:
        # Connect to MySQL
        db = MySQLdb.connect(
            host="localhost",
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            port=3306
        )

        # Create a cursor object using cursor() method
        c = db.cursor()

        # Execute SQL query to fetch all states
        c.execute("SELECT * FROM states")

        # Fetch all the rows using fetchall() method
        rows = c.fetchall()

        # Print each row
        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL DB: {e}")
        sys.exit(1)

    finally:
        # Close cursor and connection
        if 'c' in locals():
            c.close()
        if 'db' in locals() and db.open:
            db.close()

