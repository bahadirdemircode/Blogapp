from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("index", views.index),
    path('homework/create/', views.homework_create, name='homework_create'),
    path('homework/list/', views.homework_list, name='homework_list'),
    path('homework/<int:id>/edit/', views.homework_edit, name='homework_edit'),
    path('homework/<int:id>/delete/', views.homework_delete, name='homework_delete'),
    path('homework/<int:id>/', views.homework_detail, name='homework_detail'),
    path("blogs", views.blogs, name="blogs"),
    path("category/<slug:slug>", views.blogs_by_category, name="blogs_by_category"),
    path("blogs/<slug:slug>", views.blog_details, name="blog_details"),
]
