from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class InputData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    input_values = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.user.username} - {self.timetamp}"
