'use strict';
/**
 * Created by vladimir on 8.10.15..
 */
angular.module('pythonProjectsApp')
    .factory('NBA_All_StarFactory', ["$http", "SERVER", function ($http, SERVER) {

        function Players(response) {
            this.response = response;

            this.parse = function () {
                this.players = [];
                for (var i = 0; i < response.length; i++)
                    this.players.push(new Player(response[i]));
            };

            this.parse();
        }

        function Player(response) {
            this.response = response;

            this.parse = function () {
                this.all_star_year = response.all_star_year;
                this.all_player = response.all_player;
                this.first_name = response.first_name;
                this.last_name = response.last_name;
                this.conference = response.conference;
                this.minutes = response.minutes;
                this.points = response.points;
                this.off_rebounds = response.off_rebounds;
                this.def_rebounds = response.def_rebounds;
                this.rebounds = response.rebounds;
                this.assists = response.assists;
                this.steals = response.steals;
                this.blocks = response.blocks;
                this.turnovers = response.turnovers;
            };

            this.parse();
        }

        function getPlayers() {
            var playersResponse = {
                players: null
            };
            return new Players(playersResponse);
        }

        function getPlayer() {
            var playerResponse = {
                 all_star_year: 0,
                 all_player: '',
                 first_name: '',
                 last_name: '',
                 conference: '',
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

        function getAllStarPlayersInfo(query) {

            var player_id = query.id;
            var first_name = query.first;
            var last_name = query.last;
            var conference = query.conf;
            var year = query.year;
            var points = query.pts;
            var rebounds = query.reb;
            var assists = query.ast;
            var blocks = query.blk;

            var pts_mode = query.selectedModePointsAS;
            var reb_mode = query.selectedModeReboundsAS;
            var blk_mode = query.selectedModeBlocksAS;
            var ast_mode = query.selectedModeAssistsAS;

            var sortBy = query.sortBy;
            var sortReverse = query.sortReverse;

            //var prefix = query.prefix;
            //var prefixName;
            //
            //if (prefix)
            //    prefixName = Object.keys(prefix)[0];

            var queryURL = "get-allstar/?format=json";

            if (player_id)
                queryURL += "&player_id=" + player_id;

            if (first_name)
                queryURL += "&first_name=" + first_name;

            //if (prefix && prefixName == "first_name")
            //    queryURL += "&first_name=" + prefix[prefixName];

            if (last_name)
                queryURL += "&last_name=" + last_name;

            //if (prefix && prefixName == "last_name")
            //    queryURL += "&last_name=" + prefix[prefixName];

            if (conference)
                queryURL += "&conference=" + conference;

            if (year)
                queryURL += "&year=" + year;

            if (points) {
                if (pts_mode)
                    queryURL += "&points=" + points + "&pts_mode=" + pts_mode;
                else
                    alert("You must check mode for parameter points.");
            }

            if (rebounds) {
                if (reb_mode)
                    queryURL += "&rebounds=" + rebounds + "&reb_mode=" + reb_mode;
                else
                    alert("You must check mode for parameter rebounds.");
            }

            if (assists) {
                if (ast_mode)
                    queryURL += "&assists=" + assists + "&ast_mode=" + ast_mode;
                else
                    alert("You must check mode for parameter assists.");
            }

            if (blocks) {
                if (blk_mode)
                    queryURL += "&blocks=" + blocks + "&blk_mode=" + blk_mode;
                else
                    alert("You must check mode for parameter blocks.");
            }

            if (sortBy) {
                queryURL += "&order_by=" + [sortBy];
                if (sortReverse)
                    queryURL += "&order_mode=descending";
                else
                    queryURL += "&order_mode=ascending";
            }

            /*
            *   Searching for every object in the search list in the tableState
            *   object, when we get the key, with key name and value we make the query
            *
            * */
            var prefix = query.prefix;
            var prefixName;

            if (prefix)
                for (var i = 0; i < Object.keys(prefix).length; i++) {
                    prefixName = Object.keys(prefix)[i];
                    queryURL += "&" + prefixName + "=" + prefix[prefixName];
                }

            /*
            *   Pagination, here we pass number of page items and number of page
            * */
            var page = query.page;
            var pageSize = query.pageSize;

            if (page)
                if (pageSize)
                    queryURL += "&page=" + page + "&page_size=" + pageSize;
                else
                    alert('You must put number of items per page.');

            return $http({
                method: 'GET',
                url: SERVER + queryURL
            }).then(function(response) {
                return new Players(response.data);
            }, function(response) {
                alert("-------Error-------");
            });
        }

        var flags = {};

        function getAllStarPlayersInfoOrder(query, order, flag) {

            var player_id = query.id;
            var first_name = query.first;
            var last_name = query.last;
            var conference = query.conf;
            var year = query.year;
            var points = query.pts;
            var rebounds = query.reb;
            var assists = query.ast;
            var blocks = query.blk;

            var pts_mode = query.selectedModePointsAS;
            var reb_mode = query.selectedModeReboundsAS;
            var blk_mode = query.selectedModeBlocksAS;
            var ast_mode = query.selectedModeAssistsAS;

            var queryURL = "get-allstar/?format=json";

            if (flag[order]) {
                queryURL += "&order_by=" + order + "&order_mode=ascending";
                flag[order] = false;
            }
            else {
                queryURL += "&order_by=" + order + "&order_mode=descending";
                flag[order] = true;
            }

            if (player_id)
                queryURL += "&player_id=" + player_id;

            if (first_name)
                queryURL += "&first_name=" + first_name;

            if (last_name)
                queryURL += "&last_name=" + last_name;

            if (conference)
                queryURL += "&conference=" + conference;

            if (year)
                queryURL += "&year=" + year;

            if (points) {
                if (pts_mode)
                    queryURL += "&points=" + points + "&pts_mode=" + pts_mode;
                else
                    alert("You must check mode for parameter points.");
            }

            if (rebounds) {
                if (reb_mode)
                    queryURL += "&rebounds=" + rebounds + "&reb_mode=" + reb_mode;
                else
                    alert("You must check mode for parameter rebounds.");
            }

            if (assists) {
                if (ast_mode)
                    queryURL += "&assists=" + assists + "&ast_mode=" + ast_mode;
                else
                    alert("You must check mode for parameter assists.");
            }

            if (blocks) {
                if (blk_mode)
                    queryURL += "&blocks=" + blocks + "&blk_mode=" + blk_mode;
                else
                    alert("You must check mode for parameter blocks.");
            }

            flags = flag;

            return $http({
                method: 'GET',
                url: SERVER + queryURL
            }).then(function(response) {
                return new Players(response.data);
            }, function(response) {
                alert("-------Error-------");
            });
        }

        function getAllStarStatistics (id) {
            return $http({
                method: 'GET',
                url: SERVER + "get-allstar/?format=json&player_id=" + id +
                              "&order_by=all_star_year&order_mode=ascending"
            })
                .then(function(response) {
                    return new Players(response.data)
                }, function() {
                    alert("-------- Error --------");
                });
        }

        return {
            getPlayers: getPlayers,
            getPlayer: getPlayer,
            getAllStarPlayersInfo: getAllStarPlayersInfo,
            getAllStarPlayersInfoOrder: getAllStarPlayersInfoOrder,
            flags: flags,
            getAllStarStatistics: getAllStarStatistics
        };
    }]);