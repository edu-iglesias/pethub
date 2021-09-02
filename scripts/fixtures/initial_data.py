import sys
import os
import django
import time

sys.path.append("../pethub")
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pethub.settings')
django.setup()

CLIENT_CONFIDENTIAL = "confidential"
CLIENT_PUBLIC = "public"
GRANT_AUTHORIZATION_CODE = "authorization-code"
GRANT_IMPLICIT = "implicit"
GRANT_PASSWORD = "password"
GRANT_CLIENT_CREDENTIALS = "client-credentials"

def create():

    expires = now() + timedelta(seconds=OAUTH2_PROVIDER["ACCESS_TOKEN_EXPIRE_SECONDS"])
    scope = OAUTH2_PROVIDER["SCOPES"]

    """
    Model: Users
    """

    user_instance, is_created = User.objects.get_or_create(
        username='admin@test.com',
        email='admind@test.com',
    )

    user_instance.set_password('p@ssw0rD')
    user_instance.first_name = 'Jisoo'
    user_instance.last_name = 'Kim'
    user_instance.is_staff = True
    user_instance.is_active = True
    user_instance.is_superuser = True
    user_instance.save()

    """
    Model: Application
    """

    application_instance, is_created = Application.objects.get_or_create(
        client_id='U4rNMWqqKonkhVRMebKYp5oWyGOPI8mEhXCYvJVa',
        user=user_instance,
        redirect_uris='http://localhost:8000/',
        client_type=CLIENT_CONFIDENTIAL,
        authorization_grant_type=GRANT_IMPLICIT,
        client_secret='1jLnBW7LvxJivfon2Hyo9qBEyuCepdqwvRZzmuRmptZeBUgpjuFVe6fxLN9t90uyFhyU0bLXOB0jxdpS28FS5BYKmGOdVmwRlE6aKjeRskNkfLrS2wC8ixlhFsrkjQXM',
        name='pethub_app'
    )

    token, is_created = AccessToken.objects.get_or_create(
        user=user_instance,
        application=application_instance,
        expires=expires,
        scope=scope,
        token='testtoken',
    )

    print(">> script run successful.")


if __name__ == '__main__':
    from django.contrib.auth.models import User
    from oauth2_provider.models import Application, AccessToken
    from pethub.settings import OAUTH2_PROVIDER
    from django.utils.timezone import now
    from datetime import timedelta

    start_time = time.time()
    create()
