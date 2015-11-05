'use strict';
/**
 * Created by vladimir on 27.10.15..
 */
angular.module('nbaDirectives', [])
    .directive('nbaAllStarGraph', function() {
      //  Embedded function in html template for this directive
      var drawGraph = function ($scope, element) {

          // Auxiliary function for drawing
          function draw_graph(){

              var placeholder = element.find(".demo-placeholderAllStar");
              placeholder.empty();

              if (!$scope.ticks || $scope.ticks.length <= 0 || !$scope.data || $scope.data.length <= 0
                  || !$scope.title || $scope.title.length <= 0)
                  return 0;

                $.jqplot('placeholder', $scope.data, {
                    //title: {
                    //    text: $scope.title,
                    //    fontSize: '14pt',
                    //    show: true
                    //},
                    seriesDefaults: {
                        renderer:$.jqplot.BarRenderer,
                        pointLabels: { show: true }
                    },
                    //legend: {
                    //    show: true,
                    //    location: 'sw',
                    //    placement: 'outside',
                    //    marginLeft: "300px"
                    //},
                    axes: {
                        xaxis: {
                            renderer: $.jqplot.CategoryAxisRenderer,
                            ticks: $scope.ticks
                        }
                    }
                });

                $('#placeholder').bind('jqplotDataHighlight',
                    function (ev, seriesIndex, pointIndex, data) {
                        $('#info3').html('series: '+seriesIndex+', point: '+ pointIndex+', data: '+ data);
                    }
                );

          }

          // Directive attributes watching
          $scope.$watch('data', function (newValue, oldValue) {
                draw_graph();
          });
          $scope.$watch('ticks', function (newValue, oldValue) {
                draw_graph();
          });
          $scope.$watch('title', function (newValue, oldValue) {
                draw_graph();
          });
      };

      return {
        restrict: 'E',
        scope: {
            data: '=data',
            ticks: '=ticks',
            title: '=title'
        },
        templateUrl: 'views/nbaAllStarTemplate.html',
        link: drawGraph
      };
    });