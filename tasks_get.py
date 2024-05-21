from bitrix24 import Bitrix24

bx24 = Bitrix24('webhook')

# Получение id задач по проекту
print(bx24.callMethod("tasks.task.list",
    filter={'GROUP_ID': 1},
	select=['ID']))

# Получение записей в задаче по учету времени за сегодня
