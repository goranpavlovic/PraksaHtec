/**
 * Created by vladimir on 1.10.15..
 */
'use strict';

/**
 * @ngdoc function
 * @name pythonProjectsApp.controller:NBACtrl
 * @description
 * # NBACtrl
 * Controller of the pythonProjectsApp
 */
angular.module('pythonProjectsApp')
  .controller('NBACtrl', [ 'NBAService', function (NBAService) {
        var self = this;
        /**
         *  For the first form, for all players we use structure nbaQuery
         *
         *  Here, we use for every form new structure, because in that way
         *  we have more clear code
         *
         *  For example :
         *      nbaQuery  = {
         *          id : JORDMI01,
                    first_name : Michael,
                    last_name : Jordan,
                    position : G,
                    first_season : 1984,
                    last_season : 2002
         *      }
         */
        self.nbaQuery = {
          id : '',
          first_name : '',
          last_name : '',
          position : '',
          first_season : '',
          last_season : ''
        };

        self.nbaContext = NBAService.nbaContext;

        self.getPlayersInfo = function() {
            self.showResult = false;
            self.showPlayer = false;
            NBAService.getPlayersInfo(self.nbaQuery.id,
                                      self.nbaQuery.first_name,
                                      self.nbaQuery.last_name,
                                      self.nbaQuery.position,
                                      self.nbaQuery.first_season,
                                      self.nbaQuery.last_season)
                .then(function (players) {
                    self.showResult = true;
                    self.players = players;
                });
        };

        /*
        *   Here, we get player by id and the mode
        *   Mode is radio button, and can be:
        *       1. Regular Season - data take from the table PlayersRegularSeason
        *       2. Playoff - data take from the table PlayersPlayoff
        *
        * */

        self.player = null;
        self.statMode = 'playoff';

        self.seasonContext = NBAService.seasonContext;

        //self.getPlayersAllInfo = function () {
        //    NBAService.getPlayerAllInfo(self.playerID, self.statMode);
        //};

        self.setPlayer = function(player) {
            self.showPlayer = true;
            self.player = player;
            self.getInfoForMode(player, self.statMode);
        };

        self.getInfoForMode = function(player, mode) {

            console.log("--------- INFO FOR MODE ---------");
            console.log(mode);
            NBAService.getPlayerAllInfo(player.player_id, mode)
                .then(function(response) {
                    self.playerInfo = response;
                    self.reboundOrDraw(mode);
                });
        };

        /*
        *
        *   Graph/chart for individual statistic for player
        *   1. ngOptions - nbaPlayerStatistics(Points, Rebounds, Blocks...)
        *   2. ngOptions - nbaPlayerReboundsStatistics
        *
        *   1. ngModel - for all
        *   2. ngModel - for rebounds
        *
        * */
        self.nbaPlayerStatistics = ['points', 'rebounds', 'assists', 'blocks', 'steals', 'turnovers'];
        self.nbaPlayerReboundsStatistics = ['all', 'offensive', 'defensive', 'both'];
        self.selectedAll = '';
        self.selectedRebounds = '';
        self.selectedStat = '';
        self.reboundsFlag = false;

        self.setReboundsMode = function () {
            return self.reboundsFlag = (self.selectedAll == 'rebounds');
        };

        // Graph
        self.drawGraph = function () {
            //console.log("---------draw graph method-------")
            if (self.setReboundsMode()) {
                self.selectedStat = self.selectedRebounds;
                //NBAService.drawGraph();
            }
            else {
                self.selectedStat = self.selectedAll;
                //NBAService.drawGraph();
            }
            NBAService.drawGraph(self.selectedStat, self.statMode);
        };

        self.reboundOrDraw = function (mode) {

            console.log("---- REBOUND OR DRAW -----");
            console.log(mode);
            console.log(self.statMode);
            // If mode equals rebounds we make new ngOptions
            // to draw statistics for the rebounds (all, offensive, ...)
            // and draw for all
            if (mode == 'rebounds') {
                self.setReboundsMode();
                self.selectedStat = 'all';
                self.drawGraph(self.selectedStat, self.statMode);
            }

            // In this case, we draw the graph(chart)
            else {
                self.drawGraph(self.selectedStat, self.statMode);
            }
        };

        self.tableAndGraph = function (player, mode) {
            console.log("--------- TABLE AND GRAPH ---------");
            console.log(mode);
            console.log(self.statMode);
            self.getInfoForMode(player, mode);
        };

        // Modes if we have filtering by points, rebounds, ...
        // Second and third form
        self.playerModes = [ 'gt', 'gte', 'lt', 'lte', 'eq' ];

        /**
         *  Second form - Career table
         */
        self.nbaCareerQuery = {
            // Search parameters
            id: '',
            firstName: '',
            lastName: '',
            points: '',
            rebounds: '',
            assists: '',
            steals: '',
            blocks: '',
            turnovers: '',
            selectedModePointsPC: '',
            selectedModeReboundsPC: '',
            selectedModeAssistsPC: '',
            selectedModeBlocksPC: '',
            selectedModeStealsPC: '',
            selectedModeTurnoversPC: ''

        };

        self.nbaCareerContext = NBAService.nbaCareerContext;

        // Flag to show table career statistics for players
        self.playerCareer = false;

        self.getPlayersInfoCareer = function () {
            self.playerCareer = true;

            NBAService.getPlayersInfoCareer
            (self.nbaCareerQuery.id, self.nbaCareerQuery.firstName, self.nbaCareerQuery.lastName,
             self.nbaCareerQuery.points, self.nbaCareerQuery.rebounds, self.nbaCareerQuery.assists,
             self.nbaCareerQuery.steals, self.nbaCareerQuery.blocks, self.nbaCareerQuery.turnovers,
             self.nbaCareerQuery.selectedModePointsPC, self.nbaCareerQuery.selectedModeReboundsPC,
                self.nbaCareerQuery.selectedModeAssistsPC,
                self.nbaCareerQuery.selectedModeStealsPC, self.nbaCareerQuery.selectedModeBlocksPC,
                self.nbaCareerQuery.selectedModeTurnoversPC
            );

            //self.playerCareer = false;
        };

        /**
         *  Third form - All-Star table
         *  Form of nbaAllStarContext:
         *
         *      [
                  {
                    "all_star_year": 2007,
                    "all_player": "allenra02 ",
                    "first_name": "Ray",
                    "last_name": "Allen",
                    "conference": "East",
                    "minutes": 19,
                    "points": 28,
                    "off_rebounds": 2,
                    "def_rebounds": 0,
                    "rebounds": 2,
                    "assists": 1,
                    "steals": 2,
                    "blocks": 0,
                    "turnovers": 0
                  }
                ]
         *
         */
        self.nbaAllStarContext = NBAService.nbaAllStarContext;

        self.nbaAllStarQuery = {
            id: '',
            first: '',
            last: '',
            conf:'',
            year: '',
            pts: '',
            reb: '',
            blk: '',
            ast: '',
            selectedModePointsAS: '',
            selectedModeReboundsAS: '',
            selectedModeAssistsAS: '',
            selectedModeBlocksAS: '',
        //    Sorting
            sortBy: '',
            sortReverse: '',
        //    Searching
            prefix: null

        };

        self.allStarTable = false;

        self.orderFlags = NBAService.orderFlags;

        self.playerAllStarModes = [ 'gt', 'gte', 'lt', 'lte', 'eq', 'between'];

        self.getAllStarPlayersInfo = function () {
            self.allStarTable = true;
            NBAService.getAllStarPlayersInfo(self.nbaAllStarQuery);
        };

        self.tableState = null;

        self.callServerAllStar = function callServerAllStar(tableState) {
            console.log("-------- ENTER CALL SERVER ALL STAR --------");
            if (self.tableState === null){
                console.log("-------- TABLE STATE IF --------");
                console.log(tableState);
                self.tableState = tableState;
                return;
            }

            self.allStarTable = true;

            var pagination = self.tableState.pagination;

            var start = pagination.start || 0;     // This is NOT the page number, but the index of item in the list that you want to use to display the table.
            var number = pagination.number || 10;  // Number of entries showed per page.

            var sortBy = self.tableState.sort.predicate;
            var sortReverse = self.tableState.sort.reverse;
            //var searchFirstName;
            //var searchLastName;

            //if (self.tableState.search.predicateObject == 'first_name') {
            //    searchFirstName = self.tableState.search.predicateObject;
            //    self.nbaTeamQuery.first_name = searchFirstName;
            //}
            //
            //if (self.tableState.search.predicateObject == 'last_name') {
            //    searchLastName = self.tableState.search.predicateObject;
            //    self.nbaTeamQuery.last_name = searchLastName;
            //}
            var prefix = self.tableState.search.predicateObject;

            self.nbaAllStarQuery.sortBy = sortBy;
            self.nbaAllStarQuery.sortReverse = sortReverse;
            self.nbaAllStarQuery.prefix = prefix;

            NBAService.getPage(start, number, self.tableState, self.nbaAllStarQuery)
                .then(function (result) {
                    self.nbaAllStarContext = result;
                    self.tableState.pagination.numberOfPages = 10;//set the number of pages so the pagination can update
                });
        };

        //self.sort = function (order) {
        //    NBAService.getAllStarPlayersInfoOrder(self.nbaAllStarQuery, order, self.orderFlags);
        //};

        self.myData = [];
        self.myChartOptions = {};

        self.drawFlags = {
            minutes: false,
            points: false,
            rebounds: false,
            offensive: false,
            defensive: false,
            assists: false,
            blocks: false,
            steals:false,
            turnovers: false
        };

        //self.graphTypes

        self.drawGraphAllStar = function () {

        };

    }]);