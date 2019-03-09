from django.urls import path
from rest_framework import routers
from apis.users.views import UserCreate, LoginView
from rest_framework_swagger.views import get_swagger_view
from rest_framework.documentation import include_docs_urls


router = routers.DefaultRouter()
schema_view = get_swagger_view(title="Demo API")

urlpatterns = [
    path("users/", UserCreate.as_view(), name="user_create"),
    path("login/", LoginView.as_view(), name="login"),
    path(
        r"docs/",
        include_docs_urls(title="Demo API", authentication_classes=[], permission_classes=[]),
    ),
    path(r"swagger-docs/", schema_view),
]

urlpatterns += router.urls
