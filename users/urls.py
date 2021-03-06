from django.urls import path, include
from . import views
app_name = 'users'
urlpatterns = [
    path('', include('django.contrib.auth.urls')),  # Enable default authorization URL.
    path('register/', views.register, name='register'),  # Registration page.
]