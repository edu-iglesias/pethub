from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.routers import DefaultRouter

from account.views import AccountView, ProfileView
from pet_finder.views import PetFinderView
from pethub.settings import API_VERSION

router = DefaultRouter()

router.register('account', AccountView, basename='account')
router.register('profile', ProfileView, basename='profile')
router.register('pet_finder', PetFinderView, basename='pet_finder')

schema_view = get_schema_view(
   openapi.Info(
      title="PetHub API",
      default_version='v1',
      description="Lorem Ipsum",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)



urlpatterns = [
   path('admin/', admin.site.urls),
   path(API_VERSION + '/', include(router.urls)),
   # url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   # url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

