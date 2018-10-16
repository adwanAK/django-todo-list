from django.db import models
import datetime

# Create your models here.

class TodoList(models.Model):
    title = models.CharField(max_length=100)
    completed = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class TodoItem(models.Model):
    todolist = models.ForeignKey(TodoList, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    date_created= models.DateTimeField('created on')
    due_date = models.DateTimeField('date due')


    def __str__(self):
        return self.name
