from __future__ import unicode_literals
from django.db import models

class question(models.Model) :
    ques_id = models.IntegerField()
    statement = models.CharField(max_length=500)
    op1 = models.CharField(max_length=300)
    op2 = models.CharField(max_length=300)
    op3 = models.CharField(max_length=300)
    op4 = models.CharField(max_length=300)

    def __str__(self):
        return str(self.ques_id)

class user(models.Model) :
    username = models.CharField(max_length=200)
    user_id = models.IntegerField()
    quest = models.ForeignKey(question, on_delete=models.CASCADE, related_name='questionKey')

    def __str__(self):
        return self.username


