from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from permissions.services import APIPermissionClassFactory
from phrasebox.models import Phrasebox
from phrasebox.serializers import PhraseboxSerializer
from guardian.shortcuts import assign_perm
from django.core.exceptions import PermissionDenied


def evaluar_user(user, obj, request):
    #   user making request === track owner
    # print('eval\n')
    # print(user, obj, request)
    return user.username == obj.username

class PhraseboxSet(viewsets.ModelViewSet):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
    permission_classes = (
        APIPermissionClassFactory(
            name='TrackPermission',
            permission_configuration={
                'base': {
                    'create': lambda user, req: user.is_authenticated,
                    # 'list': lambda user, req: user.is_authenticated,
                    'myphrases': lambda user, req: user.is_authenticated,
                },
                'instance': {
                    'retrieve': evaluar_user,
                    'destroy': evaluar_user,
                    'update': evaluar_user,
                    'partial_update': evaluar_user,
                    # 'create': evaluar_user,
                }
            }
        ),
    )

    def perform_create(self, serializer):
        #   get user making request and check auth.
        user = self.request.user
        if not user.is_authenticated:
            raise PermissionDenied('Unauthenticated')
        else:
            phrase = serializer.save()
            #   asociar phrase con usuario y sus permisos
            assign_perm('phrase.phrase', user, phrase)
            assign_perm('phrase.phrase', user, phrase)
            return Response(serializer.data)

    @action(detail=False, url_path='myphrases', methods=['get'])
    def myphrases(self, request, pk=None):
        # print(type(request), request)
        usn = self.request.user
        # print(usn)
        the_words = Phrasebox.objects.filter(username=usn.username)
        return Response(TrackSerializer(the_tracks, many=True).data)