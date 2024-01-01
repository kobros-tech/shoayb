

odoo.define("logo.chooseLogoDialog", function(require) {
    "use strict";

    console.log("Hello kobrosly this is your first JS code in odoo: testing mode!");


    var publicwidget = require("web.public.widget");

    publicwidget.registry.chooseLogoDialog = publicwidget.Widget.extend({
        selector: "#greeting_id",
        events: {
            'click': "_dialog",
        },

        _dialog: function(evt) {
            console.log("Hello kobrosly this is your first JS code in odoo");
            document.querySelector("dialog").showModal();
        },
    });

    publicwidget.registry.closeLogoDialog = publicwidget.Widget.extend({
        selector: "#close_dialog",
        events: {
            'click': "_dialog",
        },

        _dialog: function(evt) {
            
            // close the dialog button
            if (evt.target.value === "close") {
                console.log("closing the dialog")
                document.querySelector("dialog").close();
                return false;
            }
            
        },
    });


    
});
