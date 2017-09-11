from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Post, PostRating
from .permissions import IsOwnerOnNonSafeMethods
from .serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    """
    Posts management ModelViewSet.
    """
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = (IsAuthenticated, IsOwnerOnNonSafeMethods,)

    def list(self, request, *args, **kwargs):
        posts = Post.objects.filter(author=request.query_params.get('author'))
        serializer = PostSerializer(posts, many=True)

        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        request.data['author'] = request.user.id

        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        request.data['author'] = request.user.id

        return super().update(request, *args, **kwargs)


class PostRatingViewSet(viewsets.ViewSet):
    """
    PostRating ViewSet.
    Allows to like / dislike a specific Post. 
    """

    @detail_route(methods=['post'])
    def like(self, request, pk=None):
        post = get_object_or_404(Post, pk=pk)

        exists, post_rating = self._get_or_prepare(post, request.user)
        if not exists or post_rating is False:
            post_rating.positive = True
            post_rating.save()

        serializer = PostSerializer(post)

        return Response(serializer.data)

    @detail_route(methods=['post'])
    def dislike(self, request, pk=None):
        post = get_object_or_404(Post, pk=pk)

        exists, post_rating = self._get_or_prepare(post, request.user)
        if not exists or post_rating.positive is True:
            post_rating.positive = False
            post_rating.save()

        serializer = PostSerializer(post)

        return Response(serializer.data)

    def _get_or_prepare(self, post, user):
        """
        Returns a PostRating object with the provided details if exists,
        otherwise an instance of PostRating object.
        :param post: Post object instance
        :param user: User object instance
        :return: PostRating object
        """
        try:
            exists, post_rating = True, PostRating.objects.get(post=post, user=user)
        except PostRating.DoesNotExist:
            exists, post_rating = False, PostRating(post=post, user=user)

        return exists, post_rating
