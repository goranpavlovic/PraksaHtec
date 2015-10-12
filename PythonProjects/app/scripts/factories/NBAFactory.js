'use strict';
/**
 * Created by vladimir on 1.10.15..
 */

angular.module('pythonProjectsApp')
    .factory('NBAFactory', ["$http", "SERVER", function($http, SERVER){

        // -- Class PlayersAll
        // Create list of players. In this list we put all
        // players which we get from database
        function PlayersAll(response) {
            var self = this;
            self.response = response;

            self.parse = function () {
                self.players = [];
                for (var i = 0; i < response.length; i++)
                    self.players.push(new Player(response[i]));
            };
            self.parse();
        }

        // -- Class Player
        // Create player with all characteristics from database
        function Player(response) {
            var self = this;
            self.response = response;

            self.parse = function () {
                self.player_id = response.player_id;
                self.first_name = response.first_name;
                self.last_name = response.last_name;
                self.position = response.position;
                self.first_season = response.first_season;
                self.last_season = response.last_season;
                self.height_feet = response.height_feet;
                self.height_inches = response.height_inches;
                self.weight = response.weight;
                self.college = response.college;
                self.birth_date = response.birth_date;
            };
            self.parse();
        }

        // getter for list of players
        function getPlayersAll() {
            var playersAllResponse = {
                players : []
            };
            return new PlayersAll(playersAllResponse);
        }

        // getter for player
        function getPlayer() {
            var playerResponse = {
                player_id : 0,
                first_name : '',
                last_name : '',
                position : '',
                first_season : 0,
                last_season : 0,
                height_feet : 0,
                height_inches : 0,
                weight : 0,
                college : 0,
                birth_date : null
            };
            return new Player(playerResponse);
        }

        // In this function is implemented getting of all rows(players) from
        // database from table Players. All filtering is implemented to the
        // back-end side, here we only pass parameters from web page to the queries.
        // And logically query execute to the back-end
        function getPlayersInfo(id, first_name, last_name,
                                       position, first_season, last_season)
        {
            var getQuery = "get-players/?format=json";
            if (id) {
                getQuery += ("&player_id=" + id);
            }
            if (first_name) {
                getQuery += ("&first_name=" + first_name);
            }
            if (last_name) {
                getQuery += ("&last_name=" + last_name);
            }
            if (position) {
                getQuery += ("&position=" + position);
            }
            if (first_season) {
                getQuery += ("&first_season=" + first_season);
            }
            if (last_season) {
                getQuery += ("&last_season=" + last_season);
            }
            return $http({
                method : 'GET',
                url: SERVER + getQuery

            }).then(function(response){
                return new PlayersAll(response.data);
            }, function(){
                alert("Error");
            });
        }

        // If we want to use some functions in services
        // we must return these functions to this way
        return {
            getPlayersInfo : getPlayersInfo,
            getPlayer : getPlayer,
            getPlayersAll : getPlayersAll
        }

}]);