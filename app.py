from flask import Flask, render_template, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/')
def home():
    return 204