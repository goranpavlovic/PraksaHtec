'use strict';

/**
 * @ngdoc overview
 * @name webJsdApp
 * @description
 * # webJsdApp
 *
 * Main module of the application.
 */
angular
  .module('webJsdApp', [
    'ngAnimate',
    'ngAria',
    'ngCookies',
    'ngMessages',
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
      .when('/about', {
        templateUrl: 'views/about.html',
        controller: 'AboutCtrl',
        controllerAs: 'about'
      })
      .when('/moja_ruta', {
        templateUrl: 'views/mojaruta.html',
        controller: 'MojaRutaCtrl',
        controllerAs: 'mojaruta'
      })
        .when('/practice_2', {
        templateUrl: 'views/practice_2.html',
        controller: 'MojaRutaCtrl',
        controllerAs: 'Practice'
      })
      .otherwise({
        redirectTo: '/'
      });
  });
