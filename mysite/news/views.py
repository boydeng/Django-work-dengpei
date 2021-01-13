from django.shortcuts import render

# Create your views here.
from .models import Article

def year_archive(request, year):
    a_list = Article.objects.filter(pub_date__year=year)
    context = {'year': year, 'article_list': a_list}
    return render(request, 'news/year_archive.html', context)


#作业提交#
from .models import Student_dengpei



def Dengpei_yunpan_work(request,year):
    a_list = Sdudent_dengpei.objects.filter(pub_date__year=year)
    context = {'year': year, 'sdudent_dengpei_list': a_list}
    return render(request, 'templates/Dengpei_yunpan_work.html', context)