'use strict';

var app = angular.module('PyPerfumeStore', ['ngRoute', 'ngAnimate', 'ngSanitize',
  'ngResource',
  'angular-loading-bar',
  'angular-page-loader',])
.run(function($timeout, $rootScope) {

    $timeout(function() { // simulate long page loading
        $rootScope.isLoading = false; // turn "off" the flag
    }, 2000)

}).run(['$route', function($route)  {
  $route.reload();
}])
.config(['cfpLoadingBarProvider', function (cfpLoadingBarProvider) {cfpLoadingBarProvider.includeSpinner = false;/*cfpLoadingBarProvider.latencyThreshold = 500;*/}])
.config(['$locationProvider', '$routeProvider', function($locationProvider, $routeProvider) {
  $routeProvider.when('/', {
    				templateUrl : 'static/views/home.html',
    			}).when('/login', {
    				templateUrl : 'static/views/login.html'
    			}).otherwise({
          redirectTo: '/'
        });
        // use the HTML5 History API
        $locationProvider.html5Mode(true);
}]);
