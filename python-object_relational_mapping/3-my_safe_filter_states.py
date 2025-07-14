#!/usr/bin/python3
"""Safely lists all states where name matches the argument (prevents SQL injection)"""

import MySQLdb
import sys

if __name__ == "__main__":
    # CLI arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    # Cursor to execute secure parameterized query
    cursor = db.cursor()

    # Use %s to safely pass user input
    cursor.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC", (state_name,))

    # Print results
    for row in cursor.fetchall():
        print(row)

    # Cleanup
    cursor.close()
    db.close()
