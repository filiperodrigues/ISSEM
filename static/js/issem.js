$(document).ready(function () {
    $(document).ready(function () {
        $('.ui.dropdown').dropdown();
        $('#id_estado_civil').dropdown();
        $('#id_cargo').dropdown();
        $('#id_tipo_sanguineo').dropdown();
        $('#id_cidade_atual').dropdown();
        $('#id_cidade_natural').dropdown();
        $('#tipo').dropdown();
    });

    $('.ui.modal')
        .modal('setting', 'closable', false)
        .modal('attach events', '#cadastro-secretaria', 'show');
});

function get_cidade() {
    $.ajax({
        type: 'POST',
        url: '/issem/escolha_cidade_natural/',
        data: {
            estado: $("select[name='estado']").val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        dataType: 'json',
        success: function (data) {
            var options = '<option>Selecione uma cidade</option>';
            for (var i = 0; i < data.length; i++) {
                options += '<option value="' + data[i].pk + '">' + data[i].fields['nome'] + '</option>';
                console.log(options)
            }
            $("select#cidade_atual").html(options);
            $("select#cidade_atual").attr('disabled', false);
        }
    });
}

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