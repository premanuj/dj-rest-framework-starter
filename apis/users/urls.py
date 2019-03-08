from .views import UserViewSet, UserRegistration
from django.urls import path

from rest_framework import routers
from apis.users.views import UserViewSet
from rest_framework.documentation import include_docs_urls
from rest_framework_swagger.views import get_swagger_view


router = routers.DefaultRouter()
router.register("users", UserViewSet, base_name="users")

schema_view = get_swagger_view(title="Demo API")

urlpatterns = [
    path("users/", UserRegistration.as_view(), name="user_create"),
    path(r"docs/", include_docs_urls(title="Demo API")),
    path(r"swagger-docs/", schema_view),
]

urlpatterns += router.urls
