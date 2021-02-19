from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ToDo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    task = models.CharField(max_length=100)
    is_done = models.BooleanField(default=False)
    time_stamp = models.DateTimeField(auto_now_add = True)

    class Meta():
        ordering = ('time_stamp',)

    def __str__(self):
        return self.task