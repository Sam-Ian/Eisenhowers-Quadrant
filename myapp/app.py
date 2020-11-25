from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'entersecretkey'

@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html')

@app.route('/add-task', methods=["GET", "POST"])
def add_task():
    return render_template('add_task.html')
