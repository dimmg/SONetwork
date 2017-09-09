from django.conf.urls import include, url
from django.contrib import admin

from rest_framework_jwt.views import obtain_jwt_token

from posts.urls import page_router as posts_router
from users.urls import router as users_router

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', obtain_jwt_token),

    url(r'^api/', include(users_router.urls)),
    url(r'^api/', include(posts_router.urls)),
]
