from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField
from wtforms.validators import DataRequired
from csv_reader import task_id, task_name, task_type, task_id_list, task_name_list, task_type_list, full_dict_data
from flask_sqlalchemy import SQLAlchemy
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = 'entersecretkey'
if __name__ == "__main__":
    app.debug=True

app.config['ENV'] = 'development'
app.config['DEBUG'] = True
app.config['TESTING'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///eisenhowers_quadrant.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(myapp)

class AddTask(FlaskForm):
    task_name = StringField("Task Name:", validators=[DataRequired()])
    task_type = RadioField("Task Type:", choices=[("Urgent Important", "Urgent/Important"), ("Urgent Non Important", "Urgent/Non Important"), ("Non Urgent Important", "Non Urgent/Important"), ("Non Urgent/Non Important", "Non Urgent/Non Important")], validators=[DataRequired()])
    submit_task = SubmitField("Add Task")

@app.route('/', methods=["GET", "POST"])
def index():
    unknown_type = []
    urgent_important_tasks = []
    non_urgent_important_tasks = []
    urgent_non_important_tasks = []
    non_urgent_non_important_tasks = []

    for task in full_dict_data:
        if task['Urgent/Important'] == 'Urgent Important':
            urgent_important_tasks.append(task['Task'])
        elif task['Urgent/Important'] == 'Non Urgent Important':
            non_urgent_important_tasks.append(task['Task'])
        elif task['Urgent/Important'] == 'Urgent Non Important':
            urgent_non_important_tasks.append(task['Task'])
        elif task['Urgent/Important'] == 'Non Urgent Non Important':
            non_urgent_non_important_tasks.append(task['Task'])
        else:
            unknown_type.append(task)

    return render_template('index.html', urgent_important_tasks=urgent_important_tasks, non_urgent_important_tasks=non_urgent_important_tasks, urgent_non_important_tasks=urgent_non_important_tasks, non_urgent_non_important_tasks=non_urgent_non_important_tasks, unknown_type=unknown_type)

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
    task_length = len(task_id)
    return render_template('view_tasks.html', task_name_list=task_name_list, task_type_list=task_type_list, task_length=task_length)

@app.route('/delete-task')
def delete_task():
    return render_template('delete_task.html')

@app.route('/set-alarm')
def set_alarm():
    return render_template('set_alarm.html')

@app.route('/free-trial')
def free_trial():
    return render_template('free_trial.html')