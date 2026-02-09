from django.urls import path

from app import views

urlpatterns = [
    path('home', views.home, name="home"),
    path('task_create', views.task_create, name="task_create"),
    path('task_detail/<int:pk>', views.task_detail, name="task_detail"),
    path('task_edit/<int:pk>', views.task_edit, name="task_edit"),
    path('task_delete/<int:pk>', views.task_delete, name="task_delete"),
]