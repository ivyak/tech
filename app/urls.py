from django.urls import path

from app import views

urlpatterns = [
    path('home', views.home, name="home"),
    path('task_create', views.task_create, name="task_create"),
    path('task_detail/<int:pk>', views.task_detail, name="task_detail"),
    path('task_edit/<int:pk>', views.task_edit, name="task_edit"),
    path('task_delete/<int:pk>', views.task_delete, name="task_delete"),
    path('signup', views.signup, name="signup"),
    path('login', views.CustomLoginView.as_view(), name="login"),
    path('logout', views.CustomLogoutView.as_view(), name="logout"),
]