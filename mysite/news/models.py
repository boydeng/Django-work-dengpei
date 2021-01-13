from django.db import models

class Reporter(models.Model):
    full_name = models.CharField(max_length=80)

    def __str__(self):
        return self.full_name

class Article(models.Model):
    pub_date = models.DateField()
    headline = models.CharField(max_length=200)
    content = models.TextField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline
#分布式云盘作业
from django.db import models

class student_dengpei(models.Model):
    full_name = models.CharField(max_length=80)
    class Sex(models.IntegerChoices):
        MALE = 1, '男'
        FEMALE = 0,'女'
        
        
    sex = models.GenericIPAddressField(choices=Sex.choices)

    def __setattr__(self):
        return self.full_name
class yunpan_work(models.Model):
    commit_date = models.DateField(auto_now=True)
    headline = models.CharField(max_length=200)
    attach = models.FileField()
    remark = models.TextField()
    student_dengpei = models.ForeignKey(student_dengpei, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline