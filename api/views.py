from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from api.permissions import IsOwnerOrReadOnly, IsAuthOrBlockData, IsAdminOrOwner
from root.models import Post

from .serializers import UserSerializer, PostSerializer, UserDetailSerializer, PostDetailSerializer


class CreateUserView(CreateAPIView):
    model = get_user_model()
    permission_classes = (AllowAny,)
    serializer_class = UserDetailSerializer


class ListUserView(ListAPIView):
    queryset = get_user_model().objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer


class DetailUserView(RetrieveAPIView):
    queryset = get_user_model().objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = UserDetailSerializer


class UpdateUserView(UpdateAPIView):
    queryset = get_user_model()
    permission_classes = (IsAdminOrOwner, IsAuthenticated)
    serializer_class = UserDetailSerializer


class CreatePostView(CreateAPIView):
    queryset = Post.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = PostDetailSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ListPostView(ListAPIView):
    queryset = Post.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = PostSerializer


class DetailPostView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    permission_classes = (IsAuthOrBlockData,)


class UpdatePostView(UpdateAPIView):
    queryset = Post.objects.all()
    permission_classes = (IsOwnerOrReadOnly, IsAuthenticated)
    serializer_class = PostDetailSerializer
