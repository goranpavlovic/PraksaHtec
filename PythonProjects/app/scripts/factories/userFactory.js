'use strict';
/**
 * Created by tehnika on 17-Sep-15.
 */

angular.module('pythonProjectsApp').factory('userFactory', ["$http", "SERVER", function($http, SERVER){

    function User(jsonResponse){
        var userPtr = this;
        userPtr.response = jsonResponse;

        userPtr.validate = function(){

            userPtr.parseJsonString();
        };

        userPtr.parseJsonString = function(){
            userPtr.id = 10;
            userPtr.firstName = userPtr.response.firstName;
            userPtr.lastName = userPtr.response.lastName;
            userPtr.email = userPtr.response.email;
            userPtr.permissions = userPtr.response.permissions;
        };

        userPtr.saveUser = function(){

            return $http({
                method: 'POST',
                url: SERVER + "get-user/",
                headers: {
                    'Content-type': undefined
                },
                transformRequest: function(){
                    var formData = new FormData();
                    formData.append("id", userPtr.id);
                    formData.append("email", userPtr.email);
                    return formData;
                }
            }).then(function(response){
                alert("User successfully saved!");
            }, function(response){
                console.log("-----------error------------");
            });
        };

        userPtr.validate();
    }

    function getUser (){

        var apiResponse = {
            firstName: 'John',
            lastName: 'Doe',
            email: 'john.doe@gmail.com',
            permissions: ['can_add_record', 'can_edit_record', 'can_delete_record']
        };

        return new User(apiResponse);
    }

    function getUserById(id){
        return $http({
            method: 'GET',
            url: SERVER + "get-user/?format=json&id=" + id,
        }).then(function(response){

            return new User(response.data);
        }, function(response){
            console.log("-----------error------------");
        });
    }


    return {
        getUser: getUser,
        getUserById: getUserById
    }

}]);

