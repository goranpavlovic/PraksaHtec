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

