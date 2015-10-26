'use strict';

/**
 * @ngdoc function
 * @name webJsdApp.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of the webJsdApp
 */
angular.module('webJsdApp')
  .controller('MainCtrl', function () {

    var self = this;

    self.awesomeThings = [
      'HTML5 Boilerplate',
      'AngularJS',
      'Karma'
    ];

    self.test = "Some tekst..........";


    self.musicians = [{
        name: 'Ime1',
        surname: 'Ime 2',
        email: 'em1@htec.rs',
        albums: [{
          name: 'album1'
        },
        {
          name: 'album2'
        }
      ]
    },{
        name: 'Ime2',
        surname: 'Ime 2',
        email: 'em2@htec.rs',
        albums: [{
          name: 'aspfojewoiasdrfer'
        },
        {
          name: 'asojerwyewr'
        }
      ]
    }];

  });
