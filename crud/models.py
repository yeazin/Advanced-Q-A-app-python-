from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Todouser(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING, related_name='todo_user')
    email = models.EmailField(blank=True)
    username = models.CharField(blank=False, max_length=200)

    def __str__(self):
        return f"{self.username} | {self.user}"


class ToDo(models.Model):
    list_name   = models.CharField(max_length=300, blank=False, null=True, verbose_name='List Name')
    finish_yet  = models.BooleanField(default=False)

    def __str__(self):
        return self.list_name

    class Meta:
        verbose_name = " To Do List"
        verbose_name_plural = 'To Do List'
    