import datetime

from django.db import models
from django.utils import timezone


class Todo(models.Model):
    todo_text = models.CharField(max_length=500)
    creation_date = models.DateTimeField('date created')

    def __str__(self):
        return self.todo_text

    def was_created_last_seven_days(self):
        return self.creation_date >= timezone.now() - datetime.timedelta(days=7)


class Priority(models.Model):
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE)
    prio = models.IntegerField(default=0)

    def __str__(self):
        return str(self.prio)
