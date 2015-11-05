'use strict';
/**
 * Created by vladimir on 27.10.15..
 */

angular.module('nbaFilters', [])
    .filter('searchFilter', function() {
      return function(input, content) { // content is the word in input expression
        //  Search can't be empty, it must have value
        //  if doesn't have, we return completely word from table field
        if (!content)
            return input;

        //  Below we use function indexOf, that function works only with the
        //  array and the string, so if we have any other type in our table fields
        //  we must convert that in string, if that's possible(using try/catch)
        try {
            if (typeof input != 'string')
                input = String(input);

            if (typeof content != 'string')
                content = String(content);
        }
        catch(ex) {
            alert("Can't convert input or content to integer. Error " + ex);
            return input;
        }


        //  If find the content word in the input word
        //  we make input with bold content within itself
        if (input.indexOf(content) >= 0) {
            var tokens = input.split(content);
            var contentChanged;
            contentChanged = content.bold().fontcolor("#880000");

            var returnString = tokens[0];

            for (var i = 1; i < tokens.length; i++) {
                returnString += (contentChanged + tokens[i]);
            }

            return returnString;
        }
        else
            return input;
      };
});