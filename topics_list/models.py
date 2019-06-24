from django.db import models

# Create your models here.


class TopicsList(models.Model):
    topic_no = models.IntegerField()
    title = models.CharField(max_length=120)

    def __str__(self):
        return  '{} - {}'.format(self.topic_no, self.title)
