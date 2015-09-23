/**
 * Created by vladimir on 21.9.15..
 */
'use strict';
/**
 * Created by tehnika on 17-Sep-15.
 */

angular.module('pythonProjectsApp')
    .factory('musicFactory', ["$http", "SERVER", function($http, SERVER){

        function Song(response){

        }


        function Musician(response) {
            var self = this;
            self.response = response;

            self.parse = function () {
                self.id = response.id;
                self.first = response.first;
                self.last = response.last;
                /*
                self.songs = [];
                for item in songs
                    songs.append(new Song())
                    */
            };
            self.parse();
        }

        function getMusician() {
            var response = {
                id : 0,
                first : '',
                last : ''
            };

            return new Musician(response);
        }

        function get_info(id) {
            return $http({
                method : 'GET',
                url: SERVER + "get-musician/?format=json&id=" + id
            }).then(function(response){
                alert("----- GO -----");
                return new Musician(response);
            }, function(){
                alert("Error");
            })
        }

        return {
            getMusician : getMusician,
            get_info : get_info
        }
}]);