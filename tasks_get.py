from bitrix24 import Bitrix24


bx24 = Bitrix24('webhook')



# Получение id задач по проекту

response = bx24.callMethod("tasks.task.list",
    filter={'GROUP_ID': 1},
	select=['ID'])


# Достали все id задач

tasks_id = []

for element in response["tasks"]:
	tasks_id.append(element["id"])

print(tasks_id)	

task_records = bx24.callMethod('tasks.task.history.list', 
	taskId = 3, 
	filter={'field': 'time_spent_in_logs'}, 
	select =['name', 'lastName', 'createdDate', 'value'])["list"]



for task_record in task_records:
	print(task_record["user"]["name"], ' ',task_record["user"]["lastName"], " ", task_record["createdDate"], task_record["value"]["to"]   )
	print("\n")

result = bx24.callMethod('task.elapseditem.getlist', order = {"USER_ID": "desc"}, filter = {"USER_ID" : 1, ">CREATED_DATE": '2024-05-28'})

print(result)


