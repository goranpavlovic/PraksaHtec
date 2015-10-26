'use strict';
/**
 * Created by vladimir on 13.10.15..
 */

/*
angular.module('pythonProjectsApp').directive('nbaGraph', function() {
  return {
    restrict: 'E',
    scope: {
        player: '=player'
    },
    //templateUrl: 'views/nbaCareerTemplate.html',
    template : 'First Name: {{ player.first_name }} Last Name: {{ player.last_name }}'
    //link: function($scope, $element) {
    //
    //
    //}
  };
});
*/

angular.module('pythonProjectsApp')
    .directive('nbaGraph', function() {
      return {
        restrict: 'E',
        scope: {
            player: '=player',
            statistics: '=statistics',
            name: '=name'
        },

        templateUrl: 'views/nbaCareerTemplate.html'
        //link: function(scope) {
        //    $(function() {
        //
        //        var data = [ ["January", 10], ["February", 8], ["March", 4], ["April", 13], ["May", 17], ["June", 9] ];
        //
        //        $.plot("#placeholder", [ data ], {
        //            series: {
        //                bars: {
        //                    show: true,
        //                    barWidth: 0.6,
        //                    align: "center"
        //                }
        //            },
        //            xaxis: {
        //                mode: "categories",
        //                tickLength: 0
        //            }
        //        });
        //
        //        // Add the Flot version string to the footer
        //
        //       // $("#footer").prepend("Flot " + $.plot.version + " &ndash; ");
        //    });
        //}
      };
    });