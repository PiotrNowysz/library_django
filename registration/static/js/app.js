document.addEventListener("DOMContentLoaded", function () {

    var password = $('[type=password]');
    var show_pass = $('#show_pass');
    show_pass.on("click", function () {
        if ($(this).prop('checked')) {
            password.attr('type', 'text')
        } else {
            password.attr('type', 'password')
        }
    });


    $("#id_username").change(function () {
        var username = $(this).val();

        $.ajax({
            url: '/ajax/validate_username/',
            data: {
                'username': username
            },
            dataType: 'json',
            success: function (data) {
                if (data.is_taken) {
                    alert("A user with this username already exists.");
                }
            }
        });

    });


});

