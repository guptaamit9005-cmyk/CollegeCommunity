from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    college_name = models.CharField(max_length=200)
    branch = models.CharField(max_length=100)
    year = models.IntegerField()
    is_senior = models.BooleanField(default=False)

    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username