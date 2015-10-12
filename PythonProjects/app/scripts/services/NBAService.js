'use strict';
/**
 * Created by vladimir on 1.10.15..
 */

angular.module('pythonProjectsApp')
    .service('NBAService', ["$http", "NBAFactory", "NBARegularFactory", function($http, NBAFactory, NBARegularFactory){
        var self = this;

        self.nbaContext = {
            player : null
        };

        self.getPlayersInfo = function(id, // Filtering players by id,
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
            seasons : null
        };

        self.getPlayerAllInfo = function (id, statMode) {
            // If checked regular radio button
            if (statMode === 'regular') {
                return NBARegularFactory.getStatisticsRegular(id)
                    .then(function(data) {
                        self.seasonContext = data.seasons;
                        return data.seasons;
                    });
            }
            // If checked playoff radio button
            if (statMode === 'playoff') {
                return NBARegularFactory.getStatisticsPlayoff(id)
                    .then(function(data) {
                        self.seasonContext = data.seasons;
                        return data.seasons;
                    });
            }
        };

    }]);