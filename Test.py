import http.cookies as Cookie # some cookie handling support
from http.server import BaseHTTPRequestHandler, HTTPServer # the heavy lifting of the web server
import urllib # some url parsing support
import hashlib
from datetime import datetime
import json # support for json encoding
import sys # needed for agument handling
import sqlite3
import time

# print(datetime.now())




def access_database(dbfile, query):
    connect = sqlite3.connect(dbfile)
    cursor = connect.cursor()
    cursor.execute(query)
    connect.commit()
    connect.close()

# access_database requires the name of an sqlite3 database file and the query.
# It returns the result of the query
def access_database_with_result(dbfile, query):
    connect = sqlite3.connect(dbfile)
    cursor = connect.cursor()
    rows = cursor.execute(query).fetchall()
    connect.commit()
    connect.close()
    return rows


def setup_assessment_tables(dbfile):

    # Freshly setup tables
    access_database(dbfile, "CREATE TABLE IF NOT EXISTS users (userid INTEGER PRIMARY KEY, username TEXT NOT NULL, password TEXT NOT NULL)")
    access_database(dbfile, "CREATE TABLE IF NOT EXISTS session (sessionid INTEGER PRIMARY KEY, userid INTEGER, magic TEXT NOT NULL, start INTEGER, end INTEGER)")
    access_database(dbfile, "CREATE TABLE IF NOT EXISTS traffic (recordid INTEGER PRIMARY KEY, sessionid INTEGER, time INTEGER, type INTEGER, occupancy INTEGER, location TEXT NOT NULL, mode INTEGER)")
    
    

access_database("traffic.db","INSERT INTO traffic (sessionid, time, type, occupancy, location, mode) VALUES  ({0},{1},{2},{3},{4},{5}) ".format(123,5254665,12,2, "'bath'",1))
print(access_database_with_result("traffic.db","select * from users"))    

