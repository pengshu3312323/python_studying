from django.db import models

class Topic(models.Model):
    '''learning log topics'''
    text=models.CharField(max_length=200)
    date_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        '''return the text of topic'''
        return self.text

class Entry(models.Model):
    '''in each Topics'''
    topic=models.ForeignKey(Topic)
    text=models.TextField()
    date_added=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural='entries'

    def __str__(self):
        '''return the text of Entry'''
        return self.text[:50]+'...'

