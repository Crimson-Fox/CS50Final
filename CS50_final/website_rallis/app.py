from flask import Flask, render_template, request, session, redirect, flash, jsonify # pylint: disable=unused-import

app = Flask(__name__)


@app.route("/")
def hello_world():
    '''this will be the index route'''
    print("test")
    return render_template("index.html")
