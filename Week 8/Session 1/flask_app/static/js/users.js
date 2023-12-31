// $(document).ready(function() {
//     $('#element_form').submit(function(e) {
//         e.preventDefault();
//         var response = $.post('/events/create/return_element', $('#element_form').serialize());
//         response.done(function(data) {
//             console.log(data);
//             $('#events_table').append(data);
//         })
//     });
//     $('#json_form').submit(function(e) {
//         e.preventDefault();
//         var response = $.post('/events/create/return_json', $('#json_form').serialize());
//         response.done(function(data) {
//             console.log(data);
//             $('#events_table').append("<tr><td>" + data['title'] + "</tr></td>");
//         })
//     });
// });
var elementForm = document.getElementById('element_form');
elementForm.onsubmit = function(e){
    // "e" is the js event happening when we submit the form.
    // e.preventDefault() is a method that stops the default nature of javascript.
    e.preventDefault();
    // create FormData object from javascript and send it through a fetch post request.
    var form = new FormData(elementForm);

    // this how we set up a post request and send the form data.
    fetch("/events/create/return_element", { method :'POST', body : form})
        .then( response => response.text() )
        .then( data => {
            var eventsTable =document.getElementById('table_body');
            eventsTable.innerHTML += data;
            // eventsTable.innerHTML += data;
            console.log(data);
        });
}





var jsonForm = document.getElementById('json_form');
jsonForm.onsubmit = function(e){
    // "e" is the js event happening when we submit the form.
    // e.preventDefault() is a method that stops the default nature of javascript.
    e.preventDefault();
    // create FormData object from javascript and send it through a fetch post request.
    var form = new FormData(jsonForm);
    // this how we set up a post request and send the form data.
    fetch("/events/create/return_json", { method :'POST', body : form})
        .then( response => response.json() )
        .then( data => {
            var eventsTable =document.getElementById('events_table');
            console.log(data)
            actual_data = data['event']
            var new_row = eventsTable.insertRow();
            new_row.insertCell(0).innerHTML= actual_data['id'];
            new_row.insertCell(1).innerHTML= actual_data['title'];
            new_row.insertCell(2).innerHTML= actual_data['created_at'];
            new_row.insertCell(3).innerHTML= actual_data['updated_at'];
        });
}