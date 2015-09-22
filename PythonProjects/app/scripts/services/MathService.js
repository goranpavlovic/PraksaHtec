'use strict';
/**
 * Created by tehnika on 17-Sep-15.
 */

angular.module('pythonProjectsApp').service('MathService', ["$http", function($http){

    var self = this;

    self.MathContext = { firstNum: 0,
                         secondNum: 0,
                         result: 0,
                        operations: [{op_id: 1, op_name: 'ADD'}
                            , {op_id: 2, op_name: 'SUB' }
                            , {op_id: 3, op_name: 'MUL' }
                            , {op_id: 4, op_name: 'DIV' } ] };


   self.operation = function(op) {
        var x = self.MathContext.firstNum - 0;
        var y = self.MathContext.secondNum - 0;
        var z;

        switch (op) {
            case 1: z = x + y; break;
            case 2: z = x - y; break;
            case 3: z = x * y; break;
            case 4:
                if (y == 0) {
                    self.MathContext.result = "Error division with zero is not allowed.";
                    return
                }
                z = x / y;
        }

        self.MathContext.result = z;
    }
}]);
