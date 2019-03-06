from apis.users.views import UserViewSet
from rest_framework import routers, serializers, viewsets

router = routers.DefaultRouter()
router.register(r"users", UserViewSet)

