from django.urls import path
from . import views

urlpatterns = [
path('', views.teacher_list),
path('add/', views.teacher_add),
path('edit/<int:id>/', views.teacher_edit),
path('delete/<int:id>/', views.teacher_delete),
]