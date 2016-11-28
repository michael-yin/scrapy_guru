define(function(require, exports, module) {
  var $ = require('jquery'),
    bootstrap = require('bootstrap'),
    global = require('global');
    require("lib/jquery.cookie");

  var token = $.cookie('token');

  $(function() {
    $.ajax({
      type: "GET",
      url: "/content/ajaxdetail_cookie?token="+token,
      success: function(obj) {
        console.log(obj);
        $(".product-price").html(obj.price);
        $(".product-title").html(obj.title);
      },
      error: function(err) {
        alert("something is wrong in webapp");
      },
    });
  });

});
