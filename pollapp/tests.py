from django.test import TestCase
from django.utils import timezone
from .models import Questions
import datetime
# Create your tests here.

class QuestionTest(TestCase):
    def testing_if_pub_date_recent(self):
        """To return false for any future publish date"""
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Questions(publish_date = time)
        self.assertIs(future_question.published_recently(),False)
        
    def testing_recent_with_new_question(self):
        """To"""
        time=timezone.now()- datetime.timedelta(hours=23,minutes=59,seconds=59)
        new_day=Questions(publish_date=time)
        self.assertIs(new_day.published_recently(),True)
    
    def testing_recent_with_old_question(self):
        """"""
        time=timezone.now() - datetime.timedelta(days=1,seconds=1)
        old_day=Questions(publish_date = time)
        self.assertIs(old_day.published_recently(),False)