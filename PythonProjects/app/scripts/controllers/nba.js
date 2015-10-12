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
  .controller('NBACtrl', ['NBAService', function (NBAService) {
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
            NBAService.getPlayerAllInfo(player.player_id, mode)
                .then(function(response) {
                    self.playerInfo = response;
                });
        };

        /**
         *  Second form - Career table
         */


        /**
         *  Third form - All-Star table
         */

        self.playerMods = [
            'gt',
            'gte',
            'lt',
            'lte',
            'eq'
        ];

  }]);