from oauth2_provider.models import Application
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed

from account.models import Profile
from utils.token import generate_tokens


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        max_length=65,
        min_length=8,
        write_only=True,
        required=True
    )

    first_name = serializers.CharField(max_length=255, min_length=1, required=True)
    last_name = serializers.CharField(max_length=255, min_length=1, required=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'password']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ['contact_number', 'house_address', 'city', 'postal_code', 'latitude', 'longitude', 'preference_tag']


class CustomRegisterSerializer(serializers.ModelSerializer):

    user = UserSerializer()

    class Meta:
        model = Profile
        fields = ['id', 'user', 'contact_number', 'house_address', 'city', 'postal_code', 'latitude', 'longitude', 'preference_tag']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user_instance = user_serializer.save()

            # create tokens
            try:
                app = Application.objects.get(
                    client_id="U4rNMWqqKonkhVRMebKYp5oWyGOPI8mEhXCYvJVa",
                    client_secret="1jLnBW7LvxJivfon2Hyo9qBEyuCepdqwvRZzmuRmptZeBUgpjuFVe6fxLN9t90uyFhyU0bLXOB0jxdpS28FS5BYKmGOdVmwRlE6aKjeRskNkfLrS2wC8ixlhFsrkjQXM",
                )

                generate_tokens(app, user_instance)
            except Application.DoesNotExist:
                raise serializers.ValidationError({"detail": "Invalid Application Credentials."})

            return Profile.objects.create(user=user_instance, **validated_data)

        else:
            raise serializers.ValidationError(user_serializer.errors)


class CustomLoginSerializer(serializers.Serializer):

    password = serializers.CharField( max_length=65, min_length=8, write_only=True)
    username = serializers.CharField(max_length=255, min_length=2)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')
        user_instance = authenticate(username=username, password=password)

        if user_instance:

            # create tokens
            try:
                app = Application.objects.get(
                    client_id="U4rNMWqqKonkhVRMebKYp5oWyGOPI8mEhXCYvJVa",  # change to payload.get("client_id") later on
                    client_secret="1jLnBW7LvxJivfon2Hyo9qBEyuCepdqwvRZzmuRmptZeBUgpjuFVe6fxLN9t90uyFhyU0bLXOB0jxdpS28FS5BYKmGOdVmwRlE6aKjeRskNkfLrS2wC8ixlhFsrkjQXM",
                    # change to payload.get("client_secret") later on
                )

                generate_tokens(app, user_instance)
            except Application.DoesNotExist:
                raise serializers.ValidationError({"detail": "Invalid Application Credentials."})

            return data

        raise AuthenticationFailed()

    class Meta:
        fields = ['username', 'password']



