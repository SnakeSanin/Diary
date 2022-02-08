"""diary URL Configuration

The urls file tells Django which pages to follow
build in response to browser requests.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [  # a variable is defined in the body of the file urlpatterns
    path('admin/', admin.site.urls),  # the code includes the admin.site.urls module,
    # which defines all the URLs that can be requested from the admin site.
    path('users', include('users.urls')),
    path('', include('learning_log.urls')),
]
