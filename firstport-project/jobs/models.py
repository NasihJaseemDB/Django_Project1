from django.db import models

# Create your models here.
class Job(models.Model):

    #Image
    image = models.ImageField(upload_to='images/')    #imagefield that accepts image formats
    #Summary
    summary = models.CharField(max_length=200)
    #descriptions
    description = models.TextField(max_length=1000)

    
    def __str__(self):
        return self.summary