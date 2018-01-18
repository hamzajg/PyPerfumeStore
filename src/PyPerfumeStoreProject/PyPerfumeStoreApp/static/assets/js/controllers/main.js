'use strict';

/**
 * @ngdoc function
 * @name app.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of the saitunaApp
 */
app
  .controller('MainCtrl', function ($scope,  $rootScope, $location, $interval) {

    $scope.currentPath = $location.path();
  });
