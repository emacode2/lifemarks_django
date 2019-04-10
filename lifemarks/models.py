from django.db import models

# Create your models here.
class Mark(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    photo_url = models.TextField()
    category = models.CharField(max_length=100, default="category")

    def __str__(self):
        return self.title
