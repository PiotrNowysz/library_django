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

    var confirmation = $('#confirmation');
    var del = $('#delete');
    var no = $('#no');

    del.on("click", function () {
        confirmation.removeAttr('hidden')
    });

    no.on('click', function () {
        confirmation.attr('hidden', 'hidden')

    })


});

