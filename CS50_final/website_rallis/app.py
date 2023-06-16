from flask import Flask, render_template, request, session, redirect, flash, jsonify # pylint: disable=unused-import

app = Flask(__name__)


@app.route("/", methods = ['POST','GET'])
def index():
    '''this will be the index route'''
    print("Index")
    return render_template("/index.html")

@app.route("/contactus", methods = ['POST','GET'])
def contactus():
    '''this will be the index route'''
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