(function () {
    'use strict';

      angular.module('BackEndApp')
      .factory('ServiceFactory', ['$http', '$q', '$timeout', ServiceFactory])
      function ServiceFactory($http, $q, $timeout) {
        return {
          saveArticle: function(article) {
            console.log(article);
            return $http.post("api/article", article).then(function(resp) {
              return resp.data;
            }, function(err) {
              return err;
            });
          }, getAllArticle: function() {
            return $http.get("api/article").then(function(resp) {
              return resp.data;
            }, function(err) {
              return err;
            });
          }
        }
      }
})();
