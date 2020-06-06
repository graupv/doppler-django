from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from permissions.services import APIPermissionClassFactory
from track.models import Track
from track.serializers import TrackSerializer
from guardian.shortcuts import assign_perm
from django.core.exceptions import PermissionDenied

def evaluar_user(user, obj, request):
    #   user making request === track owner
    # print('eval\n')
    # print(user, obj, request)
    return user.username == obj.username

class TrackViewSet(viewsets.ModelViewSet):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
    permission_classes = (
        APIPermissionClassFactory(
            name='TrackPermission',
            permission_configuration={
                'base': {
                    'create': lambda user, req: user.is_authenticated,
                    # 'list': lambda user, req: user.is_authenticated,
                    'mistracks': lambda user, req: user.is_authenticated,
                },
                'instance': {
                    'retrieve': evaluar_user,
                    'destroy': evaluar_user,
                    'update': evaluar_user,
                    'partial_update': evaluar_user,
                    # 'create': evaluar_user,
                    'lyrics': evaluar_user,
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
            track = serializer.save()
            #   asociar track con usuario y sus permisos
            assign_perm('track.change_track', user, track)
            assign_perm('track.view_track', user, track)
            return Response(serializer.data)

    @action(detail=True, url_path='lyrics', methods=['get'])
    def lyrics(self, request, pk=None):
        usn = self.request.user
        if Track.objects.filter(track_id=pk, username=usn.username).count() == 0:
            return Response({'Status': 'Unauthorized'})

        else:
            track = Track.objects.get(track_id=pk)
            paroles = track.lyrics
            return Response({'Lyrics': paroles})

    @action(detail=False, url_path='mytracks', methods=['get'])
    def mistracks(self, request, pk=None):
        # print(type(request), request)
        usn = self.request.user
        # print(usn)
        the_tracks = Track.objects.filter(username=usn.username)
        return Response(TrackSerializer(the_tracks, many=True).data)