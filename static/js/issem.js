$(document).ready(function () {


    $('.ui.modal')
        .modal('setting', 'closable', false)
        .modal('attach events', '#cadastro-secretaria', 'show');
});

function get_secretaria() {
    $.ajax({
        type: 'POST',
        url: '/issem/add/secretaria/',
        data: {
            sec: $("input[name='sec']").val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        dataType: 'json',
        success: function (dado) {
            var options = '';
            for (var i = dado.length-1; i >= 0; i--) {
                options += '<option value="' + dado[i].pk + '">' + dado[i].fields['nome'] + '</option>';
            }
            $("input#id_sec").prop('value', '');
            $("select#id_secretaria").html(options);


        },
    });
}
