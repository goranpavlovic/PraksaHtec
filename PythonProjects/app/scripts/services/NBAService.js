'use strict';
/**
 * Created by vladimir on 1.10.15..
 */

angular.module('pythonProjectsApp')
    .service('NBAService', ["$http", "NBAFactory", "NBARegularFactory",
                            "NBAPlayersCareerFactory", "NBA_All_StarFactory",
        function ($http, NBAFactory, NBARegularFactory, NBAPlayersCareerFactory,
                  NBA_All_StarFactory)
        {
            var self = this;

            /**
             * Players All form
             *
             * */
            self.nbaContext = {
                player: null
            };

            self.getPlayersInfo = function (id, // Filtering players by id,
                                            first_name,  // by first name,
                                            last_name,   // by last name,
                                            position,    // by players position,
                                            first_season,    // when player have started career in NBA
                                            last_season)    // and his last season in NBA
            {
                return NBAFactory.getPlayersInfo(id, first_name, last_name, position,
                    first_season, last_season)
                    .then(function (data) {
                        //self.nbaContext.player = data.players;
                        return data.players;
                    });
            };

            self.seasonContext = {
                seasons: null
            };


            self.getPlayerAllInfo = function (id, statMode) {
                // If checked 'regular' radio button
                if (statMode === 'regular') {
                    return NBARegularFactory.getStatisticsRegular(id)
                        .then(function (data) {
                            self.seasonContext = data.seasons;
                            return data.seasons;
                        });
                }
                // If checked 'playoff' radio button
                if (statMode === 'playoff') {
                    return NBARegularFactory.getStatisticsPlayoff(id)
                        .then(function (data) {
                            self.seasonContext = data.seasons;
                            return data.seasons;
                        });
                }
            };

            //function putValuesInDataArray(valueX, valueY, dataArray) {
            //    // Checking length of arrays
            //    if (valueX.length != valueY.length)
            //        return false;
            //
            //    for (var i = 0; i < valueX.length; i++) {
            //        var pairs = [];
            //        pairs.push(valueX[i]);
            //        pairs.push(valueY[i]);
            //        dataArray.push(pairs);
            //    }
            //    return true;
            //}

            function setData(statMode) {

                console.log("--------- SET DATA ----------");
                console.log(statMode);

                var seasonArray = [];
                var seasonArray_b = [];
                for(var i = 0; i < self.seasonContext.length; i++){
                    var x, y, z;
                    if (statMode == 'both') {
                        x = self.seasonContext[i]['year'];
                        y = self.seasonContext[i]['off_rebounds'];
                        z = self.seasonContext[i]['def_rebounds'];
                        seasonArray.push([x, y]);
                        seasonArray_b.push([x, z]);
                    }
                    else if (statMode == 'all') {
                        x = self.seasonContext[i]['year'];
                        y = self.seasonContext[i]['rebounds'];
                        seasonArray.push([x, y]);
                    }
                    else if (statMode == 'offensive') {
                        x = self.seasonContext[i]['year'];
                        y = self.seasonContext[i]['off_rebounds'];
                        seasonArray.push([x, y]);
                    }
                    else if (statMode == 'defensive') {
                        x = self.seasonContext[i]['year'];
                        y = self.seasonContext[i]['def_rebounds'];
                        seasonArray.push([x, y]);
                    }
                    else {
                        x = self.seasonContext[i]['year'];
                        y = self.seasonContext[i][statMode];
                        seasonArray.push([x, y]);
                    }


                    //switch (statMode) {
                    //    case 'points':
                    //        x = self.seasonContext[i].year;
                    //        y = self.seasonContext[i].points;
                    //        //y = self.seasonContext[i][statMode];
                    //
                    //        array[i].'year'
                    //        seasonArray.push([x, y ]);
                    //        break;
                    //    case 'assists':
                    //        x = self.seasonContext[i].year;
                    //        y = self.seasonContext[i].assists;
                    //        seasonArray.push([x, y ]);
                    //        break;
                    //    case 'blocks':
                    //        x = self.seasonContext[i].year;
                    //        y = self.seasonContext[i].blocks;
                    //        seasonArray.push([x, y ]);
                    //        break;
                    //    case 'steals':
                    //        x = self.seasonContext[i].year;
                    //        y = self.seasonContext[i].steals;
                    //        seasonArray.push([x, y ]);
                    //        break;
                    //    case 'turnovers':
                    //        x = self.seasonContext[i].year;
                    //        y = self.seasonContext[i].turnovers;
                    //        seasonArray.push([x, y ]);
                    //        break;
                    //    case 'all':
                    //        x = self.seasonContext[i].year;
                    //        y = self.seasonContext[i].rebounds;
                    //        seasonArray.push([x, y ]);
                    //        break;
                    //    case 'offensive':
                    //        x = self.seasonContext[i].year;
                    //        y = self.seasonContext[i].off_rebounds;
                    //        seasonArray.push([x, y ]);
                    //        break;
                    //    case 'defensive':
                    //        x = self.seasonContext[i].year;
                    //        y = self.seasonContext[i].def_rebounds;
                    //        seasonArray.push([x, y]);
                    //        break;
                    //    case 'both':
                    //        x = self.seasonContext[i].year;
                    //        y = self.seasonContext[i].def_rebounds;
                    //        z = self.seasonContext[i].off_rebounds;
                    //        seasonArray.push([x, y]);
                    //        seasonArray_b.push([x, z]);
                    //        break;

                    //}
                }
                if (statMode == 'both')
                    return [seasonArray, seasonArray_b];
                else
                    return [seasonArray];
            }

            self.drawGraph = function (mode, name) {
                /*
                 *       Drawing graph by mode,
                 *       seasonContext contents all seasons for one player,
                 *       Playoff or Regular season, that depends of radio-button
                 *
                 *       By argument name we set plot title
                 *           1. PLAYOFF
                 *           2. REGULAR SEASON
                 *
                 * */


                $(function () {

                    //var data = [ ["January", 10], ["February", 8], ["March", 4], ["April", 13], ["May", 17], ["June", 9] ];
                    //var data1 = [ ["January", 15], ["February", 18], ["March", 14], ["April", 23], ["May", 27], ["June", 19] ];
                    //var data = [];

                    var data = setData(mode);
                    //putValuesInDataArray(coord.x, coord.y, data);

                    $.plot("#placeholder", data, {
                        series: {
                            bars: {
                                show: true,
                                barWidth: 0.6,
                                align: "center"
                            }
                        },
                        xaxis: {
                            mode: "categories",
                            tickLength: 0
                        }
                    });


                    // Add the Flot version string to the footer

                    // $("#footer").prepend("Flot " + $.plot.version + " &ndash; ");
                });
            };

            /**
             *
             * Players Career form
             *
             * */
            self.nbaCareerContext = {
                players: null
            };

            self.getPlayersInfoCareer = function (id, firstName, lastName,
                                                  points, rebounds, assists,
                                                  steals, blocks, turnovers,
                                                  pts_mode, reb_mode, ast_mode,
                                                  stl_mode, blk_mode, turn_mode) {
                NBAPlayersCareerFactory.getPlayersInfo(id, firstName, lastName,
                    points, rebounds, assists,
                    steals, blocks, turnovers,
                    pts_mode, reb_mode, ast_mode,
                    stl_mode, blk_mode, turn_mode)
                    .then(function (data) {
                        self.nbaCareerContext.players = data.players;
                    });
            };

            self.drawGraphCareer = function () {

            };

            /**
             *
             *  Players All-Star form
             *
             * */
            self.nbaAllStarContext = {
                players: null
            };

            self.orderFlags = {
                 all_star_year: true,
                 all_player: true,
                 first_name: true,
                 last_name: true,
                 conference: true,
                 minutes: true,
                 points: true,
                 off_rebounds: true,
                 def_rebounds: true,
                 rebounds: true,
                 assists: true,
                 steals: true,
                 blocks: true,
                 turnovers: true
            };

            self.getAllStarPlayersInfo = function (query) {
                NBA_All_StarFactory.getAllStarPlayersInfo(query)
                    .then(function (data) {
                        self.nbaAllStarContext.players = data.players;
                    });
            };

            self.getAllStarPlayersInfoOrder = function (query, order, flag) {
                NBA_All_StarFactory.getAllStarPlayersInfoOrder(query, order, flag)
                    .then(function (data) {
                        self.nbaAllStarContext.players = data.players;
                    });
                self.orderFlags = NBA_All_StarFactory.flags;
            };

            /**
             *
             *      ALL STAR FORM
             *
             * */
            self.getPage = function (start, number, params, query) {

                console.log("---------GET PAGE SERVICE--------");

                return NBA_All_StarFactory.getAllStarPlayersInfo(query)
                    .then(function(data) {
                            return data.players;
                        });
            };

        }]);