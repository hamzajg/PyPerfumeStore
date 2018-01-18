'use strict';

var app = angular.module('PyPerfumeStore', ['ngRoute',])
.config(['$locationProvider', '$routeProvider', function($locationProvider, $routeProvider) {
  $routeProvider.when('/', {
    				templateUrl : 'static/views/home.html'
    			}).when('/login', {
    				templateUrl : 'static/views/login.html'
    			}).otherwise({
          redirectTo: '/'
        });
        // use the HTML5 History API
        //$locationProvider.html5Mode(true);
}]);
