define(function(require, exports, module) {
    var $ = require("jquery");
    require("lib/jquery.cookie");

    var Pub = {
      csrfSafeMethod: function(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
      },
    };


    $().ready(function() {
        $.ajaxSetup({
          crossDomain: false, // obviates need for sameOrigin test
          beforeSend: function(xhr, settings) {
            if (!Pub.csrfSafeMethod(settings.type)) {
              xhr.setRequestHeader("X-CSRFToken", $.cookie('csrftoken'));
            }
          }
        });
    });

    return Pub;
})
