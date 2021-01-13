from django.shortcuts import render

# Create your views here.
from .models import Article

def year_archive(request, year):
    a_list = Article.objects.filter(pub_date__year=year)
    context = {'year': year, 'article_list': a_list}
    return render(request, 'news/year_archive.html', context)


#分布式云盘作业
from .models import student_dengpei, yunpan_work

from django.views.generic.edit import CreateView

class Dengpei_work(CreateView):
    model = yunpan_work
    template_name = 'dengpei_work.html'
    fields = ['headline','attach','remark', 'student_dengpei']