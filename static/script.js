var timeoutID;

// ---- type ahead stretch challenge ----
// if user types in search bar, after some time (wait for user to finish typing), a POST request is made
// to /search in app.py, which will return an html file organizing the gifs, and then load the gifs in
// img-grid
$(function() {
    $("#process-input").on('input', function(response) {
        window.clearTimeout(timeoutID);
        var search = $('#process-input').val()
        // console.log(response)
        timeoutID = window.setTimeout(function(search) {
            $.ajax({
                url: '/search',
                data: {"search": search},
                type: 'POST',
                success: function(response) {
                    // console.log(search);
                    // console.log(response);
                    $("#img-grid").html(response);
                },
                error: function(error) {
                    console.log(error)
                }
            });
        }, 1000, search)
    });
});
