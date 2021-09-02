from django.contrib.auth.models import User
from django.db.transaction import atomic
from drf_yasg.utils import swagger_auto_schema
from oauth2_provider.models import Application
from rest_framework import status, serializers
from rest_framework.decorators import action, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from account.models import Profile
from account.serializers import CustomRegisterSerializer, UserSerializer, ProfileSerializer, CustomLoginSerializer
from utils.token import get_tokens_via_username


class AccountView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @swagger_auto_schema(
        method='POST',
        request_body=CustomRegisterSerializer,
        responses={
            201: CustomRegisterSerializer,
        },
    )
    @atomic
    @action(methods=['POST'], detail=False, permission_classes=[], authentication_classes=[])
    def register(self, request):
        data = request.data
        user_data = data.get('user')
        serializer = CustomRegisterSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            serialized_data = serializer.data

            # rename id to profile_id
            serialized_data['profile_id'] = serialized_data['id']
            serialized_data.pop('id')

            serialized_data['tokens'] = get_tokens_via_username(user_data.get('username'))
            return Response(serialized_data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        method='POST',
        request_body=CustomLoginSerializer,
        responses={
            200: CustomRegisterSerializer,
        },
    )
    @atomic
    @action(methods=['POST'], detail=False, permission_classes=[], authentication_classes=[])
    def login(self, request):
        data = request.data
        username = data.get('username')
        serializer = CustomLoginSerializer(data=data)

        # get application
        try:
            app = Application.objects.get(
                client_id="U4rNMWqqKonkhVRMebKYp5oWyGOPI8mEhXCYvJVa",  # change to payload.get("client_id") later on
                client_secret="1jLnBW7LvxJivfon2Hyo9qBEyuCepdqwvRZzmuRmptZeBUgpjuFVe6fxLN9t90uyFhyU0bLXOB0jxdpS28FS5BYKmGOdVmwRlE6aKjeRskNkfLrS2wC8ixlhFsrkjQXM",
                # change to payload.get("client_secret") later on
            )
        except Application.DoesNotExist:
            raise serializers.ValidationError({"detail": "Invalid Application Credentials."})

        if serializer.is_valid():

            profile_instance = Profile.objects.filter(
                user__username=username
            ).select_related("user").first()

            tokens_dict = get_tokens_via_username(username)

            response_output = {
                'user': {
                    'username': profile_instance.user.username,
                    'first_name': profile_instance.user.first_name,
                    'last_name': profile_instance.user.last_name,
                },
                'tokens': tokens_dict,
                'contact_number': profile_instance.contact_number,
                'house_address': profile_instance.house_address,
                'city': profile_instance.city,
                'postal_code': profile_instance.postal_code,
                'latitude': profile_instance.latitude,
                'longitude': profile_instance.longitude,
            }

            return Response(response_output, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@permission_classes((AllowAny,))
class ProfileView(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
