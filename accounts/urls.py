from django.contrib.auth import views
from django.urls import path, include

app_name = 'accounts'
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]