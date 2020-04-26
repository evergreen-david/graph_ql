from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('name',)

class Comment(models.Model):
    comment = models.CharField(max_length=100)
    updated_at = models.DateField()

    def __str__(self):
        return self.comment
    
    class Meta:
        ordering = ('comment',)
