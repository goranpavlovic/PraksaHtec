__author__ = 'vladimir'

from django.db import models
from django.core import validators


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


class PlayersAllStar(models.Model):
    pass


class PlayersCareer(models.Model):
    player_id = models.CharField(max_length=15)
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




