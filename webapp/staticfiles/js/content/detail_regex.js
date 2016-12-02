define(function(require, exports, module) {
  var $ = require('jquery'),
    bootstrap = require('bootstrap'),
    global = require('global');

  var data = {
    "price": "$ 13.99", "title": "Regex is important"
  };

  $(function() {
    $(".product-price").html(data.price);
    $(".product-title").html(data.title);
  });

});
