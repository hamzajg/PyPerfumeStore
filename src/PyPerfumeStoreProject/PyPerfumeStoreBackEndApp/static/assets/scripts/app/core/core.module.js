(function () {
    'use strict';

    angular.module('BackEndApp.core', [
        // Angular modules
         'ngAnimate'
        ,'ngAria'
        ,'ngMessages'

        // Custom modules
        ,'BackEndApp.layout'
        ,'BackEndApp.i18n'

        // 3rd Party Modules
        ,'ngMaterial'
        ,'ui.router'
        ,'ui.bootstrap'
        ,'duScroll'
    ]);

})();
