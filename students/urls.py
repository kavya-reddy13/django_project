from django.urls import path
from . import views

urlpatterns = [
path('', views.student_list),
path('add/', views.student_add),
path('edit/<int:id>/', views.student_edit),
path('delete/<int:id>/', views.student_delete),
]