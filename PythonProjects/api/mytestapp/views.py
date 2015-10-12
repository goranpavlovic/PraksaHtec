from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json
# Create your views here.


class GetUser(APIView):

    def get(self, request, format=None):

        id = request.GET.get('id')

        data = {
            "firstName": 'John',
            "lastName": 'Doe',
            "email": "john.doe@gmail.com",
            "permissions": ["can_add_record", "can_edit_record", "can_delete_record"],
        }

        print "--------------getting user: " + str(id) + "-------"

        return Response(data=data, status=status.HTTP_200_OK)

    def post(self, request, format=None):

        id = request.POST.get('id')
        email = request.POST.get('email')

        #user = get_object_or_404(User, pk=request.POST.get('id'))
        #user.email = request.POST.get('email')

        print "--------------saving user: " + str(id) + "-------"
        print "--------------saving user: " + str(email) + "-------"

        return Response(data={'status': 'success'}, status=status.HTTP_200_OK)

from django.shortcuts import render

# Create your views here.
import json
from rest_framework.response import Response

from rest_framework.views import APIView
from rest_framework.decorators import detail_route, list_route
from rest_framework import status, viewsets
from mytestapp.models import MyTestModel, Musician, Album, Song
from mytestapp.serializers import MySerializer, MusicSerializer, SongSerializerTwo, SongSerializer
from serializers import NameSerializer
from django.core.exceptions import ValidationError
import time


class MyFirstView(APIView):

    def get(self, request, format=None):

        objects = MyTestModel.objects.all()
        serializer = MySerializer(objects, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def post(self, request, format=None):
        name = request.POST.get('test_field')
        # insert
        tf = MyTestModel(test_field=name)
        tf.save()
        # update
        tf = "Base: " + tf.test_field
        tf.save()
        serializer = MySerializer(tf)
        return Response(status=status.HTTP_201_CREATED, data=serializer.data)


class AnotherView(APIView):
    """
    This method will return data about musicians in the following format:
        [
          {
            "id": 4,
            "first_name": "Bora",
            "last_name": "Djordjevic",
            "instrument": "Gitara"
          }
        ]
    """

    def get(self, request, format=None):
        objects = Musician.objects.all()
        serializer = MusicSerializer(data=objects, many=True)
        serializer.is_valid(raise_exception=False)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def post(self, request, format=None):
        first_name = request.POST.get(u'first_name')
        last_name = request.POST.get(u'last_name')
        instrument = request.POST.get(u'instrument')
        temp = Musician(first_name=first_name, last_name=last_name, instrument=instrument)
        temp.save()
        serializer = MusicSerializer(temp)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

from django.shortcuts import get_object_or_404


class SetMusicianName(APIView):
    def post(self, request, format=None):
        id = request.POST.get(u'id')
        first_name = request.POST.get(u'first_name')
        if first_name is None and len(first_name) == 0:
            return Response(status=status.HTTP_400_BAD_REQUEST, data="You must send first_name")
        musician = get_object_or_404(Musician, pk=id)
        musician.first_name = first_name
        musician.save()
        serializer = MusicSerializer(musician)
        return Response(status=status.HTTP_200_OK, data=serializer.data)


class SetMusicianCountry(APIView):
    def get(self):
        pass
    def post(self, request, format=None):
        first_name = request.POST.get(u'first_name')
        last_name = request.POST.get(u'last_name')
        id = request.POST.get(u'id')
        country = request.POST.get(u'country')
        if (first_name is None and len(first_name) == 0) or (last_name is None and len(last_name) == 0):
            return Response(status=status.HTTP_400_BAD_REQUEST, data="Put first and last name of musician")
        # if first_name is None and len(first_name):
            # return Response(status=status.HTTP_200_OK, data="Put first name and change country for that name!")
        #musician = get_object_or_404(Musician, pk=id, first_name=first_name, last_name=last_name)
        musician = get_object_or_404(Musician, pk=id)
        musician.country = country
        musician.save()
        serializer = MusicSerializer(musician)
        return Response(status=status.HTTP_200_OK, data=serializer.data)


class MusicianInfo(APIView):

    def get(self, request, format=None):
        musician_id = request.GET.get('id')
        if musician_id is None:
            return Response(status=status.HTTP_400_BAD_REQUEST, data="Musician with this id doesn't exist")
        #objects = Musician.objects.filter(id_).order_by('release_date')
        musician = get_object_or_404(Musician, pk=musician_id)
        serializer = MusicSerializer(musician)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def post(self, request, format=None):
        id = request.POST.get(u'id')
        first_name = request.POST.get(u'first_name')
        last_name = request.POST.get(u'last_name')
        instrument = request.POST.get(u'instrument')
        age = request.POST.get(u'age')
        country = request.POST.get(u'country')
        if id is None:
            return Response(status=status.HTTP_400_BAD_REQUEST, data="Musician with this id doesn't exist")

        musician = get_object_or_404(Musician, pk=id)
        if first_name is not None:
            musician.first_name = first_name
        if last_name is not None:
            musician.last_name = last_name
        if instrument is not None:
            musician.instrument = instrument
        if age is not None:
            musician.age = age
        if country is not None:
            musician.country = country

        musician.save()
        serializer = MusicSerializer(musician)
        return Response(status=status.HTTP_200_OK, data=serializer.data)


class SongInfo(APIView):

    def get(self, request, format=None):
        song_id = request.GET.get('id')
        if song_id is None:
            return Response(status=status.HTTP_400_BAD_REQUEST, data="Song with this id doesn't exist")
        song = Song.objects.get(pk=song_id)
        serializer = SongSerializerTwo(song)
        return Response(status=status.HTTP_200_OK, data=serializer.data)


class MusicianViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Musician.objects.all()
        serializer = MusicSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Musician.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = MusicSerializer(user)
        return Response(serializer.data)


class SongViewSet(viewsets.ViewSet):

    # queryset = Song.objects.all()
    # serializer_class = SongSerializer

    def list(self, request, format=None):

        return Response(status.HTTP_200_OK)

    @detail_route(methods=['post'])
    def set_name(self, request, pk=None):
        name = request.POST.get('name')
        song = get_object_or_404(Song, pk=pk)


        #jedan nacin za update modela
        song.name = name
        try:
            song.full_clean()
        except ValidationError as e:
            return Response(e.message_dict, status=status.HTTP_400_BAD_REQUEST)
        song.save()
        """
        #drugi nacin preko serializera i provere validnosti u serializerima
        nameSerializier = NameSerializer(data=request.POST)
        if nameSerializier.is_valid():
            song.name = nameSerializier.data['name']
            song.save()
        else:
            return Response(nameSerializier.data, status=status.HTTP_400_BAD_REQUEST)
        """
        return Response(SongSerializer(song).data, status=status.HTTP_200_OK)

    @list_route(methods=['get'])
    def longest_songs(self, request):
        # longest_songs = Song.objects.filter(id__gt=2)
        longest_songs = Song.objects.filter(duration__lt='00:03:00')
        longest_songs = longest_songs.order_by('duration')
        serializer = SongSerializer(longest_songs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# --------------------------------------------------------------------------
# ------------------------------ BASKETBALL --------------------------------
# --------------------------------------------------------------------------

from mytestapp.models import Players, PlayersAllStar, PlayersCareer, Teams,\
                             TeamSeason, Coaches, CoachesCareer, PlayersPlayOff, \
                             PlayersRegularSeason, PlayersImage

from mytestapp.serializers import PlayersSerializer, PlayersRegularSeasonSerializer, \
                                  PlayersPlayoffSerializer, PlayersAllStarSerializer, PlayerImageSerializer


class PlayersView(APIView):
    def get(self, request, format=None):
        player_id = request.GET.get(u'id')
        player_first_season = request.GET.get(u'first')
        if player_id is None:
            return Response(status=status.HTTP_400_BAD_REQUEST, data="Player with this id doesn't exist.")
        player = get_object_or_404(Players, pk=player_id)
        serializer = PlayersSerializer(player)
        serializer_2 = None

        if player_first_season is not None:
            # if type(player_first_season) == int:
            #     objects = Players.objects.all().get(pk=player_first_season)
                objects = Players.objects.all().filter(first_season__gt=player_first_season)
                serializer_2 = PlayersSerializer(objects, many=True)

        if serializer_2 is None:
            return Response(serializer.data, status.HTTP_200_OK)
        else:
            return Response([serializer.data, serializer_2.data],  status.HTTP_200_OK)

    def post(self, request, format=None):
        pass


class PlayersViewTwo(APIView):
    # Here we make get method which can retrieve list of desired data
    def get(self, request, format=None):
        player_id = request.GET.get(u'player_id')
        first_name = request.GET.get(u'first_name')
        last_name = request.GET.get(u'last_name')
        position = request.GET.get(u'position')
        first_season = request.GET.get(u'first_season')
        last_season = request.GET.get(u'last_season')

        # Get all rows from table Players
        objects = Players.objects.all()

        # Filtering table by id, name, position, season
        if player_id is not None:
            objects = objects.filter(pk=player_id)
        if first_name is not None:
            objects = objects.filter(first_name=first_name)
        if last_name is not None:
            objects = objects.filter(last_name=last_name)
        if position is not None:
            objects = objects.filter(position=position)
        if first_season is not None:
            objects = objects.filter(first_season=first_season)
        if last_season is not None:
            objects = objects.filter(last_season=last_season)

        serializer = PlayersSerializer(objects, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class PlayersRegularSeasonView(APIView):
    def get(self, request, format=None):
        player_id = request.GET.get(u'player_id')
        if player_id is None:
            return Response(status=status.HTTP_400_BAD_REQUEST, data="Player with this id doesn't exist.")

        objects = PlayersRegularSeason.objects.filter(player_id=player_id)
        serializer = PlayersRegularSeasonSerializer(objects, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class PlayersPlayoffView(APIView):
    def get(self, requet, format=None):
        player_id = requet.GET.get(u'player_id')
        if player_id is None:
            return Response(status=status.HTTP_400_BAD_REQUEST, data="Player with this id doesn't exist.")

        objects = PlayersPlayOff.objects.filter(player_id=player_id)
        serializer = PlayersPlayoffSerializer(objects, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class PlayersAllStarView(APIView):
    #  Auxiliary method for statistics modes
    def compare(self, mode):
        if mode == 'gt' or mode == 'lt' or mode == 'eq' or\
           mode == 'gte' or mode == 'lte':
            return True
        else:
            return False

    def get(self, request, format=None):
        player_id = request.GET.get(u'player_id')
        first_name = request.GET.get(u'first_name')
        last_name = request.GET.get(u'last_name')
        conference = request.GET.get(u'conference')
        year = request.GET.get(u'year')
        points = request.GET.get(u'points')
        rebounds = request.GET.get(u'rebounds')
        assists = request.GET.get(u'assists')
        blocks = request.GET.get(u'blocks')

        #   Modes for points, rebounds, assists, blocks
        #   GREATER, LESS, EQUALS, GREATER or EQUALS, LESS or EQUALS
        #   gt, lt, eq, gte, lte

        pts_mode = request.GET.get(u'pts_mode')
        reb_mode = request.GET.get(u'reb_mode')
        ast_mode = request.GET.get(u'ast_mode')
        blk_mode = request.GET.get(u'blk_mode')

        # Get all objects, all rows from Table All-Star
        objects = PlayersAllStar.objects.all()

        # Checking parameter points
        if points is not None:
            # If user put some value for parameter points, he must check the mode
            # if mode is checked
            if pts_mode is not None:
                # in case when mode take incorrect value
                # we show the message about error
                if self.compare(pts_mode) is False:
                    return Response(status=status.HTTP_400_BAD_REQUEST, data="Invalid mode for parameter points.")

                # here, we have correct value and correct mode
                else:
                    if pts_mode == 'gt':
                        objects = objects.filter(points__gt=points)
                    elif pts_mode == 'gte':
                        objects = objects.filter(points__gte=points)
                    elif pts_mode == 'lt':
                        objects = objects.filter(points__lt=points)
                    elif pts_mode == 'lte':
                        objects = objects.filter(points__lte=points)
                    else:
                        objects = objects.filter(points=points)

            # if mode isn't checked
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST, data="Check mode for points")

        # Checking parameter rebounds
        if rebounds is not None:
            # Checked mode
            if reb_mode is not None:
                # Invalid mode
                if self.compare(reb_mode) is False:
                    return Response(status=status.HTTP_400_BAD_REQUEST, data="Invalid mode for parameter rebounds.")

                # Correct mode
                else:
                    if reb_mode == 'gt':
                        objects = objects.filter(rebounds__gt=rebounds)
                    elif reb_mode == 'gte':
                        objects = objects.filter(rebounds__gte=rebounds)
                    elif reb_mode == 'lt':
                        objects = objects.filter(rebounds__lt=rebounds)
                    elif reb_mode == 'lte':
                        objects = objects.filter(rebounds__lte=rebounds)
                    else:
                        objects = objects.filter(rebounds=rebounds)

            # Not checked mode
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST, data="Check mode for rebounds")

        # Checking parameter assists
        if assists is not None:
            # Checked mode
            if ast_mode is not None:
                # Invalid mode
                if self.compare(ast_mode) is False:
                    return Response(status=status.HTTP_400_BAD_REQUEST, data="Invalid mode for parameter assists.")

                # Correct mode
                else:
                    if ast_mode == 'gt':
                        objects = objects.filter(assists__gt=assists)
                    elif ast_mode == 'gte':
                        objects = objects.filter(assists__gte=assists)
                    elif ast_mode == 'lt':
                        objects = objects.filter(assists__lt=assists)
                    elif ast_mode == 'lte':
                        objects = objects.filter(assists__lte=assists)
                    else:
                        objects = objects.filter(assists=assists)

            # Not checked mode
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST, data="Check mode for rebounds")

        # Checking parameter blocks
        if blocks is not None:
            # Checked mode
            if blk_mode is not None:
                # Invalid mode
                if self.compare(blk_mode) is False:
                    return Response(status=status.HTTP_400_BAD_REQUEST, data="Invalid mode for parameter blocks.")

                # Correct mode
                else:
                    if blk_mode == 'gt':
                        objects = objects.filter(blocks__gt=blocks)
                    elif blk_mode == 'gte':
                        objects = objects.filter(blocks__gte=blocks)
                    elif blk_mode == 'lt':
                        objects = objects.filter(blocks__lt=blocks)
                    elif blk_mode == 'lte':
                        objects = objects.filter(blocks__lte=blocks)
                    else:
                        objects = objects.filter(blocks=blocks)
            # Not checked mode
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST, data="Check mode for rebounds")

        if player_id is not None:
            objects = objects.filter(all_player=player_id)
        if first_name is not None:
            objects = objects.filter(first_name=first_name)
        if last_name is not None:
            objects = objects.filter(last_name=last_name)

        if conference is not None:
            # Here we check name of conference
            # Invalid conference name, return message error
            if conference != 'east' and conference != 'west':
                return Response(status=status.HTTP_400_BAD_REQUEST,
                                data="You must put 'east' or 'west' for parameter conference.")

            # Correct conference name, filtering my conference
            else:
                objects = objects.filter(conference=conference)

        if year is not None:
            objects = objects.filter(all_star_year=year)

        serializer = PlayersAllStarSerializer(objects, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class PlayersImageView(APIView):
    def get(self, request, format=None):
        player_id = request.GET.get(u'player_id')
        image = PlayersImage.objects.all().filter(player_id=player_id)
        serializer = PlayerImageSerializer(image, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

