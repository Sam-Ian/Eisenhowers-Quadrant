from forms import AddTask, CompleteTask, DeleteTask
from flask import Flask, render_template, request, redirect, url_for
import csv
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'entersecretkey'



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
        if task['Urgent/Important'] == 'Urgent Important' and task['Task Complete'] == 'N':
            urgent_important_tasks.append(task['Task'])
        elif task['Urgent/Important'] == 'Non Urgent Important' and task['Task Complete'] == 'N':
            non_urgent_important_tasks.append(task['Task'])
        elif task['Urgent/Important'] == 'Urgent Non Important' and task['Task Complete'] == 'N':
            urgent_non_important_tasks.append(task['Task'])
        elif task['Urgent/Important'] == 'Non Urgent Non Important' and task['Task Complete'] == 'N':
            non_urgent_non_important_tasks.append(task['Task'])
        else:
            unknown_type.append(task)

    complete_task_form = CompleteTask()
    if complete_task_form.validate_on_submit():
    
        completed_task = complete_task_form.task_completed_name.data

        for row in full_dict_data:
            if row['Task'] == completed_task:
                row['Task Complete'] = 'Y'     

        with open('Eisenhower.csv', 'w', newline='', encoding='utf-8') as csv_file_write:
            csv_writer = csv.DictWriter(csv_file_write, fieldnames=('Task ID', 'Task', 'Urgent/Important', 'Task Complete', 'Date Added', 'Date Completed'))
            csv_writer.writeheader()
            csv_writer.writerows(full_dict_data)

        return redirect(url_for('index', _external=True, _scheme='http'))
    return render_template('index.html', urgent_important_tasks=urgent_important_tasks, non_urgent_important_tasks=non_urgent_important_tasks, urgent_non_important_tasks=urgent_non_important_tasks, non_urgent_non_important_tasks=non_urgent_non_important_tasks, unknown_type=unknown_type, complete_task_form=complete_task_form)



@app.route('/add-task', methods=["GET", "POST"])
def add_task():
    add_task_form = AddTask()
    if add_task_form.validate_on_submit():

        task_name = {}
        task_type = {}
        time_limit = {}

        with open('Eisenhower.csv', newline='') as csv_file_dict_read:
            csv_dict_reader = csv.DictReader(csv_file_dict_read)
            for task in csv_dict_reader:
                task_name[task['Task ID']] = (task['Task'])
                task_type[task['Task ID']] = (task['Urgent/Important'])
                time_limit[task['Task ID']] = (task['Time Limit'])

        new_id = len(task_name) + 1
        task_name[new_id] = add_task_form.task_name.data
        task_type[new_id] = add_task_form.task_type.data
        time_limit[new_id] = add_task_form.time_limit.data


        with open('Eisenhower.csv', 'a', newline='', encoding='utf-8') as csv_file_write:
            fields=['Task ID', 'Task', 'Urgent/Important', 'Task Complete', 'Date Added', 'Date Completed', 'Time Limit']
            csv_writer = csv.DictWriter(csv_file_write, fieldnames=fields)
            csv_writer.writerow({'Task ID': new_id, 'Task': task_name[new_id], 'Urgent/Important': task_type[new_id], 'Task Complete': 'N', 'Date Added': datetime.today().strftime('%d/%m/%Y'), 'Date Completed': 'Null', 'Time Limit': time_limit[new_id]})

        return redirect(url_for('index', _external=True, _scheme='http'))
    return render_template('add_task.html', template_form=add_task_form)



@app.route('/view-tasks', methods=["GET", "POST"])
def view_tasks():

    task_id_list = []
    task_name_list = []
    task_type_list = []
    task_complete_list = []
    task_added_list = []

    with open('Eisenhower.csv', newline='') as csv_file_read:
        csv_reader = csv.reader(csv_file_read)
        next(csv_reader)

        for task in csv_reader:
            if task[3] == 'N':
                task_id_list.append(task[0])
                task_name_list.append(task[1])
                task_type_list.append(task[2])
                task_complete_list.append(task[3])
                task_added_list.append(task[4])

    task_length = len(task_id_list)

    full_dict_data = []

    with open('Eisenhower.csv', newline='') as csv_file_dict_read:
        csv_dict_reader = csv.DictReader(csv_file_dict_read)
        for task in csv_dict_reader:
            full_dict_data.append(task)

    delete_task_form = DeleteTask()
    if delete_task_form.validate_on_submit():
        deleted_task = delete_task_form.task_delete_name.data

        for i in range(len(full_dict_data)):
            if full_dict_data[i]['Task'] == deleted_task:
                del full_dict_data[i]
                break

        with open('Eisenhower.csv', 'w', newline='', encoding='utf-8') as csv_file_write:
            csv_writer = csv.DictWriter(csv_file_write, fieldnames=('Task ID', 'Task', 'Urgent/Important', 'Task Complete', 'Date Added', 'Date Completed'))
            csv_writer.writeheader()
            csv_writer.writerows(full_dict_data)
        return redirect(url_for('view_tasks', _external=True, _scheme='http')) 
    return render_template('view_tasks.html', task_name_list=task_name_list, task_type_list=task_type_list, task_complete_list=task_complete_list, task_added_list=task_added_list, task_length=task_length, delete_task_form=delete_task_form)



@app.route('/completed-tasks')
def completed_tasks():

    completed_task_id = []
    completed_task_name = []
    completed_task_type = []
    completed_task_added = []
    completed_task_completed = []

    with open('Eisenhower.csv', newline='') as csv_file_read:
        csv_reader = csv.reader(csv_file_read)
        next(csv_reader)

        for task in csv_reader:
            if task[3] == 'Y':
                completed_task_id.append(task[0])
                completed_task_name.append(task[1])
                completed_task_type.append(task[2])
                completed_task_added.append(task[4])
                completed_task_completed.append(task[5])
                
    task_length = len(completed_task_id)

    return render_template('completed_tasks.html', completed_task_id=completed_task_id, completed_task_name=completed_task_name, completed_task_type=completed_task_type, completed_task_added=completed_task_added, completed_task_completed=completed_task_completed, task_length=task_length)



@app.route('/set-alarm')
def set_alarm():
    return render_template('set_alarm.html')



@app.route('/free-trial')
def free_trial():
    return render_template('free_trial.html')