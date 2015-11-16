# Create your models here.
from django.db import models
from django.core import validators


# Create your models here.
class MyTestModel(models.Model):
    test_field = models.TextField()


class Musician(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    instrument = models.CharField(max_length=50)
    age = models.IntegerField(null=True)
    country = models.CharField(max_length=30, null=True)


class ProductionHouse(models.Model):
    name = models.CharField(max_length=50)
    director = models.CharField(max_length=30)
    founded = models.DateField()
    budget = models.IntegerField()


class Album(models.Model):
    artist = models.ForeignKey(Musician)
    producer = models.ForeignKey(ProductionHouse, null=True)
    name = models.CharField(max_length=50)
    release_date = models.DateField()
    num_stars = models.IntegerField()


class Song(models.Model):
    album = models.ForeignKey(Album)
    name = models.CharField(max_length=50)
    duration = models.TimeField(null=True)

# ------------------------------------------------------------------------------------------ #
# ------------------------------------ BASKETBALL ------------------------------------------ #
# ------------------------------------------------------------------------------------------ #


class Players(models.Model):
    CENTER = 'C'
    FORWARD = 'F'
    POWER_FORWARD = 'PF'
    POWER_GUARD = 'PG'
    GUARD = 'G'
    PLAYER_POSITION = (
        (CENTER, 'Center'),
        (FORWARD, 'Forward'),
        (POWER_FORWARD, 'Power Forward'),
        (GUARD, 'Guard'),
        (POWER_GUARD, 'Power Guard')
    )

    player_id = models.CharField(max_length=10, primary_key=True)
    first_name = models.CharField(max_length=50, null=True, editable=False)
    last_name = models.CharField(max_length=50, null=True, editable=False)

    position = models.CharField(max_length=2,
                                choices=PLAYER_POSITION,
                                default=GUARD,  # Default is GUARD, but field can be null value,
                                null=True)      # so, here, we set null to be TRUE

    first_season = models.PositiveIntegerField(null=True,
                                               # Season year must in range (1950, 2015)
                                               validators=[
                                                   validators.MinValueValidator(1950),
                                                   validators.MaxValueValidator(2015)
                                               ])
    last_season = models.PositiveIntegerField(null=True,
                                              validators=[
                                                  validators.MinValueValidator(1950),
                                                  validators.MaxValueValidator(2015)
                                              ])

    height_feet = models.FloatField(null=True,
                                    validators=[                            # Player height constraints,
                                        validators.MinValueValidator(5.0),  # player can't be lower then 150 cm
                                        validators.MaxValueValidator(8.0)   # and can't be higher than 240 cm
                                    ])

    height_inches = models.FloatField(null=True,
                                      validators=[          # Same concept like with feet, above
                                          validators.MinValueValidator(59.0),
                                          validators.MaxValueValidator(94.0)
                                      ])

    weight = models.FloatField(null=True)
    college = models.CharField(max_length=50, null=True)
    birth_date = models.DateTimeField(null=True)


class PlayersCareer(models.Model):
    player_id = models.CharField(max_length=15, db_index=True)
    first_name = models.CharField(max_length=50, null=True, editable=False)
    last_name = models.CharField(max_length=50, null=True, editable=False)
    games_played = models.IntegerField()
    minutes = models.IntegerField()
    points = models.IntegerField()
    off_rebounds = models.IntegerField()
    def_rebounds = models.IntegerField()
    rebounds = models.IntegerField()
    assists = models.IntegerField()
    steals = models.IntegerField()
    blocks = models.IntegerField()
    turnovers = models.IntegerField()


class PlayersRegularSeason(models.Model):
    player_id = models.CharField(max_length=15, db_index=True)
    first_name = models.CharField(max_length=50, null=True, editable=False)
    last_name = models.CharField(max_length=50, null=True, editable=False)
    year = models.IntegerField(null=True,
                               validators=[
                                    validators.MinValueValidator(1950),
                                    validators.MaxValueValidator(2015)
                               ])
    team = models.CharField(max_length=15)
    games_played = models.IntegerField()
    minutes = models.IntegerField()
    points = models.IntegerField()
    off_rebounds = models.IntegerField()
    def_rebounds = models.IntegerField()
    rebounds = models.IntegerField()
    assists = models.IntegerField()
    steals = models.IntegerField()
    blocks = models.IntegerField()
    turnovers = models.IntegerField()


class PlayersPlayOff(models.Model):
    player_id = models.CharField(max_length=15, db_index=True)
    first_name = models.CharField(max_length=50, null=True, editable=False)
    last_name = models.CharField(max_length=50, null=True, editable=False)
    year = models.IntegerField(null=True,
                               validators=[
                                    validators.MinValueValidator(1950),
                                    validators.MaxValueValidator(2015)
                               ])
    team = models.CharField(max_length=15)
    games_played = models.IntegerField()
    minutes = models.IntegerField()
    points = models.IntegerField()
    off_rebounds = models.IntegerField()
    def_rebounds = models.IntegerField()
    rebounds = models.IntegerField()
    assists = models.IntegerField()
    steals = models.IntegerField()
    blocks = models.IntegerField()
    turnovers = models.IntegerField()


class PlayersAllStar(models.Model):
    all_star_year = models.IntegerField(validators=[    # Year must be between 1947 and 2015
                                            validators.MinValueValidator(1947),
                                            validators.MaxValueValidator(2015)
                                        ])
    all_player = models.ForeignKey(Players)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    conference = models.CharField(max_length=50)
    minutes = models.IntegerField(null=True)
    points = models.IntegerField(null=True)
    off_rebounds = models.IntegerField(null=True)
    def_rebounds = models.IntegerField(null=True)
    rebounds = models.IntegerField(null=True)
    assists = models.IntegerField(null=True)
    steals = models.IntegerField(null=True)
    blocks = models.IntegerField(null=True)
    turnovers = models.IntegerField(null=True)


class Teams(models.Model):
    team = models.CharField(max_length=10, null=True)
    location = models.CharField(max_length=30, null=True)
    name = models.CharField(max_length=30, null=True)
    league = models.CharField(max_length=10, null=True)


class TeamSeason(models.Model):
    team = models.CharField(max_length=10, null=True)
    year = models.IntegerField(validators=[
                                    validators.MinValueValidator(1947),
                                    validators.MaxValueValidator(2015)
                               ],
                               null=True)
    league = models.CharField(max_length=10, null=True)
    o_fgm = models.IntegerField(null=True)
    o_fga = models.IntegerField(null=True)
    o_ftm = models.IntegerField(null=True)
    o_fta = models.IntegerField(null=True)
    o_oreb = models.IntegerField(null=True)
    o_dreb = models.IntegerField(null=True)
    o_reb = models.IntegerField(null=True)
    o_asts = models.IntegerField(null=True)
    o_pf = models.IntegerField(null=True)
    o_stl = models.IntegerField(null=True)
    o_to = models.IntegerField(null=True)
    o_blk = models.IntegerField(null=True)
    o_3pm = models.IntegerField(null=True)
    o_3pa = models.IntegerField(null=True)
    o_pts = models.IntegerField(null=True)
    d_fgm = models.IntegerField(null=True)
    d_fga = models.IntegerField(null=True)
    d_ftm = models.IntegerField(null=True)
    d_fta = models.IntegerField(null=True)
    d_oreb = models.IntegerField(null=True)
    d_dreb = models.IntegerField(null=True)
    d_reb = models.IntegerField(null=True)
    d_asts = models.IntegerField(null=True)
    d_pf = models.IntegerField(null=True)
    d_stl = models.IntegerField(null=True)
    d_to = models.IntegerField(null=True)
    d_blk = models.IntegerField(null=True)
    d_3pm = models.IntegerField(null=True)
    d_3pa = models.IntegerField(null=True)
    d_pts = models.IntegerField(null=True)
    pace = models.IntegerField(null=True)
    won = models.IntegerField(null=True)
    lost = models.IntegerField(null=True)


class Coaches(models.Model):
    coach_id = models.CharField(max_length=15, null=True)
    year = models.IntegerField(null=True)
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)
    season_win = models.IntegerField(null=True)
    season_loss = models.IntegerField(null=True)
    playoff_win = models.IntegerField(null=True)
    playoff_loss = models.IntegerField(null=True)
    team = models.CharField(max_length=10, null=True)


class CoachesCareer(models.Model):
    coach_id = models.CharField(max_length=15, null=True)
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)
    season_win = models.IntegerField(null=True)
    season_loss = models.IntegerField(null=True)
    playoff_win = models.IntegerField(null=True)
    playoff_loss = models.IntegerField(null=True)


class PlayersImage(models.Model):
    player_id = models.CharField(max_length=15)
    image = models.CharField(max_length=200)

# -------------------------------------------------------------------------------------------------------
# -------------------------------------------- MONGO ----------------------------------------------------
# -------------------------------------------------------------------------------------------------------

from mongoengine import *


class Person(Document):
    first_name = StringField()
    last_name = StringField()
    age = IntField()


class Statistics(EmbeddedDocument):
    year = IntField()
    points = IntField()
    rebounds = IntField()
    minutes = IntField()
    position = StringField()


class Player(Document):
    first_name = StringField()
    last_name = StringField()
    seasons = ListField(EmbeddedDocumentField(Statistics))
