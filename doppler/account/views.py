from rest_framework import permissions
from rest_framework import viewsets
from django.contrib.auth import get_user_model 
from django.contrib.auth.models import User 
from permissions.services import APIPermissionClassFactory

from account.serializers import UserSerializer


class CreateUserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    model = get_user_model()
    serializer_class = UserSerializer
    permission_classes = (
        APIPermissionClassFactory(
            name='AccountPermission',
            permission_configuration={
                'base': {
                    'create': permissions.AllowAny,
                    #   anyone can sign up
                    # 'list': lambda user, req: user.is_authenticated,
                    #   list -> user.is_admin o algo despues
                    
                },
                'instance': {
                    #   empty to avoid user requests
                    # 'retrieve': evaluar_user,
                    # 'destroy': evaluar_user,
                    # 'update': evaluar_user,
                    # 'partial_update': evaluar_user,
                    # # 'create': evaluar_user,
                }
            }
        ),
    )