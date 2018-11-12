function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


$(document).ready(function () {
    $('.delete_button').click(function (e) {
        e.preventDefault();
        var csrftoken = getCookie('csrftoken');
        var url = $(this).attr('href');
        $.ajax({
            url: url,
            method: 'DELETE',
            data: { csrfmiddlewaretoken: csrftoken }
        }).done(function (data) {
            location.reload();
            concole.log(data);
        })
    })
});