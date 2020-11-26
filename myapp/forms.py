from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField


class AddTask(FlaskForm):
    task_name = StringField("Task Name:")
    task_type = RadioField("Task Type:")
    submit_task = SubmitField("Add Task")
