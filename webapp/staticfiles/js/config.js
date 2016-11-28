//The build will inline common dependencies into this file.

//For any third party dependencies, like jQuery, place them in the lib folder.

//Configure loading modules from the lib directory,
//except for 'app' ones, which are in a sibling
//directory.

requirejs.config({
    baseUrl: '/static/js/'
    ,
    paths: {
      jquery: "lib/jquery/jquery-1.9.1"
      ,
      bootstrap:"lib/bootstrap/bootstrap"
    }
    ,
    shim: {
      bootstrap: {deps: ['jquery']}
      ,
      'lib/jquery.simplePagination': {deps: ['jquery']}
      ,
      'lib/d3': {exports: 'd3'}
    }
});


