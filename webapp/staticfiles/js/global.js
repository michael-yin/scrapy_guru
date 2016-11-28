define(function(require, exports, module) {
  require("jquery");
  var $ = window.$;
  var jQuery = window.$;

  var Self = {
    getUrlVars: function(url_str) {
      /*
          http://jquery-howto.blogspot.com/2009/09/get-url-parameters-values-with-jquery.html
          */
      if (url_str.indexOf('?') > -1) {
        var vars = [],
          hash;
        var hashes = url_str.slice(url_str.indexOf('?') + 1).split('&');
        for (var i = 0; i < hashes.length; i++) {
          hash = hashes[i].split('=');
          vars.push(hash[0]);
          vars[hash[0]] = hash[1];
        }
        return vars;
      } else {
        return {};
      }
    },

    getUrlVar: function(url_str, key) {
      dict = Self.getUrlVars(url_str);
      if (key in dict) {
        return dict[key];
      } else {
        return "";
      }
    },

    getLocationUrlVar: function(key) {
      var dict = Self.getUrlVars(window.location.href);
      if (key in dict) {
        return dict[key];
      } else {
        return "";
      }
    },

    getPageIndex: function() {
      var dict = Self.getUrlVars(window.location.href);
      if ("page" in dict) {
        return dict[key];
      } else {
        return 1;
      }
    }
  };


  //expose it
  return Self;

});
