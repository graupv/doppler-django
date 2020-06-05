from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from permissions.services import APIPermissionClassFactory
from track.models import Track
from track.serializers import TrackSerializer

def evaluar_user(user, obj, request):
    #   user making request === track owner
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
                    'list': lambda user, req: user.is_authenticated,
                    'misTracks': lambda user, req: user.is_authenticated,
                },
                'instance': {
                    'retrieve': evaluar_user,
                    'destroy': evaluar_user,
                    'update': evaluar_user,
                    'partial_update': evaluar_user,
                    'create': evaluar_user,
                    'lyrics': evaluar_user,
                }
            }
        ),
    )

    def create(self, serializer):
        #   get user making request and check auth.
        user = self.request.user
        if not user.is_authenticated:
            raise PermissionDenied('Unauthenticated')
        else:
            track = serializer.save()
            #   asociar bebe con usuario y sus permisos
            assign_perm('track.change_track', user, track)
            assign_perm('track.view_track', user, track)
            return Response(serializer.data)

    @action(detail=True, url_path='lyrics', methods=['get'])
    def lyrics(self, request, pk=None):
        track = self.get_object()
        paroles = track.lyrics
        return Response({'status': 'ok lyrics'})

    @action(detail=False, url_path='mistracks', methods=['get'])
    def misTracks(self, request, pk=None):
        print(type(request), request)
        usn = self.request.user
        print(usn)
        the_tracks = Track.objects.get(username=usn.username)
        print(the_tracks)
        print(f'Got {Track.objects.filter(username=usn.username).count()} tracks')
        return Response(TrackSerializer(the_tracks).data)