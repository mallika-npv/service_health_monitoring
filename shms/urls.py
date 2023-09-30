from . import views
from django.urls import path

urlpatterns = [
    path("", views.login_view, name="login"),
    path("register", views.register, name="register"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("", views.logout_view, name="logout"),
    path('update_service_statuses/', views.update_service_statuses, name='update_service_statuses'),
]