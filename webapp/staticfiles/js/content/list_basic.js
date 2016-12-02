define(function(require, exports, module) {
  var $ = require('jquery'),
    simplePagination = require('lib/jquery.simplePagination'),
    bootstrap = require('bootstrap'),
    global = require('global');

  $(function() {
    var pageobj = $.parseJSON($("#page_data").contents().text());

    $("#pagination").pagination({
        pages: pageobj.pages,
        currentPage: pageobj.page,
        onPageClick: function(pageNumber) {
            location.href = "/content/list_basic/" + pageNumber;
        }
    });
  });

});
