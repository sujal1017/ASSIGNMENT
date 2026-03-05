from django.db import models

class Student(models.Model):

    name = models.CharField(max_length=100)
    usn = models.CharField(max_length=20)
    sem = models.IntegerField()
    branch = models.CharField(max_length=50)

    def __str__(self):
        return self.name