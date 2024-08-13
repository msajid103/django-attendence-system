from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=20)
    roll_no = models.CharField(primary_key=True, max_length=20)
    password = models.CharField(max_length=20)
    allow_status = models.BooleanField(default=True)

    def __str__(self):
        return self.roll_no
class Time_table(models.Model):
    student = models.ForeignKey(Student, on_delete= models.CASCADE)
    entry_time = models.DateTimeField()
    exit_time = models.DateTimeField(null=True)
