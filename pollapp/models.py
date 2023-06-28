from django.db import models
from django.utils import timezone
import datetime
# Create your models here.
class Questions(models.Model):
    question_text=models.CharField(max_length=300)
    publish_date=models.DateTimeField('Date Published')
    def __str__(self):
        return self.question_text
    def published_recently(self):
        return timezone.now() >= self.publish_date >=timezone.now() - datetime.timedelta(days=1)

class Choices(models.Model):
    question=models.ForeignKey(Questions,on_delete=models.CASCADE)
    choice_text=models.CharField(max_length=200)
    vote_num=models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
   