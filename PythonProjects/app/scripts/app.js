'use strict';

/**
 * @ngdoc overview
 * @name pythonProjectsApp
 * @description
 * # pythonProjectsApp
 *
 * Main module of the application.
 */
angular
  .module('pythonProjectsApp', [
    'ngAnimate',
    'ngCookies',
    'ngResource',
    'ngRoute',
    'ngSanitize',
    'ngTouch'
  ])
  .config(function ($routeProvider) {
    $routeProvider
      .when('/main', {
        templateUrl: 'views/main.html',
        controller: 'MainCtrl',
        controllerAs: 'main'
      })
      .when('/factorial', {
        templateUrl: 'views/fact.html',
        controller: 'FactorialCtrl',
        controllerAs: 'factorials'
      })
      .when('/about', {
        templateUrl: 'views/about.html',
        controller: 'AboutCtrl',
        controllerAs: 'about'
      })
      .when('/music', {
        templateUrl: 'views/music.html',
        controller: 'MusicCtrl',
        controllerAs: 'music'
      })
      .when('/nba', {
          templateUrl: 'views/nba.html',
          controller: 'NBACtrl',
          controllerAs: 'nba'
        })
      .when('/nbaPlayersAll', {
          templateUrl: 'views/nba_players_all.html',
          controller: 'NBACtrl',
          controllerAs: 'nba'
        })
      .when('/nbaCareer', {
          templateUrl: 'views/nba_players_career.html',
          controller: 'NBACtrl',
          controllerAs: 'nba'
        })
      .when('/nbaAllStar', {
          templateUrl: 'views/nba_players_allstar.html',
          controller: 'NBACtrl',
          controllerAs: 'nba'
        })
      .otherwise({
        redirectTo: '/'
      });
  });
