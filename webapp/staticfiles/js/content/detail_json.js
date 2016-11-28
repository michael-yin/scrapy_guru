define(function(require, exports, module) {
  var $ = require('jquery'),
    bootstrap = require('bootstrap'),
    global = require('global');

  $(function() {
    var data = $.parseJSON($("#json_data").contents().text());
    $(".product-price").html(data.price);
    $(".product-title").html(data.title);
  });

});
