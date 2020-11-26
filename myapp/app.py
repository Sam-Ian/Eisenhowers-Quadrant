from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField
from wtforms.validators import DataRequired
from csv_read_write import task_name, task_type
from flask_sqlalchemy import SQLAlchemy
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = 'entersecretkey'
if __name__ == "__main__":
    app.debug=True

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///eisenhowers_quadrant.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(myapp)

class AddTask(FlaskForm):
    task_name = StringField("Task Name:", validators=[DataRequired()])
    task_type = RadioField("Task Type:", choices=[("Urgent Important", "Urgent/Important"), ("Urgent Non Important", "Urgent/Non Important"), ("Non Urgent Important", "Non Urgent/Important"), ("Non Urgent/Non Important", "Non Urgent/Non Important")], validators=[DataRequired()])
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

        with open('Eisenhower.csv', 'a', newline='', encoding='utf-8') as csv_file_write:
            fields=['Task ID', 'Task', 'Urgent/Important']
            csv_writer = csv.DictWriter(csv_file_write, fieldnames=fields)
            csv_writer.writerow({'Task ID': new_id, 'Task': task_name[new_id], 'Urgent/Important': task_type[new_id]})

        return redirect(url_for('view_tasks', _external=True, _scheme='http'))
    return render_template('add_task.html', template_form=add_task_form)

@app.route('/view-tasks')
def view_tasks():
    return render_template('view_tasks.html', template_task_name=task_name, template_task_type=task_type)

@app.route('/delete-task')
def delete_task():
    return render_template('delete_task.html')

@app.route('/set-alarm')
def set_alarm():
    return render_template('set_alarm.html')

@app.route('/free-trial')
def free_trial():
    return render_template('free_trial.html')