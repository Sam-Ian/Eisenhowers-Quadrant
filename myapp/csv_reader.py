import csv

task_id = {}
task_name = {}
task_type = {}
full_dict_data = []
task_id_list = []
task_name_list = []
task_type_list = []

with open('Eisenhower.csv') as csv_file_dict_read:
    csv_dict_reader = csv.DictReader(csv_file_dict_read)
    for task in csv_dict_reader:
        task_id[task['Task ID']] = (task['Task ID'])
        task_name[task['Task ID']] = (task['Task'])
        task_type[task['Task ID']] = (task['Urgent/Important'])
        full_dict_data.append(task)
        
with open('Eisenhower.csv') as csv_file_read:
    csv_reader = csv.reader(csv_file_read)
    next(csv_reader)
    for task in csv_reader:
        task_id_list.append(task[0])
        task_name_list.append(task[1])
        task_type_list.append(task[2])

