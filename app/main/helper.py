from datetime import datetime
from flask import flash, session
from random import randrange
from app.models import Task, Date, Info

def saveData(date, y_tasks, t_tasks, a_info):

    #try:
        if date and y_tasks and t_tasks and a_info:
            check_date = Date.nodes.get_or_none(date=date)

            if not check_date:
                new_date = Date(date=date)
                new_date.save()
            
                y_tasks = y_tasks.split("~")
                t_tasks = t_tasks.split("~")
                a_info = a_info.split("~")

                for task in y_tasks:
                    new_task = Task(text=task)
                    new_task.save()
                    new_task.date.connect(new_date, {'isToday': False})
                    new_task.save()

                for task in t_tasks:
                    new_task = Task(text=task)
                    new_task.save()
                    new_task.date.connect(new_date, {'isToday': True})
                    new_task.save()

                for info in a_info:
                    new_info = Info(text=info)
                    new_info.save()
                    new_info.date.connect(new_date)
                    new_info.save()
            else:
                y_tasks = y_tasks.split("~")
                t_tasks = t_tasks.split("~")
                a_info = a_info.split("~")

                for task in y_tasks:
                    new_task = Task(text=task)
                    new_task.save()
                    new_task.date.connect(check_date, {'isToday': False})
                    new_task.save()

                for task in t_tasks:
                    new_task = Task(text=task)
                    new_task.save()
                    new_task.date.connect(check_date, {'isToday': True})
                    new_task.save()

                for info in a_info:
                    new_info = Info(text=info)
                    new_info.save()
                    new_info.date.connect(check_date)
                    new_info.save()
            return True
    #except:
        return False
