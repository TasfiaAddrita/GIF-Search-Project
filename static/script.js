$(function() {
    $("#process-input").on('keyup', function() {
        var search = $('#process-input').val()
        $.ajax({
            url: '/search',
            data: $('form').serialize(),
            type: 'POST',
            success: function(response) {
                console.log(search)
                console.log(response)
                // $("#img-grid").innerHTML = response.results
            },
            error: function(error) {
                console.log(error)
            }
        });
    });
});
