'use strict';
/**
 * Created by vladimir on 12.10.15..
 */

angular.module('pythonProjectsApp')
    .factory('NBAPlayersCareerFactory', ["$http", "SERVER", function($http, SERVER){

    function Players(response) {
        this.response = response;

        this.parse = function () {
            this.players = [];
            for (var i = 0; i < response.length; i++)
                this.players.push(new Player(response[i]))
        };

        this.parse();
    }

    function Player(response) {
        this.response = response;

        this.parse = function () {
            this.player_id = response.player_id;
            this.first_name = response.first_name;
            this.last_name = response.last_name;
            this.games_played = response.games_played;
            this.minutes = response.minutes;
            this.off_rebounds = response.off_rebounds;
            this.def_rebounds = response.def_rebounds;
            this.points = response.points;
            this.rebounds = response.rebounds;
            this.assists = response.assists;
            this.blocks = response.blocks;
            this.steals = response.steals;
            this.turnovers = response.turnovers;
        };

        this.parse();
    }

    // getter for all players
    function getPlayers() {
        var playersResponse = {
            players: null
        };

        return new Players(playersResponse);
    }

    // getter for single player
    function getPlayer() {
        var playerResponse = {
            player_id: 0,
            first_name: '',
            last_name: '',
            games_played: '',
            minutes: 0,
            points: 0,
            off_rebounds: 0,
            def_rebounds: 0,
            rebounds: 0,
            assists: 0,
            steals: 0,
            blocks: 0,
            turnovers: 0
        };

        return new Player(playerResponse);
    }

    function getPlayersInfo(id, firstName, lastName,
                            points, rebounds, assists,
                            steals, blocks, turnovers,
                            pts_mode, reb_mode, ast_mode,   // Modes,
                            stl_mode, blk_mode, turn_mode)  // these six parameters
    {
        var urlRequest = "get-career/?format=json";

        if (id)
            urlRequest += "&player_id=" + id;

        if (firstName)
            urlRequest += "&first_name=" + firstName;

        if (lastName)
            urlRequest += "&last_name=" + lastName;

        if (points) {
            if (pts_mode)
                urlRequest += "&points=" + points + "&pts_mode=" + pts_mode;
            else
                alert("You must check mode for parameter points.");
        }

        if (rebounds) {
            if (reb_mode)
                urlRequest += "&rebounds=" + rebounds + "&reb_mode=" + reb_mode;
            else
                alert("You must check mode for parameter rebounds.");
        }

        if (assists) {
            if (ast_mode)
                urlRequest += "&assists=" + assists + "&ast_mode=" + ast_mode;
            else
                alert("You must check mode for parameter assists.");
        }

        if (steals) {
            if (stl_mode)
                urlRequest += "&steals=" + steals + "&stl_mode=" + stl_mode;
            else
                alert("You must check mode for parameter steals.");
        }

        if (blocks) {
            if (blk_mode)
                urlRequest += "&blocks=" + blocks + "&blk_mode=" + blk_mode;
            else
                alert("You must check mode for parameter blocks.");
        }

        if (turnovers) {
            if (turn_mode)
                urlRequest += "&turnovers=" + turnovers + "&turn_mode=" + turn_mode;
            else
                alert("You must check mode for parameter turnovers.");
        }

        return $http({
            method: 'GET',
            url: SERVER + urlRequest
        })
        .then(function(response) {
            return new Players(response.data)
        }, function(response) {
            alert("Error");
        });
    }

    return {
        getPlayers: getPlayers,
        getPlayer: getPlayer,
        getPlayersInfo: getPlayersInfo
    };
}]);