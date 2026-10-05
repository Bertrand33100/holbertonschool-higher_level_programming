#!/usr/bin/python3
"""Safely displays all values in the states table where name matches."""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = %s ORDER BY id",
                (sys.argv[4],))
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()
