$(document).ready(
    function () {
        $('.cpf input').mask('000.000.000-00', {reverse: true});
        $('.data input').mask('00/00/0000');
        $('.hora').mask('00:00');
        $('.minuto').mask('00');
        $('.cep input').mask('00000-000');
        $('.rg input').mask('000000000');
        $('.n_endereco input').mask('000000000');
        $('.fone_ddd input').mask('(00) 0000-0000');
        $('.crm input').mask('00000000000000000000000000000000');
        $('.somente_letras input').mask('SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS', {
            'translation': {
                S: {pattern: /[A-Za-z ]/},
            }
        });
        get_cidade_natural();
        get_cidade_atual();
        $("#id_data_inicio, #id_data_admissao, #id_data_inicial, #id_data_retorno, #id_data_pericia, #id_data_portaria, #id_data_final").datepicker({dateFormat: "dd/mm/yy"});
        $("#id_data_nascimento").datepicker({
            dateFormat: "dd/mm/yy",
            maxDate:'-18Y',
            monthNames: ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro'],
            dayNames: ['Domingo','Segunda','Terça','Quarta','Quinta','Sexta','Sábado'],
            dayNamesShort: ['Dom','Seg','Ter','Qua','Qui','Sex','Sáb','Dom'],
            dayNamesMin: ['D','S','T','Q','Q','S','S','D'],
        });
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
        $('#id_cidade').dropdown();
        $('#id_secretaria').dropdown();
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

function change_life() {
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