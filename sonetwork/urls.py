from django.conf.urls import include, url
from django.contrib import admin

from rest_framework_jwt.views import obtain_jwt_token

from users.urls import router as users_router

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', obtain_jwt_token),

    url(r'^api/', include(users_router.urls))
]
