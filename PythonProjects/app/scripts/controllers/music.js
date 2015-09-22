/**
 * Created by vladimir on 21.9.15..
 */
'use strict';

/**
 * @ngdoc function
 * @name pythonProjectsApp.controller:MusicCtrl
 * @description
 * # MusicCtrl
 * Controller of the pythonProjectsApp
 */
angular.module('pythonProjectsApp')
  .controller('MusicCtrl', ['MusicService', function (MusicService) {
        var self = this;

        self.musicContext = MusicService.musicContext;

        self.get_info = function () {
            MusicService.get_info();
        }
  }]);