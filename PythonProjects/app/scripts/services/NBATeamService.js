/**
 * Created by vladimir on 19.10.15..
 */
'use strict';

angular.module('pythonProjectsApp')
  .service('NBATeamService', ['NBATeamSeasonFactory',
        function (NBATeamSeasonFactory) {
            var self = this;

            self.teamSeasonCollection = {
                teams : null
            };

            //self.orderFlags = {
            //
            //};
            
            self.getTeamSeasonInfo = function(query) {
                NBATeamSeasonFactory.getTeamSeasonInfo(query)
                    .then(function(data) {
                        self.teamSeasonCollection.teams = data.teams;
                    });
            };

            //self.getTeamSeasonInfoOrderBy = function(query, column, flags) {
            //    NBATeamSeasonFactory.getTeamSeasonInfo(query)
            //        .then(function(data) {
            //            self.teamSeasonCollection = data.teams;
            //        });
            //    self.orderFlags = NBATeamSeasonFactory.flags;
            //};

            self.getPage = function getPage(start, number, params, query) {

                //var deferred = $q.defer();

                //self.getTeamSeasonInfo(query);

                //var filtered = params.search.predicateObject ?
                //               $filter('filter')(self.teamSeasonCollection.teams,
                //                                 params.search.predicateObject) : self.teamSeasonCollection.teams;

                //if (params.sort.predicate) {
                //    filtered = $filter('orderBy')(filtered, params.sort.predicate, params.sort.reverse);
                //}

                //var result = filtered.slice(start, start + number);

                //$timeout(function () {
                //    //note, the server passes the information about the data set size
                //    deferred.resolve({
                //        data: result,
                //        numberOfPages: Math.ceil(filtered.length / number)
                //    });
                //}, 1500);

                console.log("---------GET PAGE SERVICE--------");

                //return filtered;

                //return deferred.promise;

                return NBATeamSeasonFactory.getTeamSeasonInfo(query)
                    .then(function(data) {
                        console.log("---------RESPONSE--------");
                        return data.teams;
                    });

            }

        } ]);