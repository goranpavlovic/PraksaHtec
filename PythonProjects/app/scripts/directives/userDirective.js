'use strict';
/**
 * Created by tehnika on 17-Sep-15.
 */


angular.module('pythonProjectsApp').directive('myUser', function() {
  return {
    restrict: 'E',
    scope: {
      user: '=user',
    },
    templateUrl: 'views/userTemplate.html',
    link: function($scope, $element) {


    }
  };
});