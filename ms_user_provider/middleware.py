from ms_user_provider.model import get_user_model


class MesghalMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        jwt_token = request.headers.get('Authorization')
        if jwt_token is not None:
            request.user = get_user_model(jwt_token)

        response = self.get_response(request)

        return response
