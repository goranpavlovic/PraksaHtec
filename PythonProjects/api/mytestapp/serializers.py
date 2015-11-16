__author__ = 'tehnika'

from rest_framework import serializers
from mytestapp.models import MyTestModel, Musician, Album, Song, ProductionHouse
from django.db.models import Sum, Count


class MySerializer(serializers.ModelSerializer):
    class Meta:
        model = MyTestModel
        fields = ('id', 'test_field')


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ('id', 'name', 'duration')


class ProductionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductionHouse
        fields = ('id', 'name', 'director', 'founded', 'budget')


class AlbumSerializer(serializers.ModelSerializer):

    production_house = serializers.SerializerMethodField()
    songs = serializers.SerializerMethodField()
    duration_of_album = serializers.SerializerMethodField()
    num_of_songs = serializers.SerializerMethodField()

    class Meta:
        model = Album
        fields = ('id', 'artist', 'name', 'release_date', 'num_stars', 'production_house',
                  'songs', 'duration_of_album', 'num_of_songs')

    def get_production_house(self, obj):
        production_house = obj.producer
        serializer = ProductionSerializer(production_house)
        return serializer.data

    def get_songs(self, obj):
        songs = obj.song_set.all()
        serializer = SongSerializer(songs, many=True)
        return serializer.data

    def seconds_to_time(self, time_s):
        if time_s is not None:
            h = time_s / 3600
            h = int(h)
            m = (time_s - h * 3600) / 60
            m = int(m)
            s = time_s - h * 3600 - m * 60
            # s = int(round(s))
            return "%d:%d:%d" % (h, m, s)
        else:
            return "00:00:00"

    def get_duration_of_album(self, obj):
        duration_of_album = obj.song_set.all().aggregate(Sum('duration'))
        # return self.seconds_to_time(duration_of_album.get('duration__sum'))
        query_string = "SELECT a.id as id, Sum(TIME_TO_SEC(s.duration)) as sum " \
                       "FROM usermanagement_song as s, usermanagement_album as a " \
                       "WHERE s.album_id = a.id and a.id=%s"
        aggregation = Song.objects.raw(query_string, [obj.id, ])
        try:
            return self.seconds_to_time(aggregation[0].sum)
        except Exception as e:
            return ""

    def get_num_of_songs(self, obj):
        num_of_songs = obj.song_set.all().aggregate(Count('id'))
        return num_of_songs


class MusicSerializer(serializers.ModelSerializer):

    albums = serializers.SerializerMethodField()

    class Meta:
        model = Musician
        fields = ('id', 'first_name', 'last_name', 'instrument', 'age', 'country', 'albums')

    def get_albums(self, obj):
        albums = obj.album_set.all()
        serializer = AlbumSerializer(albums, many=True)
        return serializer.data


class MusicianSerializerTwo(serializers.ModelSerializer):
    class Meta:
        model = Musician
        fields = ('id', 'first_name', 'last_name', 'instrument', 'age', 'country')


class AlbumSerializerTwo(serializers.ModelSerializer):

    musician_info = serializers.SerializerMethodField()

    class Meta:
        model = Album
        fields = ('id', 'artist', 'name', 'release_date', 'num_stars', 'musician_info')

    def get_musician_info(self, obj):
        # musician_info = obj.artist
        serializer = MusicianSerializerTwo(obj.artist)
        return serializer.data


class SongSerializerTwo(serializers.ModelSerializer):

    album_info = serializers.SerializerMethodField()

    class Meta:
        model = Song
        fields = ('id', 'name', 'duration', 'album_info')

    def get_album_info(self, obj):
        # album_info = obj.album
        serializer = AlbumSerializerTwo(obj.album)
        return serializer.data


class NameSerializer(serializers.Serializer):

    name = serializers.CharField(max_length=50)


# --------------------------------------------------------------------------------------
# --------------------------------- BASKETBALL -----------------------------------------
# --------------------------------------------------------------------------------------

from models import Players, PlayersCareer, PlayersRegularSeason, PlayersPlayOff, PlayersAllStar, PlayersImage, \
                   Teams, TeamSeason


class PlayersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Players
        fields = ('player_id', 'first_name', 'last_name', 'position', 'first_season',
                  'last_season', 'height_feet', 'height_inches', 'weight', 'college',
                  'birth_date')


class PlayersStatisticsSerializer(serializers.ModelSerializer):
    pass


class PlayersCareerSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayersCareer
        fields = ('player_id', 'first_name', 'last_name', 'games_played', 'minutes', 'points',
                  'off_rebounds', 'def_rebounds', 'rebounds', 'assists', 'steals', 'blocks', 'turnovers')


class PlayersCareerStatisticsSerializer(serializers.ModelSerializer):
    pass


class PlayersAllStarSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayersAllStar
        fields = ('all_star_year', 'all_player', 'first_name', 'last_name', 'conference',
                  'minutes', 'points', 'off_rebounds', 'def_rebounds', 'rebounds',
                  'assists', 'steals', 'blocks', 'turnovers')


class PlayersRegularSeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayersRegularSeason
        fields = ('player_id', 'first_name', 'last_name', 'year', 'team', 'games_played', 'minutes', 'points',
                  'off_rebounds', 'def_rebounds', 'rebounds', 'assists', 'steals', 'blocks', 'turnovers')


class PlayersPlayoffSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayersPlayOff
        fields = ('player_id', 'first_name', 'last_name', 'year', 'team', 'games_played', 'minutes', 'points',
                  'off_rebounds', 'def_rebounds', 'rebounds', 'assists', 'steals', 'blocks', 'turnovers')


class PlayerImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayersImage
        fields = ('player_id', 'image')


class TeamAllSerializer(serializers.ModelSerializer):
    pass


class TeamSeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamSeason
        fields = ('team', 'year', 'league', 'o_fgm', 'o_fga', 'o_ftm', 'o_fta', 'o_oreb',
                  'o_dreb', 'o_reb', 'o_asts', 'o_pf', 'o_stl', 'o_to', 'o_blk', 'o_3pm',
                  'o_3pa', 'o_pts', 'pace', 'won', 'lost')


class CoachAllSerializer(serializers.ModelSerializer):
    pass


class CoachCareerSerializer(serializers.ModelSerializer):
    pass

