/**
 * Created by vladimir on 19.10.15..
 */
'use strict';

angular.module('pythonProjectsApp')
  .controller('NBATeamCtrl', [ 'NBATeamService', function (NBATeamService) {
        var self =this;

        /**
         *
         *  First Form for teams - ALL
         *
         * */

        /**
         *
         *  Second Form for teams - SEASON
         *
         * */
        // Table from database
        self.teamSeasonCollection = NBATeamService.teamSeasonCollection;
        // Show table
        self.tableFlag = false;
        self.isLoading = false;
        // Flags used in table sorting
        //self.orderFlags = NBATeamService.orderFlags;

        self.teamModes = ['gt', 'gte', 'eq', 'lte', 'lt'];

        self.nbaTeamQuery = {
            // Basic parameters
            team: '',
            year: '',
            league: '',
            points: '',
            rebounds: '',
            blocks: '',
            assists: '',
            steals: '',
            turnovers: '',
            // Modes for parameters
            selectedModePointsTS: '',
            selectedModeReboundsTS: '',
            selectedModeBlocksTS: '',
            selectedModeAssistsTS: '',
            selectedModeStealsTS: '',
            selectedModeTurnoversTS: '',
            // Sorting
            sortBy: '',
            sortReverse: ''
        };

        self.selectedNumOfItems = '';
        self.numItems = [ 5, 10, 20, 50 ];

        self.getTeamSeasonInfo = function () {
            //self.tableFlag = true;
            NBATeamService.getTeamSeasonInfo(self.nbaTeamQuery);
        };
        //
        //self.sort = function (column) {
        //    NBATeamService.getTeamSeasonInfoOrderBy(self.nbaTeamQuery, column, self.orderFlags);
        //};

        self.initialCallHappends = false;

        self.initialCall = function(){
            self.initialCallHappends = true;
            self.callServer();
        };

        self.tableState = null;

        self.callServer = function callServer(tableState) {

            console.log("--------- CALL SERVER -----------");
            if (self.tableState === null){
                console.log(tableState);
                self.tableState = tableState;
                return;
            }

            if (!self.initialCallHappends)
                return;

            self.tableFlag = true;
            console.log("--------- API CALL -----------");
            self.isLoading = true;

            var pagination = self.tableState.pagination;

            var start = pagination.start || 0;     // This is NOT the page number, but the index of item in the list that you want to use to display the table.
            var number = pagination.number || 10;  // Number of entries showed per page.

            // Getting of objects from tableState
            var sortBy = self.tableState.sort.predicate;
            var sortReverse = self.tableState.sort.reverse;

            self.nbaTeamQuery.sortBy = sortBy;
            self.nbaTeamQuery.sortReverse = sortReverse;

            NBATeamService.getPage(start, number, self.tableState, self.nbaTeamQuery).then(function (result) {
                console.log('---------RESULT--------');
                console.log(result);
                self.teamSeasonCollection = result;
                self.tableState.pagination.numberOfPages = 10;//set the number of pages so the pagination can update
                self.isLoading = false;
            });
        };


    } ]);