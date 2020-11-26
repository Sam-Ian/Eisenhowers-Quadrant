import csv
import app

task_name = {}
task_type = {}

with open('Eisenhower.csv') as csv_file_read:
    csv_reader = csv.DictReader(csv_file_read)
    for task in csv_reader:
        task_name[task['Task ID']] = (task['Task'])
        task_type[task['Task ID']] = (task['Urgent/Important'])

# with open('Eisenhower_test.csv') as csv_file_write:
#     fields = ['Task ID', 'Task', 'Urgent/Important']
#     csv_writer = csv.DictWriter(csv_file_write, fieldnames=fields)

#     csv_writer.writeheader()

#     # for id, name in task_name.items():
#     #     csv_writer.writerow(name)
#     # for id, t_type in task_type.items():
#     #     csv_writer.writerow(t_type)


