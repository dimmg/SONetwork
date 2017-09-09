from rest_framework import routers

from .views import UserViewSet

router = routers.SimpleRouter()
router.register('users', UserViewSet, base_name='users')
