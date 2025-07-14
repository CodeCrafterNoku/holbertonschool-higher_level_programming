#!/usr/bin/python3
"""Lists all cities and their corresponding state names from hbtn_0e_4_usa"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get CLI args
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to DB
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    # Cursor
    cursor = db.cursor()

    # Execute JOIN query: city id, city name, state name
    cursor.execute("""
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
    """)

    # Display results
    for row in cursor.fetchall():
        print(row)

    # Cleanup
    cursor.close()
    db.close()
