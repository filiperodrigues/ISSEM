$(document).ready(
    function () {
        $("#id_data_nascimento, #id_data_inicio, #id_data_admissao, #id_data_inicial, #id_data_retorno, #id_data_pericia, #id_data_portaria").datepicker({dateFormat: "dd/mm/yy"});
        $('.ui.dropdown').dropdown();
        $('#id_estado_civil').dropdown();
        $('#id_cargo').dropdown();
        $('#id_tipo_sanguineo').dropdown();
        $('#id_estado_natural').dropdown();
        $('#id_estado_atual').dropdown();
        $('#id_cidade_atual').dropdown();
        $('#id_cidade_natural').dropdown();
        $('#id_local_trabalho').dropdown();
        $('#id_tipo').dropdown();
        $('#id_departamento').dropdown();
        $('.ui.modal')
            .modal('setting', 'closable', false)
            .modal('attach events', '#cadastro-secretaria', 'show');

    });

function get_cidade_natural() {
    $.ajax({
        type: 'POST',
        url: '/issem/escolha_cidade_natural/',
        data: {
            estado: $("select[name='estado_natural']").val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        dataType: 'json',
        success: function (data) {

            var options = '';
            for (var i = 0; i < data.length; i++) {
                options += '<option value="' + data[i].pk + '">' + data[i].fields['nome'] + '</option>';
            }
            $("#id_cidade_natural").html(options);
        }
    });
}

function get_cidade_atual() {
    $.ajax({
        type: 'POST',
        url: '/issem/escolha_cidade_atual/',
        data: {
            estado: $("select[name='estado_atual']").val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        dataType: 'json',
        success: function (data) {
            $("select#id_cidade_atual").html("");
            var options = '';
            for (var i = 0; i < data.length; i++) {
                options += '<option value="' + data[i].pk + '">' + data[i].fields['nome'] + '</option>';
            }
            $("select#id_cidade_atual").html(options);
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
            for (var i = dado.length - 1; i >= 0; i--) {
                options += '<option value="' + dado[i].pk + '">' + dado[i].fields['nome'] + '</option>';
            }
            $("input#id_sec").prop('value', '');
            $("select#id_secretaria").html(options);
        },
    });
}

function data_fim_teste(data_inicio) {
    // #======= CADASTRO DEPENDENTE =======#
    $("#id_data_fim").datepicker({minDate: data_inicio, dateFormat: "dd/mm/yy"});
    $("input#id_data_fim").attr('disabled', false);
    // #======= CADASTRO BENEFÍCIO =======#
    $("#id_data_final").datepicker({minDate: data_inicio, dateFormat: "dd/mm/yy"});
    $("input#id_data_final").attr('disabled', false);
}
