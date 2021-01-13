from django.contrib import admin

from . import models

admin.site.register(models.Article)
admin.site.register(models.Reporter)
admin.site.register(models.Student_dengpei)   #分布式云盘作业

