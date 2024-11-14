from django.urls import path

from quiz import views

urlpatterns = [
    path('', views.quiz_view, name='quiz'),
    path('about/', views.about, name='about'),
]