from flask import Flask, render_template, request, session, redirect, flash, jsonify # pylint: disable=unused-import
import sqlite3

app = Flask(__name__)

con = sqlite3.connect("enquiries.db", check_same_thread=False)
cur = con.cursor()

@app.route("/", methods = ['POST','GET'])
def index():
    if request.method == 'POST':
        fname = request.form.get("fname")
        lname = request.form.get("lname")
        email = request.form.get("email")
        details = request.form.get("details")
        if not fname:
           return render_template("/index.html")
        if not lname:
            return render_template("/index.html")
        if not email:
            return render_template("/index.html")
        if not details:
            return render_template("/index.html")
        print("POST")
        cur.execute("INSERT INTO enquiries VALUES(?,?,?,?)",[ fname, lname, email, details])
        con.commit()
        return render_template("/index.html")
    '''this will be the index route'''
    print("GET")
    return render_template("/index.html")

@app.route("/contactus", methods = ['POST','GET'])
def contactus():
    if request.method == 'POST':
        fname = request.form.get("fname")
        lname = request.form.get("lname")
        email = request.form.get("email")
        details = request.form.get("details")
        if not fname:
            return render_template("/index.html")
        if not lname:
            return render_template("/index.html")
        if not email:
            return render_template("/index.html")
        if not details:
            return render_template("/index.html")
        print("POST")
        cur.execute("INSERT INTO enquiries VALUES(?,?,?,?)",[ fname, lname, email, details])
        con.commit()
        return render_template("/index.html")
    print("contact Page")
    return render_template("/contactus.html")

@app.route("/services")
def services():
    '''this will be the services route'''
    print("services Page")
    return render_template("/services.html")

@app.route("/about")
def about():
    '''this will be the services route'''
    print("about Page")
    return render_template("/about.html")

@app.route("/timber")
def timber():
    '''this will be the timber route'''
    print("timber Page")
    return render_template("/timber.html")

@app.route("/suppliers")
def suppliers():
    '''this will be the suploers route'''
    print("suppliers Page")
    return render_template("/suppliers.html")

@app.route("/hardware")
def hardware():
    '''this will be the suploers route'''
    print("hardware Page")
    return render_template("/hardware.html")

@app.route("/sheets")
def sheets():
    '''this will be the suploers route'''
    print("sheets Page")
    return render_template("/sheets.html")

@app.route("/doors")
def doors():
    '''this will be the suploers route'''
    print("sheets Page")
    return render_template("/doors.html")

@app.route("/specialties")
def specialties():
    '''this will be the suploers route'''
    print("specialtiesPage")
    return render_template("/specialties.html")

@app.route("/treated-pine-lvl")
def treatedpinelvl():
    '''this will be the suploers route'''
    print("specialtiesPage")
    return render_template("/treated-pine-lvl.html")