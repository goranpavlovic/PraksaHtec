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
        'ngTouch',
        'angular-flot',
        'smart-table',
        'nbaFilters',
        'nbaDirectives'
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
      .when('/nba/all', {
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
      .when('/nbaTeamAll', {
          templateUrl: 'views/nba_team_all.html',
          controller: 'NBATeamCtrl',
          controllerAs: 'nbaTeam'
        })
      .when('/nbaTeamSeason', {
          templateUrl: 'views/nba_team_season.html',
          controller: 'NBATeamCtrl',
          controllerAs: 'nbaTeam'
        })
      .when('/nbaCoachAll', {
          templateUrl: 'views/nba_coach_all.html',
          controller: 'NBACtrl',
          controllerAs: 'nba'
        })
      .when('/nbaCoachCareer', {
          templateUrl: 'views/nba_coach_career.html',
          controller: 'NBACtrl',
          controllerAs: 'nba'
        })
      .otherwise({
        redirectTo: '/'
      });
  });

