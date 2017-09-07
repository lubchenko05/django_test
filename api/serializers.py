from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from rest_framework import serializers

from root.models import Profile, Post


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('phone', 'image', 'address')


class UserDetailSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(required=True)
    password = serializers.CharField(write_only=True, allow_blank=True)

    def create(self, validated_data):
        user = get_user_model().objects.create(
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        profile_data = validated_data.pop('profile')
        # create profile
        profile = Profile.objects.create(
            user=user,
            phone=profile_data['phone'],
            image=profile_data['image'],
            address=profile_data['address'],
        )

        user.save()
        return user

    def update(self, instance, validated_data):
        instance.set_password = validated_data['password']
        instance.save()
        profile = instance.get_profile()
        if 'image' in validated_data['profile']:
            profile.image = validated_data['profile']['image']
        profile.phone = validated_data['profile']['phone']
        profile.address = validated_data['profile']['address']
        profile.save()
        return instance

    class Meta:
        model = get_user_model()
        fields = ('email', 'password', 'profile')


class UserSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='user-detail', lookup_field='pk', read_only='True')

    class Meta:
        model = get_user_model()
        fields = ('url', 'email',)


class PostSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='post-detail', lookup_field='pk', read_only=True)

    class Meta:
        model = Post
        fields = ('url', 'title')


class PostDetailSerializer(serializers.ModelSerializer):
    owner = serializers.CharField(read_only=True)
    title = serializers.CharField(allow_blank=True)
    image = serializers.ImageField(max_length=None, required=False)
    text = serializers.CharField(allow_blank=True)

    class Meta:
        model = Post
        fields = ('owner', 'title', 'image', 'text')


class PostOpenDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'image', 'text')