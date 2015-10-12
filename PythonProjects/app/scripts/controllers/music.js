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

        var editMode = false;

        self.musicQuery = {
            id: ''
        };

        self.musicContext = MusicService.musicContext;

        //self.output = MusicService.musicianContext;

        self.get_info = function () {
            MusicService.get_info(self.musicQuery.id);
        };

        self.set_info = function () {
            MusicService.set_info(self.musicContext.musician);
            self.editMode = false;
        };

        self.saveSong = function (song) {

        };

        self.setEditMode = function () {
            self.editMode = true;
        };

        self.save_info = function () {
            self.set_info();
            //self.get_info();
        }
  }]);