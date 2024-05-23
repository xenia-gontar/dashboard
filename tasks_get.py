from bitrix24 import Bitrix24


bx24 = Bitrix24('webhook')



# Получение id задач по проекту

response = bx24.callMethod("tasks.task.list",
    filter={'GROUP_ID': 1},
	select=['ID'])

print(response)
print(response["tasks"])

# Достали все id задач

tasks_id = []

for element in response["tasks"]:
	tasks_id.append(element["id"])

print(tasks_id)	
