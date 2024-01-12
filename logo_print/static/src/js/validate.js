

odoo.define("logo.chooseLogoDialog", function(require) {
    "use strict";


    var publicwidget = require("web.public.widget");

    publicwidget.registry.chooseLogoDialog = publicwidget.Widget.extend({
        selector: "#greeting_id",
        events: {
            'click': "_dialog",
        },

        _dialog: function(evt) {
            // before opening return all extra values to "no" and "no thanks"
            document.querySelectorAll("select").forEach(function (element) {
                if (ptal_printing_id === element.dataset.attribute_id) {
                    
                    // before opening the dialog
                    setting_defaults()
                }
            });


            document.querySelector("#first_logo_table").style.display = "block";
            document.querySelector("#second_logo_table").style.display = "none";
            document.querySelector("#third_logo_table").style.display = "none";
            document.querySelector("#fourth_logo_table").style.display = "none";
            document.querySelector("#extra_logo_choice").style.display = "none";
            document.querySelector("#extra2_logo_choice").style.display = "none";
            document.querySelector("#extra3_logo_choice").style.display = "none";
            document.querySelector("dialog[id='dialog_positions']").showModal();
        },
    });

    publicwidget.registry.closeLogoDialog = publicwidget.Widget.extend({
        selector: "#close_dialog",
        events: {
            'click': "_close_dialog",
        },

        _close_dialog: function(evt) {
            
            // close the dialog button
            if (evt.target.value === "close") {
                document.querySelector("dialog[id='dialog_positions']").close();
                return false;
            }
        },
    });

    // publicwidget.registry.extraLogoDialog = publicwidget.Widget.extend({
    //     selector: "#extra_logo_choice",
    //     events: {
    //         'click': "_extra_logo",
    //     },
        
        // // add extra logo and stop submitting
        // _extra_logo: function(evt) {
        //     document.querySelector("#first_logo_table").style.display = "none";
        //     document.querySelector("#second_logo_table").style.display = "block";
        //     evt.target.style.display = "none";

        //     // set the value of extra logo attribute be yes
        //     let exta_logo = document.getElementsByName(`ptal-${extra_y_n_attr_line_id}`)
        //     console.log(exta_logo.value)
        //     exta_logo.value = extra_yes_id
        //     console.log(exta_logo.value)

        //     return false;
        // },
    // })


});
