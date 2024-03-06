from django.db import models



class Board(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()