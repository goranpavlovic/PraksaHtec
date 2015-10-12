'use strict';
/**
 * Created by vladimir on 7.10.15..
 */

angular.module('pythonProjectsApp')
    .factory('NBARegularFactory', ["$http", "SERVER", function ($http, SERVER) {

        function RegularSeasons(response) {
            var self = this;
            self.response = response;

            self.parse = function () {
                self.seasons = [];
                for (var i = 0; i < response.length; i++) {
                    self.seasons.push(new RegularSeason(response[i]));
                }
            };

            self.parse();
        }

        function RegularSeason(response) {
            var self = this;
            self.response = response;

            self.parse = function () {
                self.player_id = response.player_id;
                self.first_name = response.first_name;
                self.last_name = response.last_name;
                self.year = response.year;
                self.team = response.team;
                self.games_played = response.games_played;
                self.minutes = response.minutes;
                self.points = response.points;
                self.off_rebounds = response.off_rebounds;
                self.def_rebounds = response.def_rebounds;
                self.rebounds = response.rebounds;
                self.assists = response.assists;
                self.steals = response.steals;
                self.blocks = response.blocks;
                self.turnovers = response.turnovers;
            };

            self.parse();
        }

        function PlayoffSeasons(response) {
            var self = this;
            self.response = response;

            self.parse = function () {
                self.seasons = [];
                for (var i = 0; i < response.length; i++) {
                    self.seasons.push(new RegularSeason(response[i]));
                }
            };

            self.parse();
        }

        function PlayoffSeason(response) {
            var self = this;
            self.response = response;

            self.parse = function () {
                self.player_id = response.player_id;
                self.first_name = response.first_name;
                self.last_name = response.last_name;
                self.year = response.year;
                self.team = response.team;
                self.games_played = response.games_played;
                self.minutes = response.minutes;
                self.points = response.points;
                self.off_rebounds = response.off_rebounds;
                self.def_rebounds = response.def_rebounds;
                self.rebounds = response.rebounds;
                self.assists = response.assists;
                self.steals = response.steals;
                self.blocks = response.blocks;
                self.turnovers = response.turnovers;
            };

            self.parse();
        }

        // getter for all regular seasons
        function getRegularSeasonAll() {
            var regularAll = {
                seasons : []
            };
            return new RegularSeasons(regularAll);
        }

        // getter for one regular season from list
        // of all regular seasons
        function getRegularSeason() {
            var regular = {
                player_id : 0,
                first_name : '',
                last_name : '',
                year : 0,
                team : '',
                games_played : 0,
                minutes : 0,
                points : 0,
                off_rebounds : 0,
                def_rebounds : 0,
                rebounds : 0,
                assists : 0,
                steals : 0,
                blocks : 0,
                turnovers : 0
            };
            return new RegularSeason(regular);
        }

        // getter for all playoff seasons
        function getPlayoffSeasonAll() {
            var playoffAll = {
                seasons : []
            };
            return new PlayoffSeasons(playoffAll);
        }

        // getter for the one playoff season
        function getPlayoffSeason() {
            var playoff = {
                player_id : 0,
                first_name : '',
                last_name : '',
                year : 0,
                team : '',
                games_played : 0,
                minutes : 0,
                points : 0,
                off_rebounds : 0,
                def_rebounds : 0,
                rebounds : 0,
                assists : 0,
                steals : 0,
                blocks : 0,
                turnovers : 0
            };
            return new PlayoffSeason(playoff);
        }

        // taking of table PlayersRegularSeason from database
        var getStatisticsRegular = function (id) {
            return $http({
                method : 'GET',
                url: SERVER + "get-regular/?format=json&player_id=" + id
            }).then(function(response) {
                return new RegularSeasons(response.data);
            }, function(response) {

            });
        };

        // taking of table PlayersPlayoffSeason from database
        var getStatisticsPlayoff = function (id) {
            return $http({
                method : 'GET',
                url: SERVER + "get-playoff/?format=json&player_id=" + id

            }).then(function(response) {
                return new PlayoffSeasons(response.data);
            }, function(response) {

            });
        };


        return {
            getStatisticsRegular: getStatisticsRegular,
            getStatisticsPlayoff: getStatisticsPlayoff,
            getRegularSeasonAll: getRegularSeasonAll,
            getPlayoffSeasonAll: getPlayoffSeasonAll,
            getRegularSeason: getRegularSeason,
            getPlayoffSeason: getPlayoffSeason
        };
    }]);