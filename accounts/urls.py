from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    path('login/', LoginView.as_view(template_name="accounts/login.html"), name='login'),
    path('register/', views.register, name="register"),
    path('logout', views.log_out, name="logout"),
]