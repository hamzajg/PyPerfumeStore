'use strict';

/**
 * @ngdoc function
 * @name app.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of the saitunaApp
 */
app
  .controller('MainCtrl', ['$scope', '$rootScope', '$route', '$routeParams', '$location', function ($scope,  $rootScope, $route, $routeParams, $location) {

    $scope.currentPath = $location.path();
  }]);
