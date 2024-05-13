from django.db import models

class Task(models.Model):
    
    title = models.CharField(max_length=200, blank=True, null=True)
    completed = models.BooleanField(default=False, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
