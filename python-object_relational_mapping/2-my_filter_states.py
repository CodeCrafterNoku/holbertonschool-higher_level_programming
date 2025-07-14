#!/usr/bin/python3
"""Lists all states where name matches the argument passed"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get CLI arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Escape single quotes in user input to prevent SQL injection (still using format)
    safe_state_name = state_name.replace("'", "''")

    # Connect to MySQL
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    # Create cursor
    cursor = db.cursor()

    # Format query as required, with escaped input
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(safe_state_name)
    cursor.execute(query)

    # Display results
    for row in cursor.fetchall():
        print(row)

    # Cleanup
    cursor.close()
    db.close()
