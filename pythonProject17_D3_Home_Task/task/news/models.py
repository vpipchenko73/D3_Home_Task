from django.db import models

# Create your models here.

class Post(models.Model):
    dateCreation = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=128)
    text = models.TextField()
    rating = models.SmallIntegerField(default=0)

    #class Meta:
     #   ordering=['-dateCreation']

    def __str__(self):
        return f"{self.title[0:16]} / {self.text[0:128]}{'...'} Рейтинг- {str(self.rating)}"
