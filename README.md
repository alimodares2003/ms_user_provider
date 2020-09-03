# Mesghal user provider
# Installation

Add this line to your ```requirements.txt```
```
git+https://github.com/alimodares2003/ms_user_provider.git#egg=mesghal-user-provider
```
or use pip
```
pip install git+https://github.com/alimodares2003/ms_user_provider.git#egg=mesghal-user-provider
```
# Usage
1. Add library to ```INSTALLED_APPS``` in ```settings.py``` :

```
INSTALLED_APPS = [
    ...
    'ms_user_provider',
]
```

2. Add middleware in ```settings.py``` :
```
MIDDLEWARE = [
    ...
    'ms_user_provider.middleware.MesghalMiddleware',
]
```

Now you have access to user model as django's default user model:
```
class TestView(APIView):
    def get(self, request):
        # request.user.id
        # request.user.username
        # request.user.mobile
        # request.user.email
        # request.user.fisrt_name
        # request.user.last_name
        return Response(request.user.name)
```