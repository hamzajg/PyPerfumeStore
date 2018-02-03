(function () {
    'use strict';

    angular.module('BackEndApp')
        .controller('NewArticleCtrl', ['$scope', 'ServiceFactory', NewArticleCtrl])
        .controller('ListArticleCtrl', ['$scope', 'ServiceFactory', ListArticleCtrl])

    function NewArticleCtrl($scope, ServiceFactory) {
      var self = this;
      $scope.saveArticle = function(article) {
        ServiceFactory.saveArticle(article);
      }
    }
    function ListArticleCtrl($scope, ServiceFactory) {
      var self = this;
      $scope.listArticle = [];
      ServiceFactory.getAllArticle().then(function(data) {
        $scope.listArticle = data;
      });
    }
})();
