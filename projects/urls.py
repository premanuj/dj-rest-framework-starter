"""projects URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.documentation import include_docs_urls
from .routes import router

# router = routers.DefaultRouter()
# router.register(r"users", UserViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),
    url(r"^", include(router.urls)),
    # url(r"^api/token/", obtain_auth_token, name="api-token"),
    url(r"^docs/", include_docs_urls(title="Demo apis", public=False)),
    # url(r"^api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
