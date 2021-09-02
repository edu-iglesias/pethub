import datetime

from django.contrib.auth.models import User
from django.utils import timezone
from oauth2_provider.models import AccessToken, RefreshToken
from oauthlib.common import generate_token


def generate_tokens(app, account, scope="read write"):
    """Generate Access and Refresh tokens for an oauth2 app's account"""

    next_week = timezone.now() + datetime.timedelta(weeks=1)
    access_token = AccessToken.objects.create(
        application=app,
        user=account,
        scope=scope,
        token=generate_token(),
        expires=next_week,
    )
    refresh_token = RefreshToken.objects.create(
        application=app, user=account, access_token=access_token, token=generate_token()
    )
    return access_token, refresh_token

def get_tokens_via_username(username):

    user_instance = User.objects.filter(username=username).first()

    access_token = AccessToken.objects.filter(
        user=user_instance,
    ).first()

    refresh_token = RefreshToken.objects.filter(access_token=access_token).first()

    tokens = {
        "access_token": access_token.token,
        "refresh_token": refresh_token.token,
        "expires": access_token.expires,
        "scope": access_token.scope,
    }

    return tokens

