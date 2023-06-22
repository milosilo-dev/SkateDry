from flask import *
from imports import *

app = Flask(__name__)
@app.route("/")
def index():
    cur, com = setupdb("main.db")
    dbnames = getdb(cur, "name, locaition")
    return render_template("index.html", names=dbnames)

@app.route("/add/")
def add():
    return render_template("Addform.html")

@app.route("/add/result/")
def addresult():
    cur, com = setupdb("main.db")
    print(request.args['name'])
    adddb("'%s'" % request.args['name'], "'(%s, %s)'" % (request.args['latitude'], request.args['longitude']), cur, com)
    return redirect("/")

@app.route('/locaition/<latitude>,<longitude>')
def hello(latitude, longitude):
    drynesscalc = getdryness(latitude, longitude)

    dryoncalc = "Dry🌵🏜️"
    if (drynesscalc >= 0.33):
        dryoncalc = "Wet💦💧"
    return render_template("Locaition.html", locaition="(%s, %s)" % (latitude, longitude), dryness=drynesscalc, dryon=dryoncalc)