# django-steam

Steam api and authentication for django

## Installation

```
pip install django_steam
```

## Configuration

First install the required apps and set the required settings :
```
INSTALLED_APPS = (
    ...
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django_openid_auth',
    'django_steam_api',
    'django_steam',
    ...
)


AUTHENTICATION_BACKENDS = (
    ...
    'django_openid_auth.auth.OpenIDBackend',
    ...
)

LOGIN_URL = '/path/to/openid/login/'
OPENID_CREATE_USERS = True
STEAM_API_KEY = 'YOURSTEAMAPIKEY'

# recommended
OPENID_SSO_SERVER_URL = 'http://steamcommunity.com/openid'
SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'


# optional
OPENID_UPDATE_DETAILS_FROM_SREG = True
ALLOWED_EXTERNAL_OPENID_REDIRECT_DOMAINS = ['http://example.org']
OPENID_STRICT_USERNAMES = False
# see https://github.com/edx/django-openid-auth
# and https://github.com/voblivion/django-steam-api
```

Add openid urls to your configuration :
```
urlpatterns = patterns('',
    ...
    (r'^openid/', include('django_openid_auth.urls')),
    ...
)
```


Then update database scheme  :
```
./manage.py migrate
```

## Usage

Use any of django-steam-api models.

Give your users link to steam auth :
```
<a href="/openid/login">
    <img src="https://steamcommunity-a.akamaihd.net/public/images/signinthroughsteam/sits_01.png" width="180" height="35" border="0">
</a>
```

Access steam's player profile of authenticated users :
```
if user.steam:
    do_something_with(user.steam.player)
```
