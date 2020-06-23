from rest_framework import permissions, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

from django.contrib.auth import get_user_model 
from django.contrib.auth.models import User 
from permissions.services import APIPermissionClassFactory

from account.serializers import UserSerializer


class CreateUserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    model = get_user_model()
    parser_classes = [JSONParser]
    serializer_class = UserSerializer
    # permission_classes = (
    #     APIPermissionClassFactory(
    #         name='AccountPermission',
    #         permission_configuration={
    #             'base': {
    #                 'create': permissions.AllowAny,
    #                 #   anyone can sign up
    #                 # 'list': lambda user, req: user.is_authenticated,
    #                 #   list -> user.is_admin o algo despues
                    
    #             },
    #             'instance': {
    #                 #   empty to avoid user requests
    #                 # 'retrieve': evaluar_user,
    #                 # 'destroy': evaluar_user,
    #                 # 'update': evaluar_user,
    #                 # 'partial_update': evaluar_user,
    #                 # # 'create': evaluar_user,
    #             }
    #         }
    #     ),
    # )
    

    @action(detail=False, url_path='create', methods=['POST'], permission_classes=[permissions.AllowAny])
    def create_user(self, request):

        data = self.request.data
        #   get querydict object with Body data
        username = data.get('username')
        pw = data.get("password")
        email = data.get('email')

        #   Wrap in try and return errors
        try:
            user = User.objects.create(username=username, email=email)
            user.set_password(pw)
            user.save()
            print('User created')
            return Response(status=status.HTTP_201_CREATED)
        except Exception as e:
            print('Create user exception\n', e)
            return Response({'Result': 'Recevied but unable to create user'}, status=status.HTTP_202_ACCEPTED)
        
        

    @action(detail=True, url_path='edit', methods=['POST'], permission_classes=[permissions.IsAuthenticated])
    def modify_user(self, request, pk=None):

        user = self.request.user
        print(user, user.id)
        print(pk)
        if pk != user.id:
            #   user cannot change a different user's details
            #   or simply wrong url
            return Response(status=status.HTTP_403_FORBIDDEN)
        else:
            
            return Response({'Status': 'Modified something'}, status=status.HTTP_200_OK)