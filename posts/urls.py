from rest_framework import routers

from .views import PostViewSet, PostRatingViewSet

page_router = routers.SimpleRouter()
page_router.register('posts', PostViewSet, base_name='posts')
page_router.register('posts', PostRatingViewSet, base_name='post-ratings')
