from django.contrib.auth import login
from knox.views import LoginView
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer


class CustomLoginView(LoginView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(CustomLoginView, self).post(request, format=None)

