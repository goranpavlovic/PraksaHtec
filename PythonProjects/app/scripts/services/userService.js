'use strict';
/**
 * Created by tehnika on 17-Sep-15.
 */

angular.module('pythonProjectsApp').service('userService', ["$http", "userFactory", function($http, userFactory){

    var self = this;

    self.context = { user: null };

    //self.user = userFactory.getUserById(5);

    userFactory.getUserById(5).then(function(user){

        console.log("---------user--------");
        console.log(user);

        self.context.user = user;
    });

}]);

