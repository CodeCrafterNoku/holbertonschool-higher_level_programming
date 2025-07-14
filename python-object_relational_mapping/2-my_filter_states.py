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

    # Connect to MySQL
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    # Cursor to execute query
    cursor = db.cursor()

    # WARNING: using .format() as required by the task, not parameterized query
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name)
    cursor.execute(query)

    # Fetch and print
    for row in cursor.fetchall():
        print(row)

    # Cleanup
    cursor.close()
    db.close()
