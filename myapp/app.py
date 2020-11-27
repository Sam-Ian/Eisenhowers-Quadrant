from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField
from wtforms.validators import DataRequired
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = 'entersecretkey'
if __name__ == "__main__":
    app.debug=True

class AddTask(FlaskForm):
    task_name = StringField("Task Name:", validators=[DataRequired()])
    task_type = RadioField("Task Type:", choices=[("Urgent Important", "Urgent/Important"), ("Urgent Non Important", "Urgent/Non Important"), ("Non Urgent Important", "Non Urgent/Important"), ("Non Urgent/Non Important", "Non Urgent/Non Important")], validators=[DataRequired()])
    submit_task = SubmitField("Add Task")



@app.route('/', methods=["GET", "POST"])
def index():

    full_dict_data = []

    with open('Eisenhower.csv', newline='') as csv_file_dict_read:
        csv_dict_reader = csv.DictReader(csv_file_dict_read)
        for task in csv_dict_reader:
            full_dict_data.append(task)

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

        task_name = {}
        task_type = {}
    
        with open('Eisenhower.csv', newline='') as csv_file_dict_read:
            csv_dict_reader = csv.DictReader(csv_file_dict_read)
            for task in csv_dict_reader:
                task_name[task['Task ID']] = (task['Task'])
                task_type[task['Task ID']] = (task['Urgent/Important'])

        new_id = len(task_name) + 1
        task_name[new_id] = add_task_form.task_name.data
        task_type[new_id] = add_task_form.task_type.data

        with open('Eisenhower.csv', 'a', newline='', encoding='utf-8') as csv_file_write:
            fields=['Task ID', 'Task', 'Urgent/Important']
            csv_writer = csv.DictWriter(csv_file_write, fieldnames=fields)
            csv_writer.writerow({'Task ID': new_id, 'Task': task_name[new_id], 'Urgent/Important': task_type[new_id]})

        return redirect(url_for('index', _external=True, _scheme='http'))
    return render_template('add_task.html', template_form=add_task_form)



@app.route('/view-tasks')
def view_tasks():

    task_id_list = []
    task_name_list = []
    task_type_list = []
            
    with open('Eisenhower.csv', newline='') as csv_file_read:
        csv_reader = csv.reader(csv_file_read)
        next(csv_reader)

        for task in csv_reader:
            if task:
                task_id_list.append(task[0])
                task_name_list.append(task[1])
                task_type_list.append(task[2])

    task_length = len(task_id_list)
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