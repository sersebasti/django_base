from django.db import models

class Password(models.Model):
    title = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    link = models.URLField()
    note = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.title
    
    
