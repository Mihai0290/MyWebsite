from django.db import models

class Post(models.Model):
    name = models.CharField(max_length=200)
    content = models.TextField()
    author_name = models.CharField(max_length=50)
    date_published = models.DateField()

    class Meta:
        verbose_name = 'Postare'
        verbose_name_plural = 'Postari'
