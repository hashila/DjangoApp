from django.db import models


class product(models.Model):
    title = models.CharField(max_length=30)
    slug = models.SlugField()
    details = models.TextField()
    prize = models.IntegerField()
    image = models.ImageField(default='default.png',blank=True)

    def __str__(self):
        return self.title

    def shortd(self):
        return self.details[:40]
