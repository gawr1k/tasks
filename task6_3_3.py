from datetime import datetime
import time


class Quest:
    def __init__(self, name, description, goal):
        self.name = name
        self.description = description
        self.goal = goal
        self.start_time = None
        self.end_time = None

    def accept_quest(self):
        if self.end_time != None:
            return 'С этим испытанием вы уже справились.'
        self.start_time = datetime.now()
        return f'Начало {self.name} положено.'


    def pass_quest(self):
        if self.start_time == None:
            return 'Нельзя завершить то, что не имеет начала!'
        self.end_time = datetime.now()
        completion_time = self.end_time - self.start_time
        return f'Квест {self.name} окончен. Время выполнения квеста: 
{completion_time}'


quest_name = 'Сбор пиксельники'
quest_goal = 'Соберите 12 ягод пиксельники.'
quest_description = '''
В древнем лесу Кодоборье растёт ягода "пиксельника".
Она нужна для приготовления целебных снадобий.
Соберите 12 ягод пиксельники.'''

new_quest = Quest(quest_name, quest_description, quest_goal)

print(new_quest.pass_quest())
print(new_quest.accept_quest())
time.sleep(3)
print(new_quest.pass_quest())
print(new_quest.accept_quest())
