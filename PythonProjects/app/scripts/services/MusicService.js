/**
 * Created by vladimir on 21.9.15..
 */
'use strict';
/**
 * Created by tehnika on 21-Sep-15.
 */

angular.module('pythonProjectsApp').service('MusicService', ["$http", "musicFactory", function($http, musicFactory){
    var self  = this;

    self.musicContext = { musician : null };

    self.musicianContext = { musician : null };

    self.get_info = function (id) {
        //self.musicContext.musician = musicFactory.get_info();
        musicFactory.get_info(id).then(function(data){
            self.musicContext.musician = data;
            self.musicianContext.musician = data.getContent();
        });
    }



}]);