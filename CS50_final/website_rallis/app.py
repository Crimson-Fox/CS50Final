from flask import Flask, render_template, request, session, redirect, flash, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    print("test")
    return render_template("index.html")