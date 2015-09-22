'use strict';

/**
 * @ngdoc function
 * @name pythonProjectsApp.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of the pythonProjectsApp
 */
angular.module('pythonProjectsApp')
  .controller('MainCtrl', [ 'userService', 'MathService', function (userService, MathService) {
      var self = this;

      self.context = userService.context;
      self.mathContext = MathService.MathContext;

      self.editMode = false;

      self.toggleEditMode = function(){
          self.editMode = !self.editMode;
          console.log(self.editMode);
      };

      self.editClicked = function(){
          self.toggleEditMode();
      };

      self.saveClicked = function(){
        self.toggleEditMode();
        self.context.user.saveUser();
      };

      self.operation = function(op) {
          MathService.operation(op);
      };

  }]);
