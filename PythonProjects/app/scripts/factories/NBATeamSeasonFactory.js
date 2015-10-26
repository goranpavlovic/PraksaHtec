/**
 * Created by vladimir on 19.10.15..
 */
'use strict';

angular.module('pythonProjectsApp')
    .factory('NBATeamSeasonFactory', ["$http", "SERVER",
        function($http, SERVER){

            //   Class for all teams, all table TEAMS
            function Teams(response) {
                this.response = response;

                this.parse = function () {
                    this.teams = [];
                    for (var i = 0; i < response.length; i++)
                        this.teams.push(new Team(response[i]));
                };

                this.parse();
            }

            //  Class that makes exactly one team (one row of entity/table TEAM)
            function Team(response) {
                this.response = response;

                this.parse = function () {
                    this.team = response.team;
                    this.year = response.year;
                    this.league = response.league;
                    this.o_fgm = response.o_fgm;
                    this.o_fga = response.o_fga;
                    this.o_ftm = response.o_ftm;
                    this.o_fta = response.o_fta;
                    this.o_oreb = response.o_oreb;
                    this.o_dreb = response.o_dreb;
                    this.o_reb = response.o_reb;
                    this.o_asts = response.o_asts;
                    this.o_pf = response.o_pf;
                    this.o_stl = response.o_stl;
                    this.o_to = response.o_to;
                    this.o_blk = response.o_blk;
                    this.o_3pm = response.o_3pm;
                    this.o_3pa = response.o_3pa;
                    this.o_pts = response.o_pts;
                    this.pace = response.pace;
                    this.won = response.won;
                    this.lost = response.lost;
                };

                this.parse();
            }

            //  getter for exactly the one team
            function getTeam() {
                var teamResponse = {
                    team: '',
                    year: 0,
                    league: '',
                    o_fgm: 0,
                    o_fga: 0,
                    o_ftm: 0,
                    o_fta: 0,
                    o_oreb: 0,
                    o_dreb: 0,
                    o_reb: 0,
                    o_asts: 0,
                    o_pf: 0,
                    o_stl: 0,
                    o_to: 0,
                    o_blk: 0,
                    o_3pm: 0,
                    o_3pa: 0,
                    o_pts: 0,
                    pace: 0,
                    won: 0,
                    lost: 0
                };

                return new Team(teamResponse);
            }

            //  getter for the all teams
            function getTeamAll() {
                var teamsResponse = {
                    teams: null
                };

                return new Teams(teamsResponse);
            }

            function getTeamSeasonInfo(query) {
                var team = query.team;
                var year = query.year;
                var league = query.league;
                var points = query.points;
                var rebounds = query.rebounds;
                var assists = query.assists;
                var steals = query.steals;
                var blocks = query.blocks;
                var turnovers = query.turnovers;

                var pointsMode = query.selectedModePointsTS;
                var reboundsMode = query.selectedModeReboundsTS;
                var assistsMode = query.selectedModeAssistsTS;
                var stealsMode = query.selectedModeStealsTS;
                var blocksMode = query.selectedModeBlocksTS;
                var turnMode = query.selectedModeTurnoversTS;

                var sortBy = query.sortBy;
                var sortReverse = query.sortReverse;

                var urlQuery = "get-team-season/?format=json";

                if (team)
                    urlQuery += "&team=" + team;

                if (year)
                    urlQuery += "&year=" + year;

                if (league)
                    urlQuery += "&league=" + league;

                if (points)
                    if (pointsMode)
                        urlQuery += "&points=" + points + "&pts_mode=" + pointsMode;

                if (rebounds)
                    if (reboundsMode)
                        urlQuery += "&rebounds=" + rebounds + "&reb_mode=" + reboundsMode;

                if (blocks)
                    if (blocksMode)
                        urlQuery += "&blocks=" + blocks + "&blk_mode=" + blocksMode;

                if (assists)
                    if (assistsMode)
                        urlQuery += "&assists=" + assists + "&ast_mode=" + assistsMode;

                if (steals)
                    if (stealsMode)
                        urlQuery += "&steals=" + steals + "&stl_mode=" + stealsMode;

                if (turnovers)
                    if (turnMode)
                        urlQuery += "&turnovers=" + turnovers + "&turn_mode=" + turnMode;

                if (sortBy) {
                    urlQuery += "&order_by=" + [sortBy];
                    if (sortReverse)
                        urlQuery += "&order_mode=descending";
                    else
                        urlQuery += "&order_mode=ascending";
                }

                return $http({
                    method: 'GET',
                    url: SERVER + urlQuery
                }).then(function(response) {
                    return new Teams(response.data);
                }, function(response) {
                    alert("-------- Error -------");
                });
            }

            //var flags;
            //
            //function getTeamSeasonInfoOrderBy(query, column, flags) {
            //    var team = query.team;
            //    var year = query.year;
            //    var league = query.league;
            //    var points = query.points;
            //    var rebounds = query.rebounds;
            //    var assists = query.assists;
            //    var steals = query.steals;
            //    var blocks = query.blocks;
            //    var turnovers = query.turnovers;
            //
            //    var pointsMode = query.selectedModePointsTS;
            //    var reboundsMode = query.selectedModeReboundsTS;
            //    var assistsMode = query.selectedModeAssistsTS;
            //    var stealsMode = query.selectedModeStealsTS;
            //    var blocksMode = query.selectedModeBlocksTS;
            //    var turnMode = query.selectedModeTurnoversTS;
            //
            //
            //
            //    return $http({
            //        method: 'GET',
            //        url: SERVER + urlQuery
            //    }).then(function(response) {
            //        return new Teams(response.data)
            //    }, function(response) {
            //        alert("-------- Error -------");
            //    });
            //}

            return {
                getTeamSeasonInfo: getTeamSeasonInfo,
                //getTeamSeasonInfoOrderBy: getTeamSeasonInfoOrderBy,
                getTeamAll: getTeamAll,
                getTeam: getTeam
                //flags: flags
            }

        } ]);