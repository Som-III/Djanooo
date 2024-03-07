from django.db import models

# Create your models here.
class Question(models.Model):
    que_txt = models.CharField(max_length=500)
    pub_date = models.DateTimeField("date published")
    
    def __str__(self):
        return self.que_txt
    
    
class Choice(models.Model):
    que = models.ForeignKey(Question,on_delete=models.CASCADE)
    choicetxt = models.CharField(max_length=400)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choicetxt