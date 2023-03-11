"""test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from rest_framework import routers
from snippets.views import top
from snippets import api_views as snippet_api_views

# api router
router = routers.DefaultRouter()
# localhost:8000/api/snippets/ 以下でアクセス可能になる
router.register("snippets", snippet_api_views.SnippetViewSet)

urlpatterns = [
    path("", top, name="top"),
    path("snippets/", include("snippets.urls")),
    path("viewer/", include("viewer.urls")),
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("accounts/", include("accounts.urls")),
    path("api/", include(router.urls)),
]