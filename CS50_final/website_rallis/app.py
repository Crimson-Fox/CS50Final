from flask import Flask, render_template, request, session, redirect, flash, jsonify # pylint: disable=unused-import

app = Flask(__name__)


@app.route("/")
def index():
    '''this will be the index route'''
    print("Index")
    return render_template("/index.html")

@app.route("/contactus")
def contactus():
    '''this will be the index route'''
    print("contact Page")
    return render_template("/contactus.html")

@app.route("/services")
def services():
    '''this will be the services route'''
    print("contact Page")
    return render_template("/services.html")

@app.route("/about")
def about():
    '''this will be the services route'''
    print("contact Page")
    return render_template("/about.html")