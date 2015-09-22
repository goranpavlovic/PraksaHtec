/**
 * Created by vladimir on 21.9.15..
 */
'use strict';
/**
 * Created by tehnika on 21-Sep-15.
 */

angular.module('pythonProjectsApp').service('FactorialService', ["$http", function($http){
    var self  = this;

    self.factContext = {
        number : 0,
        result : 0,
        operations : [
            {id : 1, name : 'SIMPLE'},
            {id : 2, name : 'DOUBLE'},
            {id : 3, name : 'QUAD'},
            {id : 4, name : 'SUPER'},
            {id : 5, name : 'HYPER'}
        ]
    };

    self.factorialsFunc = function (op) {
        switch (op) {
            case 1:
                self.simpleFactorial();
                break;
            case 2:
                self.doubleFactorial();
                break;
            case 3:
                self.quadrupleFactorial();
                break;
            case 4:
                self.superFactorial();
                break;
            case 5:
                self.hyperFactorial();
                break;
        }
    };

    function factorial(n) {
        if (n == 0)
            return 1;
        else
            return n * factorial(n-1);
    }

    self.simpleFactorial = function () {
        var n = self.factContext.number;
        if (n < 0) {
            self.factContext.result = "Number must be greater or equals with zero!";
        }
        else
            self.factContext.result = factorial(n);
    };

    self.doubleFactorial = function () {
        var n = self.factContext.number;
        var result = 1;
        if (n < 0) {
            self.factContext.result = "Number must be greater or equals with zero!";
        }
        else {
            while(n > 0) {
                result *= n;
                n -= 2;
            }
            self.factContext.result = result;
        }
    };

    self.quadrupleFactorial = function () {
        var n = self.factContext.number;
        if (n < 0) {
            self.factContext.result = "Number must be greater or equals with zero!"
        }
        else {
            var fact_2n = factorial(2*n);
            var fact_n = factorial(n);
            self.factContext.result = fact_2n / fact_n;
        }
    };

    self.superFactorial = function () {
        var n = self.factContext.number;
        var result = 1;
        if (n < 0) {
            self.factContext.result = "Number must be greater or equals with zero!";
        }
        else {
            while (n > 0) {
                result *= factorial(n);
                n -= 1;
            }
            self.factContext.result = result;
        }
    };

    self.hyperFactorial = function () {
        var n = self.factContext.number;
        var result = 1;
        if (n < 0) {
            self.factContext.result = "Number must be greater or equals with zero!";
        }
        else {
            while (n > 0) {
                result *= Math.pow(n, n);
                n -= 1;
            }
            self.factContext.result = result;
        }
    }

}]);