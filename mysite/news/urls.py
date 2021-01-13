from django.urls import path

from . import views

urlpatterns = [
    
    path('articles/<int:year>/', views.year_archive),
    path('dengpei_yunpan/',views.Dengpei_yunpan_work)
    #path('articles/<int:year>/<int:month>/', views.month_archive),
    #path('articles/<int:year>/<int:month>/<int:pk>/', views.article_detail),
]