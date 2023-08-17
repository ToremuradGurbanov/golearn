from django.db import models

# Create your models here.

class Unif(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(default=None)
    text = models.TextField()

    def __str__(self):
        return self.title


class Project(Unif):
    used_tech = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return super().title


class Blog(Unif):
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return super().title


class Course(Unif):   
    date = models.DateField(auto_now_add=True)
    video = models.URLField(default=None)

    def __str__(self):
        return super().title
