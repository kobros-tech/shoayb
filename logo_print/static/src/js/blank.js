// var descrip = {};

//                     // open the dialog
//                     function logo_submit(line_id) {

//                         let proceed_id = `#line_json_proceed_${line_id}`;
//                         let proceed1_id = `#line_json_proceed1_${line_id}`;
//                         let proceed2_id = `#line_json_proceed2_${line_id}`;
//                         let proceed3_id = `#line_json_proceed3_${line_id}`;
//                         console.log("prceed 2 id: ", proceed2_id)

//                         let id = `#submit_button_${line_id}`;
//                         let form_id = `#form_json_submit_${line_id}`;

//                         let input_id = `#line_json_input_file_${line_id}`;
//                         let extra1_input_id = `#line_json_extra1_input_file_${line_id}`;
//                         let extra2_input_id = `#line_json_extra2_input_file_${line_id}`;
//                         let extra3_input_id = `#line_json_extra3_input_file_${line_id}`;

//                         let submit_id = `#line_json_submit_${line_id}`;
//                         let extra1_submit_id = `#line_json_extra1_submit_${line_id}`;
//                         let extra2_submit_id = `#line_json_extra2_submit_${line_id}`;
//                         let extra3_submit_id = `#line_json_extra3_submit_${line_id}`;

//                         let title_id = `#line_json_input_title_${line_id}`;

//                         let img_id = `#line_json_img_preview_${line_id}`;
//                         let extra1_img_id = `#line_json_extra1_img_preview_${line_id}`;
//                         let extra2_img_id = `#line_json_extra2_img_preview_${line_id}`;
//                         let extra3_img_id = `#line_json_extra3_img_preview_${line_id}`;

//                         let chooseFile = document.querySelector(input_id);
//                         let chooseFile_extra1 = document.querySelector(extra1_input_id);
//                         let chooseFile_extra2 = document.querySelector(extra2_input_id);
//                         let chooseFile_extra3 = document.querySelector(extra3_input_id);

//                         let imgPreview = document.querySelector(img_id);
//                         let imgPreview_extra1 = document.querySelector(extra1_img_id);
//                         let imgPreview_extra2 = document.querySelector(extra2_img_id);
//                         let imgPreview_extra3 = document.querySelector(extra3_img_id);

//                         // setting defaults by hiding all elements except for the logo position elements
//                         chooseFile.style.display = "block";
//                         chooseFile_extra1.style.display = "none";
//                         chooseFile_extra2.style.display = "none";
//                         chooseFile_extra3.style.display = "none";
//                         imgPreview.parentNode.style.display = "block";
//                         imgPreview_extra1.parentNode.style.display = "none";
//                         // imgPreview_extra2.style.parentNode.display = "none";
//                         imgPreview_extra3.parentNode.style.display = "none";

//                         // show the dialog with the title of the first logo position
//                         let dialog_ID = `dialog[id=\"dialog_logos_${line_id}\"]`;
//                         document.querySelector(dialog_ID).showModal();

//                         // get description of specific line in order to submit the correct number of logos
//                         fetch(`/logo/get/${line_id}`)
//                         .then(function (response) {
//                             return response.json()
//                         })
//                         .then(async function (description) {
//                             descrip = await description;

//                             document.querySelector(input_id).style.display = "block";

//                             // add the title for the first position by opening the dialog
//                             if (descrip["submissions"][descrip["logo position"]]) {
//                                 document.querySelector(title_id).innerHTML = await `Logo for: ${descrip["logo position"]} position is submitted`;
//                                 imgPreview.src = "data:image/png;base64," + descrip["submissions"][descrip["logo position"]];
//                                 imgPreview.parentNode.style.display = "block";
//                                 document.querySelector(proceed_id).style.display = "block";
//                             }
//                             else {
//                                 document.querySelector(title_id).innerHTML = await `Add logo for: ${descrip["logo position"]} position`;
//                             }
//                         })

//                         // show submitted logo
//                         document.querySelector(input_id).addEventListener('change', function () {
//                             show_logo_selected(chooseFile, imgPreview, submit_id);
//                         })
//                         // show submitted extra 1 logo
//                         document.querySelector(extra1_input_id).addEventListener('change', function () {
//                             show_logo_selected(chooseFile_extra1, imgPreview_extra1, extra1_submit_id);
//                         })
//                         // show submitted extra 2 logo
//                         document.querySelector(extra2_input_id).addEventListener('change', function () {
//                             show_logo_selected(chooseFile_extra2, imgPreview_extra2, extra2_submit_id);
//                         })
//                         // show submitted extra 3 logo
//                         document.querySelector(extra3_input_id).addEventListener('change', function () {
//                             show_logo_selected(chooseFile_extra3, imgPreview_extra3, extra3_submit_id);
//                         })

//                         async function proceeding() {
//                             chooseFile.style.display = "none";
//                             chooseFile_extra1.style.display = "block";
//                             chooseFile_extra2.style.display = "none";
//                             chooseFile_extra3.style.display = "none";
//                             imgPreview.parentNode.style.display = "none";
//                             imgPreview_extra1.parentNode.style.display = "none";
//                             // imgPreview_extra2.style.parentNode.display = "none";
//                             imgPreview_extra3.parentNode.style.display = "none";

//                             if (descrip["additional logo 1"]) {

//                                 if (descrip["additional logo 1"].toUpperCase() === "yes".toUpperCase()) {
//                                     document.querySelector(submit_id).style.display = "none";
//                                     document.querySelector(input_id).style.display = "none";
//                                     document.querySelector(extra1_input_id).style.display = "block";
//                                     document.querySelector(proceed1_id).style.display = "block";

//                                     if (descrip["submissions"][descrip["additional logo position 1"]]) {
//                                         document.querySelector(title_id).innerHTML = await `Logo for: ${descrip["additional logo position 1"]} position is submitted`;
//                                         imgPreview_extra1.src = "data:image/png;base64," + descrip["submissions"][descrip["additional logo position 1"]];
//                                         imgPreview_extra1.parentNode.style.display = "block";
//                                     }
//                                     else {
//                                         document.querySelector(title_id).innerHTML = await `Add logo for: ${descrip["additional logo position 1"]} position`;
//                                     }
//                                 }
//                             }
//                             else {
//                                 document.querySelector(submit_id).style.display = "none";
//                                 document.querySelector(input_id).style.display = "none";
//                                 document.querySelector(title_id).innerHTML = "<span>Logos for all required positions</span><br/><span>have been uploaded</span><br/><span>Thanks</span>";
//                             }

//                             document.querySelector(proceed_id).style.display = "none";
//                         }

//                         async function proceeding_1() {
//                             imgPreview_extra1.parentNode.style.display = "none";

//                             if (descrip["additional logo 2"]) {

//                                 if (descrip["additional logo 2"].toUpperCase() === "yes".toUpperCase()) {
//                                     document.querySelector(extra1_submit_id).style.display = "none";
//                                     document.querySelector(extra1_input_id).style.display = "none";
//                                     document.querySelector(extra2_input_id).style.display = "block";

//                                     if (descrip["submissions"][descrip["additional logo position 2"]]) {
//                                         document.querySelector(title_id).innerHTML = await `Logo for: ${descrip["additional logo position 2"]} position is submitted`;
//                                         imgPreview_extra2.src = "data:image/png;base64," + descrip["submissions"][descrip["additional logo position 2"]];
//                                         imgPreview_extra2.parentNode.style.display = "block";
//                                         document.querySelector(proceed2_id).style.display = "block";
//                                     }
//                                     else {
//                                         document.querySelector(title_id).innerHTML = await `Add logo for: ${descrip["additional logo position 2"]} position`;
//                                     }
//                                 }
//                             }
//                             else {
//                                 document.querySelector(extra1_submit_id).style.display = "none";
//                                 document.querySelector(extra1_input_id).style.display = "none";
//                                 document.querySelector(title_id).innerHTML = "<span>Logos for all selected positions</span><br/><span>are uploaded</span><br/><span>thanks</span>";
//                             }

//                             document.querySelector(proceed1_id).style.display = "none";
//                         }

//                         async function proceeding_2() {
//                             imgPreview_extra2.parentNode.style.display = "none";

//                             if (descrip["additional logo 3"]) {
                                
//                                 if (descrip["additional logo 3"].toUpperCase() === "yes".toUpperCase()) {
//                                     document.querySelector(extra2_submit_id).style.display = "none";
//                                     document.querySelector(extra2_input_id).style.display = "none";
//                                     document.querySelector(extra3_input_id).style.display = "block";

//                                     if (descrip["submissions"][descrip["additional logo position 3"]]) {
//                                         document.querySelector(title_id).innerHTML = await `Logo for: ${descrip["additional logo position 3"]} position is submitted`;
//                                         imgPreview_extra3.src = "data:image/png;base64," + descrip["submissions"][descrip["additional logo position 3"]];
//                                         imgPreview_extra3.parentNode.style.display = "block";
//                                         document.querySelector(proceed3_id).style.display = "block";
//                                     }
//                                     else {
//                                         document.querySelector(title_id).innerHTML = await `Add logo for: ${descrip["additional logo position 3"]} position`;
//                                     }
//                                 }
//                             }
//                             else {
//                                 document.querySelector(extra2_submit_id).style.display = "none";
//                                 document.querySelector(extra2_input_id).style.display = "none";
//                                 document.querySelector(title_id).innerHTML = "<span>Logos for all selected positions</span><br/><span>are uploaded</span><br/><span>Thanks</span>";
//                             }

//                             document.querySelector(proceed2_id).style.display = "none";
//                         }

//                         async function proceeding_3() {
//                             imgPreview_extra3.parentNode.style.display = "none";

//                             document.querySelector(extra3_submit_id).style.display = "none";
//                             document.querySelector(extra3_input_id).style.display = "none";
//                             document.querySelector(title_id).innerHTML = "<span>Logos for all selected positions</span><br/><span>are uploaded</span><br/><span>thanks</span>";

//                             document.querySelector(proceed3_id).style.display = "none";
//                         }

//                         // proceed without submitting
//                         document.querySelector(proceed_id).addEventListener('click', function () {
//                             // Prevents the page from reloading
//                             event.preventDefault();

//                             proceeding()
//                         });
//                         document.querySelector(proceed1_id).addEventListener('click', function () {
//                             // Prevents the page from reloading
//                             event.preventDefault();

//                             proceeding_1()
//                         });
//                         document.querySelector(proceed2_id).addEventListener('click', function () {
//                             // Prevents the page from reloading
//                             event.preventDefault();

//                             proceeding_2()
//                         });
//                         document.querySelector(proceed3_id).addEventListener('click', function () {
//                             // Prevents the page from reloading
//                             event.preventDefault();

//                             proceeding_3()
//                         });

//                         // submit the logo
//                         document.querySelector(submit_id).addEventListener('click',
//                             async function posting(event) {
//                                 // Prevents the page from reloading
//                                 event.preventDefault();

//                                 proceeding()

//                                 let file = document.querySelector(input_id).files[0];
                                
//                                 if (file) {
//                                     let fileReader = new FileReader();
//                                     fileReader.readAsDataURL(file);
//                                     fileReader.addEventListener("load", async function () {
//                                         // get image binaries without it's data padding
//                                         let str_64 = await `${this.result}`.split(',')[1];

//                                         // PUT request for already submitted logos, POST request for new logo submission
//                                         if (descrip["submissions"][descrip["logo position"]]) {

//                                             fetch(`/logo/post/${line_id}`, {
//                                                 method: 'PUT',
//                                                 body: JSON.stringify({
//                                                     file: str_64,
//                                                     logo_position: descrip["logo position"]
//                                                 })
//                                             })
//                                         }
//                                         else {
//                                             fetch(`/logo/post/${line_id}`, {
//                                                 method: 'POST',
//                                                 body: JSON.stringify({
//                                                     file: str_64,
//                                                     logo_position: descrip["logo position"]
//                                                 })
//                                             })
//                                             .then(function (response) {
//                                                 return response.json();
//                                             })
//                                             .then(function (data) {
//                                                 console.log("This data: " + data + "\n------ Is sent to server");
//                                                 console.log(data);
//                                             });
//                                         }
//                                     })
//                                 }
//                             }
//                         )

//                         // submit the extra 1 logo
//                         document.querySelector(extra1_submit_id).addEventListener('click',
//                             async function posting(event) {
//                                 // Prevents the page from reloading
//                                 event.preventDefault();

//                                 proceeding_1()

//                                 let file = document.querySelector(extra1_input_id).files[0];

//                                 if (file) {
//                                     let fileReader = new FileReader();
//                                     fileReader.readAsDataURL(file);
//                                     fileReader.addEventListener("load", async function () {
//                                         // get image binaries without it's data padding
//                                         let str_64 = await `${this.result}`.split(',')[1];

//                                         // PUT request for already submitted logos, POST request for new logo submission
//                                         if (descrip["submissions"][descrip["additional logo position 1"]]) {
//                                             fetch(`/logo/post/${line_id}`, {
//                                                 method: 'PUT',
//                                                 body: JSON.stringify({
//                                                     file: str_64,
//                                                     logo_position: descrip["additional logo position 1"]
//                                                 })
//                                             })
//                                         }
//                                         else {
//                                             fetch(`/logo/post/${line_id}`, {
//                                                 method: 'POST',
//                                                 body: JSON.stringify({
//                                                     file: str_64,
//                                                     logo_position: descrip["additional logo position 1"]
//                                                 })
//                                             })
//                                             .then(function (response) {
//                                                 return response.json();
//                                             })
//                                             .then(function (data) {
//                                                 console.log("This data: " + data + "\n------ Is sent to server");
//                                             });
//                                         }
//                                     })
//                                 }
//                             }
//                         )

//                         // submit the extra 2 logo
//                         document.querySelector(extra2_submit_id).addEventListener('click',
//                             async function posting(event) {
//                                 // Prevents the page from reloading
//                                 event.preventDefault();

//                                 proceeding_2()

//                                 // make post request via fetch to upload the extra 2 logo
//                                 let file = document.querySelector(extra2_input_id).files[0];

//                                 if (file) {
//                                     let fileReader = new FileReader();
//                                     fileReader.readAsDataURL(file);
//                                     fileReader.addEventListener("load", async function () {
//                                         // get image binaries without it's data padding
//                                         let str_64 = await `${this.result}`.split(',')[1];

//                                         // PUT request for already submitted logos, POST request for new logo submission
//                                         if (descrip["submissions"][descrip["additional logo position 2"]]) {
//                                             fetch(`/logo/post/${line_id}`, {
//                                                 method: 'PUT',
//                                                 body: JSON.stringify({
//                                                     file: str_64,
//                                                     logo_position: descrip["additional logo position 2"]
//                                                 })
//                                             })
//                                         }
//                                         else {
//                                             fetch(`/logo/post/${line_id}`, {
//                                                 method: 'POST',
//                                                 body: JSON.stringify({
//                                                     file: str_64,
//                                                     logo_position: descrip["additional logo position 2"]
//                                                 })
//                                             })
//                                             .then(function (response) {
//                                                 return response.json();
//                                             })
//                                             .then(function (data) {
//                                                 console.log("This data: " + data + "\n------ Is sent to server");
//                                             });
//                                         }
//                                     })
//                                 }
//                             }
//                         )

//                         // submit the extra 3 logo
//                         document.querySelector(extra3_submit_id).addEventListener('click',
//                             async function posting(event) {
//                                 // Prevents the page from reloading
//                                 event.preventDefault();

//                                 proceeding_3()

//                                 // make post request via fetch to upload the extra 3 logo
//                                 let file = document.querySelector(extra3_input_id).files[0];

//                                 if (file) {
//                                     let fileReader = new FileReader();
//                                     fileReader.readAsDataURL(file);
//                                     fileReader.addEventListener("load", async function () {
//                                         // get image binaries without it's data padding
//                                         let str_64 = await `${this.result}`.split(',')[1];

//                                         if (descrip["submissions"][descrip["additional logo position 3"]]) {
//                                             fetch(`/logo/post/${line_id}`, {
//                                                 method: 'PUT',
//                                                 body: JSON.stringify({
//                                                     file: str_64,
//                                                     logo_position: descrip["additional logo position 3"]
//                                                 })
//                                             })
//                                         }
//                                         else {
//                                             fetch(`/logo/post/${line_id}`, {
//                                                 method: 'POST',
//                                                 body: JSON.stringify({
//                                                     file: str_64,
//                                                     logo_position: descrip["additional logo position 3"]
//                                                 })
//                                             })
//                                             .then(function (response) {
//                                                 return response.json();
//                                             })
//                                             .then(function (data) {
//                                                 console.log("This data: " + data + "\n------ Is sent to server");
//                                             });
//                                         }
//                                     })
//                                 }
//                             }
//                         )


//                         function show_logo_selected(chooseFile, imgPreview, next_button) {

//                             let files = chooseFile.files[0];
//                             if (files) {
//                                 let fileReader = new FileReader();
//                                 fileReader.readAsDataURL(files);
//                                 fileReader.addEventListener("load", function () {
//                                     imgPreview.style.display = "block";
//                                     let link = `${this.result}`;
//                                     imgPreview.src = link;
//                                     imgPreview.parentNode.style.display = "block";
//                                 });

//                                 if (next_button) {
//                                     document.querySelector(next_button).style.display = "block";
//                                 }
//                             }
//                         }
                        
//                         return false;
//                     }

//                     // read file image and convert it to base 64 string
//                     async function str_64(files) {
//                         let link = "";
//                         let fileReader = new FileReader();
//                         fileReader.readAsDataURL(files);
//                         fileReader.addEventListener("load", async function () {
//                             link = await `${this.result}`;
//                             console.log("the link: ", link)
//                         })
//                     }

//                     // close the dialog
//                     function close_dialog_logos(line_id) {
//                         // close the relevant dialog
//                         let dialog_ID = `dialog[id=\"dialog_logos_${line_id}\"]`;
//                         document.querySelector(dialog_ID).close();
//                     }