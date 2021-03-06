from django.db import models

# Create your models here.
from django.db import models

class Reporter(models.Model):
    full_name = models.CharField(max_length=70)

    def __str__(self):
        return self.full_name

class Article(models.Model):
    pub_date = models.DateField()
    headline = models.CharField(max_length=200)
    content = models.TextField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline
from django.db import models

class Commit_man(models.Model):
    full_name = models.CharField(max_length=70)

    def __str__(self):
        return self.full_name

class Student_dengpei(models.Model):
    pub_date = models.DateField()
    title = models.CharField(max_length=200)
    flie_attach = models.FileField()
    content = models.TextField()
    commit_man_deng = models.ForeignKey(Reporter, on_delete=models.CASCADE)
    
    
    

    def __str__(self):
        return self.headline