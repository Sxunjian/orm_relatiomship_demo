from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

class Article(models.Model):
    title = models.CharField(max_length=100)
    comtent = models.TextField()
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
