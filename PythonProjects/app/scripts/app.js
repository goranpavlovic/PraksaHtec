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
      .when('/', {
        templateUrl: 'views/main.html',
        controller: 'MainCtrl',
        controllerAs: 'main'
      })
      .when('/', {
        templateUrl: 'views/main.html',
        controller: 'FactorialCtrl',
        controllerAs: 'factorials'
      })
      .when('/about', {
        templateUrl: 'views/about.html',
        controller: 'AboutCtrl',
        controllerAs: 'about'
      })
      .otherwise({
        redirectTo: '/'
      });
  });
