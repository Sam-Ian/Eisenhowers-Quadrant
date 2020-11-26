import csv

task_name = {}
task_type = {}

with open('Eisenhower.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for task in csv_reader:
        task_name[task['Task ID']] = (task['Task'])
        task_type[task['Task ID']] = (task['Urgent/Important'])

print(task_name)
print(task_type)
