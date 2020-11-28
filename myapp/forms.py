from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField, SelectField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import DateField
import csv

uncompleted_tasks = []

with open('Eisenhower.csv', newline='') as csv_file_dict_read:
    csv_dict_reader = csv.DictReader(csv_file_dict_read)
    for task in csv_dict_reader:
        if task['Task Complete'] == 'N':
            uncompleted_tasks.append(task['Task'])

class AddTask(FlaskForm):
    task_name = StringField("Task Name:", validators=[DataRequired()])
    task_type = RadioField("Task Type:", choices=[("Urgent Important", "Urgent/Important"), ("Urgent Non Important", "Urgent/Non Important"), ("Non Urgent Important", "Non Urgent/Important"), ("Non Urgent/Non Important", "Non Urgent/Non Important")], validators=[DataRequired()])
    time_limit = DateField("Complete By:", format="%Y-%m-%d", validators=[DataRequired()])
    submit_task = SubmitField("Add Task")

class CompleteTask(FlaskForm):
    task_completed_name = SelectField("Select Completed Task", validators=[DataRequired()], choices=uncompleted_tasks)
    submit_completed_task = SubmitField("Submit")

class DeleteTask(FlaskForm):
    task_delete_name = SelectField(validators=[DataRequired()], choices=uncompleted_tasks)
    submit_deleted_task = SubmitField("Delete Task")