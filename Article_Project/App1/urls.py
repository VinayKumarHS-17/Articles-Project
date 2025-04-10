from django.contrib import admin
from django.urls import path
from .import views


urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name='about'),
    path('events/', views.events, name='events'),
    path('article/', views.article, name='article'),
    
    path('construction/',views.construction,name='construction'),
    # path('page/<int:id>', views.page, name='page'),
]