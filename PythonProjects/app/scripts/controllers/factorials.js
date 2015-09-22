/**
 * Created by vladimir on 21.9.15..
 */
'use strict';

/**
 * @ngdoc function
 * @name pythonProjectsApp.controller:FactorialCtrl
 * @description
 * # FactorialCtrl
 * Controller of the pythonProjectsApp
 */
angular.module('pythonProjectsApp')
  .controller('FactorialCtrl', ['FactorialService', function (FactorialService) {
        var self = this;

        self.factContext = FactorialService.factContext

        self.factorialsFunc = function (op) {
              FactorialService.factorialsFunc(op);
        }
  }]);
