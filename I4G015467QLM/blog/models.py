from django.db import models
from django.contrib.auth.models import get_user_model
user=get_user_model()

# Create your models here.

class Post(models.Model):
  title = models.CharField(max_length=200)
  text = models.TextField()
  author = models.ForeignKey(user, on_delete=models.CASCADE)
  create_date = models.DateTimeField()
  published_date = models.DateTimeField()
  
def _str_(self):
  return self.title + '|' + str(self.author)
