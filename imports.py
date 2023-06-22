import requests
from datetime import datetime
import sqlite3

def getdryness(lat, lon):
    r = requests.get('https://api.open-meteo.com/v1/forecast?latitude=%s&longitude=%s&hourly=soil_moisture_0_1cm' % (lat, lon))
    soil_moisture_list = r.json()["hourly"]["soil_moisture_0_1cm"]
    t_time = r.json()["hourly"]["time"]

    c_time = datetime.now()
    c_hour = str(c_time.hour)
    if (int(c_hour) < 10):
        c_hour = "0" + c_hour
    current_datetime = str(c_time.date()) + "T" + c_hour + ":00" # example 2023-05-27T23:00

    match = t_time.index(current_datetime)

    soil_moisture = soil_moisture_list[match]
    return soil_moisture
def setupdb(dbname):
    con = sqlite3.connect(dbname)
    cur = con.cursor()
    return cur, con

def adddb(name, locaition, cur, con):
    cur.execute("INSERT INTO skatepark VALUES (%s, %s)" % (name, locaition))
    con.commit()

def getdb(cur, type):
    res = cur.execute("SELECT %s FROM skatepark" % type)
    return res.fetchall()
