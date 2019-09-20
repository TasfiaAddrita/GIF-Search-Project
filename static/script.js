$(function() {
    $("#process-input").on('keyup', function(response) {
        // console.log(response)
        // var inp = String.fromCharCode(response.keyCode);
        // if (/[a-zA-Z0-9-_ ]/.test(inp)) {
            // alert("input was a letter, number, hyphen, underscore or space");

            var search = $('#process-input').val()
            // console.log(search)
            $.ajax({
                url: '/search',
                // data: $('form').serialize(),
                data: {"search": search},
                type: 'POST',
                success: function(response) {
                    console.log(search);
                    console.log(response);
                    $("#img-grid").html(response);
                },
                error: function(error) {
                    console.log(error)
                }
            });
        // }
    });
});
