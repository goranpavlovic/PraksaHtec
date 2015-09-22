/**
 * Created by vladimir on 21.9.15..
 */
'use strict';
/**
 * Created by tehnika on 21-Sep-15.
 */

angular.module('pythonProjectsApp').service('MusicService', ["$http", "musicFactory", function($http, musicFactory){
    var self  = this;

    self.musicContext = { musician: null};

    self.get_info = function () {
        self.musicContext.musician = musicFactory.get_info();
    }



}]);