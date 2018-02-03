(function() {
  'use strict';

  angular.module('BackEndApp')
    .controller('NewArticleCtrl', ['$scope', 'ServiceFactory', NewArticleCtrl])
    .controller('ListArticleCtrl', ['$scope', 'ServiceFactory', '$filter', ListArticleCtrl])

  function NewArticleCtrl($scope, ServiceFactory) {
    var self = this;
    $scope.saveArticle = function(article) {
      ServiceFactory.saveArticle(article);
    }
  }

  function ListArticleCtrl($scope, ServiceFactory, $filter) {
    var self = this;
    var init;
    $scope.searchKeywords = '';
    $scope.filteredArticles = [];
    $scope.row = '';
    $scope.select = select;
    $scope.onFilterChange = onFilterChange;
    $scope.onNumPerPageChange = onNumPerPageChange;
    $scope.onOrderChange = onOrderChange;
    $scope.search = search;
    $scope.order = order;
    $scope.numPerPageOpt = [3, 5, 10, 20];
    $scope.numPerPage = $scope.numPerPageOpt[2];
    $scope.currentPage = 1;
    $scope.currentPage = [];
    $scope.listArticles = [];
    ServiceFactory.getAllArticle().then(function(data) {
      $scope.listArticles = data;
    });

    function select(page) {
      var end, start;
      start = (page - 1) * $scope.numPerPage;
      end = start + $scope.numPerPage;
      return $scope.currentPageArticles = $scope.filteredArticles.slice(start, end);
    };

    function onFilterChange() {
      $scope.select(1);
      $scope.currentPage = 1;
      return $scope.row = '';
    };

    function onNumPerPageChange() {
      $scope.select(1);
      return $scope.currentPage = 1;
    };

    function onOrderChange() {
      $scope.select(1);
      return $scope.currentPage = 1;
    };

    function search() {
      $scope.filteredArticles = $filter('filter')($scope.listArticles, $scope.searchKeywords);
      return $scope.onFilterChange();
    };

    function order(rowName) {
      if ($scope.row === rowName) {
        return;
      }
      $scope.row = rowName;
      $scope.filteredArticles = $filter('orderBy')($scope.listArticles, rowName);
      return $scope.onOrderChange();
    };

    init = function() {
      $scope.search();
      return $scope.select($scope.currentPage);
    };

    init();
  }
})();
