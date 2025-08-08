"""
URL configuration for BookStoreRecommendation project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import include, path
from django.contrib.auth import views as auth_views

from bookstore import views

urlpatterns = [
    path('', views.Home, name="home-route"),
    path('admin/', admin.site.urls),
    path('books/', include('bookstore.urls')),

    path('register/', views.RegisterNewUser, name='register'),
    path('login/', auth_views.LoginView.as_view(
        template_name='login.html',
        redirect_authenticated_user=True,
        next_page='/',
    ), name='login'),
    path('logout/', views.logout_view, name='logout')
]
