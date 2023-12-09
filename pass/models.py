from django.db import models


class Password(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    username = models.CharField(max_length=255, null=True, blank=True)
    password = models.CharField(max_length=255, null=True, blank=True)
    code = models.CharField(max_length=255, null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    note = models.CharField(max_length=255,null=True, blank=True)
    
    def __str__(self) -> str:
        return self.title
    
    
