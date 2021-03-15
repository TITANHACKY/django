from django.db import models

class blogPost(models.Model):
    title = models.TextField()
    slug = models.SlugField()
    content = models.TextField(null=True, blank=True)
