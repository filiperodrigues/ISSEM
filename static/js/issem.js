$(document).ready(function () {

    // ===== MÁSCARAS ===== //
    $('.cpf input').mask('000.000.000-00', {reverse: true});
    $('.cnpj input').mask('00.000.000/0000-00', {reverse: true});
    $('.hora input').mask('00:00');
    $('.data input').mask('00/00/0000');
    $('.dois_digitos input').mask('00');
    $('.cep input').mask('00000-000');
    $('.rg input').mask('000000000');
    $('.dez_digitos input').mask('0000000000');
    $('.fone_ddd input').mask('(00) 00000-0000');
    $('.crm input').mask('00000000000000000000000000000000');
    $('.valor input').mask('00000000000000000,00', {reverse: true});
    $('.somente_numeros input').mask('00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000');
    $('.somente_letras input').mask('SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS', {
        'translation': {
            S: {pattern: /[A-Za-zÀ-ú ]/},
        }
    });

    // ===== ESTILIZAR DROPDOWNS ===== //
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
    $('#id_cidade').dropdown();
    $('#id_estados').dropdown();
    $('#id_secretaria').dropdown();
    $('#id_orgao').dropdown();
    $('#id_groups').dropdown();
    $('.ui.dropdown').dropdown();
    $('.ui.modal')
        .modal('setting', 'closable', false)
        .modal('attach events', '#CadastroSecretaria', 'show')
        .modal('attach events', '#ProximasConsultas', 'show');




    //grupo edicao

    id_campo = $('#group_user').val()
    $('#id_groups option[value='+id_campo+']').attr('selected', 'selected')
    valor_campo = $('#id_groups option[value='+id_campo+']').text()
    $('#div_group_user .selection.dropdown .text').text(valor_campo).removeClass('default')

});

function calendar_input(dependente){
    confDefault = {
        dateFormat: "dd/mm/yy",
        monthNames: ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'],
        dayNames: ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado'],
        dayNamesShort: ['Dom', 'Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb', 'Dom'],
        dayNamesMin: ['D', 'S', 'T', 'Q', 'Q', 'S', 'S', 'D']
    };

    if(dependente == true) {
        $("#id_data_admissao, #id_data_inicial, #id_data_retorno, #id_data_pericia, #id_data_portaria, #id_data_final, #id_data_inicio_afastamento, #id_data_final_afastamento, #id_data_nascimento").datepicker(confDefault);
    }else{
        $("#id_data_admissao, #id_data_inicial, #id_data_retorno, #id_data_pericia, #id_data_portaria, #id_data_final, #id_data_inicio_afastamento, #id_data_final_afastamento").datepicker(confDefault);
        conf_dataNasc = confDefault;
        conf_dataNasc.maxDate = '-18Y';
        $("#id_data_nascimento").datepicker(conf_dataNasc);
    }
}

function limita_data_final() {
    var dateFormat = "dd/mm/yy",
        from = $("#id_data_inicial")
            .datepicker({
                defaultDate: "+1w",
                changeMonth: true,
                numberOfMonths: 3
            })
            .on("change", function () {
                to.datepicker("option", "minDate", getDate(this));
            }),
        to = $("#id_data_final").datepicker({
            defaultDate: "+1w",
            changeMonth: true,
            numberOfMonths: 3
        })
            .on("change", function () {
                from.datepicker("option", "minDate", getDate(from));
            });

    function getDate(element) {
        var date;
        try {
            date = $.datepicker.parseDate(dateFormat, element.value);
        } catch (error) {
            date = null;
        }
        return date;
    }
}

Date.prototype.addDays = function(days)
{
    var dat = new Date(this.valueOf());
    dat.setDate(dat.getDate() + days);
    return dat;
}

function limita_data_final_afastamento() {
    var dateFormat = "dd/mm/yy",

        from = $("#id_data_inicio_afastamento")
            .datepicker({
                defaultDate: "+2w",
                changeMonth: true,
                numberOfMonths: 3
            })
            .on("change", function () {
                data = getDate(this)

                to.datepicker("option", "minDate", data.addDays(15));
            }),
        to = $("#id_data_final_afastamento").datepicker({
            defaultDate: "+1w",
            changeMonth: true,
            numberOfMonths: 3
        })
            .on("change", function () {
                from.datepicker("option", "minDate", getDate(from));
            });

    function getDate(element) {
        var date;
        try {
            date = $.datepicker.parseDate(dateFormat, element.value);
        } catch (error) {
            date = null;
        }
        return date;
    }
}

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
            var options = '';
            for (var i = 0; i < data.length; i++) {
                options += '<option value="' + data[i].pk + '">' + data[i].fields['nome'] + '</option>';
            }
            $("select#id_cidade_atual").html(options);
        }
    });
}

function get_cidade_local_trabalho() {
    $.ajax({
        type: 'POST',
        url: '/issem/escolha_cidade_local_trabalho/',
        data: {
            estado: $("select[name='estados']").val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        dataType: 'json',
        success: function (data) {
            var options = '';
            for (var i = 0; i < data.length; i++) {
                options += '<option value="' + data[i].pk + '">' + data[i].fields['nome'] + '</option>';
            }
            $("select#id_cidade").html(options);
        }
    });
}

function get_secretaria() {
    $.ajax({
        type: 'POST',
        url: '/issem/cad/secretaria/',
        data: {
            sec: $("input[name='sec']").val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        dataType: 'json',
        success: function (dado) {
            var options = '';
            options += '<option selected="selected" value="' + dado[dado.length-1].pk + '">' + dado[dado.length-1].fields['nome'] + '</option>';
            for (var i = dado.length - 1; i >= 0; i--) {
                options += '<option value="' + dado[i].pk + '">' + dado[i].fields['nome'] + '</option>';
            }
            $("input#id_sec").prop('value', '');
            $("select#id_secretaria").html(options);
        },
    });
}

$('.message .close')
  .on('click', function() {
    window.history.back();
  })
;
