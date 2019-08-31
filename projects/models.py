from django.db import models

#TODO setup aws s3 bucket for images

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.FilePathField(path="/img")
