document.addEventListener("DOMContentLoaded", function () {

    var pass = $('[type=password]');
    var show_pass = $('#show_pass');
    show_pass.on("click", function () {
        if ($(this).prop('checked')) {
            pass.attr('type', 'text')
        } else {
            pass.attr('type', 'password')
        }
    });
});