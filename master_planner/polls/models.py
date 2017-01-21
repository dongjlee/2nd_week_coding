import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Planner(models.Model):
    plan_date = models.DateField('date published')
    plan_text = models.TextField()
    grade = models.IntegerField()

def __str__(self):
    return self.plan_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Review(models.Model):
    planner = models.ForeignKey(Planner)
    replan = models.CharField(max_length=200)

def __str__(self):
    return self.replan
