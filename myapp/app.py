from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField
from wtforms.validators import DataRequired
from python_db import task_name, task_type

app = Flask(__name__)
app.config['SECRET_KEY'] = 'entersecretkey'

class AddTask(FlaskForm):
    task_name = StringField("Task Name:", validators=[DataRequired()])
    task_type = RadioField("Task Type:", choices=[("Urgent Important", "Urgent Important"), ("Urgent Non Important", "Urgent Non Important"), ("Non Urgent Important", "Non Important Urgent"), ("Non Urgent Non Important", "Non Urgent Non Important")], validators=[DataRequired()])
    submit_task = SubmitField("Add Task")

@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html')

@app.route('/add-task', methods=["GET", "POST"])
def add_task():
    add_task_form = AddTask()
    if add_task_form.validate_on_submit():
        new_id = len(task_name) + 1
        task_name[new_id] = add_task_form.task_name.data
        task_type[new_id] = add_task_form.task_type.data
        return redirect(url_for('edit_task', _external=True, _scheme='http'))
    return render_template('add_task.html', template_form=add_task_form)

@app.route('/edit-task')
def edit_task():
    return render_template('edit_task.html', template_task_name=task_name, template_task_type=task_type)

@app.route('/delete-task')
def delete_task():
    return render_template('delete_task.html')

@app.route('/set-alarm')
def set_alarm():
    return render_template('set_alarm.html')

@app.route('/free-trial')
def free_trial():
    return render_template('free_trial.html')