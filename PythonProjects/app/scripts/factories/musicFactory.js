/**
 * Created by vladimir on 21.9.15..
 */
'use strict';
/**
 * Created by tehnika on 17-Sep-15.
 */

angular.module('pythonProjectsApp')
    .factory('musicFactory', ["$http", "SERVER", function($http, SERVER){

        function Album(response) {
            var self = this;
            self.response = response;

            self.parse = function () {
                //console.log("------------Album constructor ---------");
                self.id = response.id;
                self.artist = response.artist;
                self.name = response.name;
                self.release_date = response.release_date;
                self.num_stars = response.num_stars;

                self.production_house = new ProductionHouse(response.production_house);
                //for (var i = 0; i < response.production_house.length; i++)
                //    self.production_house.push(new ProductionHouse(response.production_house[i]));

                self.songs = [];
                for (var j = 0; j < response.songs.length; j++)
                    self.songs.push(new Song(response.songs[j]));
                self.duration_of_album = response.duration_of_album;
                self.num_of_songs = response.num_of_songs['id__count'];
                //console.log(self);
            };
            self.parse();
        }

        function Song(response){
            var self = this;
            self.response = response;

            self.parse = function () {
                self.id = response.id;
                self.name = response.name;
                self.duration = response.duration;
            };
            self.parse();
        }

        function ProductionHouse(response) {
            var self = this;
            self.response = response;

            self.parse = function () {
                self.id = response.id;
                self.name = response.name;
                self.director = response.director;
                self.founded = response.founded;
                self.budget = response.budget;
            };
            self.parse();
        }

        function Musician(response) {
            var self = this;
            self.response = response;

            self.parse = function () {
                self.id = response.id;
                self.first = response.first_name;
                self.last = response.last_name;
                self.instrument = response.instrument;
                self.age = response.age;
                self.country = response.country;
                //console.log("---------------Albums creation------------");
                //console.log(response.albums);
                self.albums = [];
                for (var i = 0; i < response.albums.length; i++)
                    self.albums.push(new Album(response.albums[i]));

            };
            self.parse();
        }

        function getMusician() {
            var response = {
                id : 0,
                first_name : '',
                last_name : '',
                instrument : '',
                age : 0,
                country : '',
                albums : []
            };

            return new Musician(response);
        }

        function getAlbum() {
            var albumResponse = {
                id : 0,
                artist : '',
                name : '',
                release_date : null,
                num_stars : 0,
                production_house : null,
                songs : [],
                duration_of_album : null,
                num_of_songs : 0
            };
            return new Album(albumResponse);
        }

        function getSong() {
            var songResponse = {
                id : 0,
                name : '',
                duration : null
            };

            return new Song(songResponse);
        }

        function getProductionHouse() {
            var phResponse = {
                id : 0,
                name : '',
                director : '',
                founded : 0,
                budget : 0
            };

            return new ProductionHouse(phResponse);
        }

        function get_info(id) {
            return $http({
                method : 'GET',
                url: SERVER + "get-musician/?format=json&id=" + id
                //transformResponse:
            }).then(function(response){
                //alert("----- GO -----");
                return new Musician(response.data);
            }, function(){
                alert("Error");
            });
        }

        function set_info(musician) {
            return $http({
                method : 'POST',
                url : SERVER + 'get-musician/',
                headers : {
                    'Content-type' : undefined  // Sta ovo predstavlja, zasto se stavlja ?????
                },
                transformRequest: function(){
                    var formData = new FormData();
                    formData.append("id", musician.id);
                    formData.append("first_name", musician.first);
                    formData.append("last_name", musician.last);
                    formData.append("instrument", musician.instrument);
                    formData.append("age", musician.age);
                    formData.append("country", musician.country);
                    return formData;
                }
            }).then(function (response) {

            }, function (response) {

            });
        }

        return {
            getMusician : getMusician,
            getAlbum : getAlbum,
            getSong : getSong,
            getProductionHouse : getProductionHouse,
            get_info : get_info,
            set_info : set_info
        }
}]);