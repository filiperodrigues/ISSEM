$(document).ready(function () {

    // ===== MÁSCARAS ===== //
    $('.cpf input').mask('000.000.000-00', {reverse: true});
    $('.cnpj input').mask('00.000.000/0000-00', {reverse: true});
    $('.hora input').mask('00:00');
    $('.data input').mask('00/00/0000');
    $('.dois_digitos input').mask('00');
    $('.dez_digitos input').mask('0000000000');
    $('.cep input').mask('00000-000');
    $('.rg input').mask('000000000');
    $('.dez_digitos input').mask('0000000000');
    $('.fone_ddd_9digitos input').mask('(00) 00000-0000');
    $('.fone_ddd_8digitos input').mask('(00) 0000-0000');
    $('.crm input').mask('00000000000000000000000000000000');
    $('.valor input').mask('00000000000000000,00', {reverse: true});
    $('.somente_numeros input').mask('00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000');
    $('.somente_letras input').mask('SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS', {
        'translation': {
            S: {pattern: /[A-Za-zÀ-ú ]/},
        }
    });

    // ===== ESTILIZAR DROPDOWNS ===== //
    $('select').dropdown();

    $('.ui.dropdown').dropdown();
});

function calendar_input(dependente) {
    confDefault = {
        dateFormat: "dd/mm/yy",
        monthNames: ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'],
        dayNames: ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado'],
        dayNamesShort: ['Dom', 'Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb', 'Dom'],
        dayNamesMin: ['D', 'S', 'T', 'Q', 'Q', 'S', 'S', 'D']
    };

    if (dependente == true) {
        $("#id_data_admissao, #id_data_inicial, #id_data_retorno, #id_data_pericia, #id_data_portaria, #id_data_final, #id_data_inicio_afastamento, #id_data_final_afastamento, #id_data_nascimento").datepicker(confDefault);
    } else {
        $("#id_data_inicio_periodo, #id_data_fim_periodo, #id_data_admissao, #id_data_inicial, #id_data_retorno, #id_data_pericia, #id_data_portaria, #id_data_final, #id_data_inicio_afastamento, #id_data_final_afastamento").datepicker(confDefault);
        conf_dataNasc = confDefault;
        conf_dataNasc.maxDate = '-18Y';
        $("#id_data_nascimento").datepicker(conf_dataNasc);
    }
}

function limita_data_final() {
    var dateFormat = "dd/mm/yy",
        from = $("#id_data_inicial, #id_data_inicio_periodo")
            .datepicker({
                defaultDate: "+1w",
                changeMonth: true,
                numberOfMonths: 3
            })
            .on("change", function () {
                to.datepicker("option", "minDate", getDate(this));
            }),
        to = $("#id_data_final, #id_data_fim_periodo").datepicker({
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

Date.prototype.addDays = function (days) {
    var dat = new Date(this.valueOf());
    dat.setDate(dat.getDate() + days);
    return dat;
}

function limita_data_final_afastamento() {
    var dateFormat = "dd/mm/yy",

        from = $("#id_data_inicio_afastamento, #data_inicio_periodo")
            .datepicker({
                defaultDate: "+2w",
                changeMonth: true,
                numberOfMonths: 3
            })
            .on("change", function () {
                data = getDate(this)

                to.datepicker("option", "minDate", data.addDays(15));
            }),
        to = $("#id_data_final_afastamento, #data_fim_periodo").datepicker({
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

//Todo Futuro
// function get_departamento() {
//     alert("oi");
//     $.ajax({
//         type: 'POST',
//         url: '/issem/escolha_departamento/',
//         data: {
//             estado: $("select[name='groups']").val(),
//             csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
//         },
//         dataType: 'json',
//         success: function (data) {
//             console.log(data);
//             var options = '';
//             for (var i = 0; i < data.length; i++) {
//                 options += '<option value="' + data[i].pk + '">' + data[i].fields['name'] + '</option>';
//             }
//            $("#id_groups").html(options);
//
//         }
//     });
// }

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
            options += '<option selected="selected" value="' + dado[dado.length - 1].pk + '">' + dado[dado.length - 1].fields['nome'] + '</option>';
            for (var i = dado.length - 1; i >= 0; i--) {
                options += '<option value="' + dado[i].pk + '">' + dado[i].fields['nome'] + '</option>';
            }
            $("input#id_sec").prop('value', '');
            $("select#id_secretaria").html(options);
        },
    });
}

$('.message .close')
    .on('click', function () {
        window.history.back();
    })
;

$('.abrirModalConsultas').click(function () {
    $('.modalConsultas').modal('show');
});

$('.abrirModalConfirmacao').click(function () {
    $('.modalConfirmacao').modal('show');
});

$('.abrirModalCadCid').click(function () {
    $('.modalCadCid').modal('show');
});


function modalRequerimento(id) {
    html = "<div class='ui green ok inverted button'>Não</div>" +
        "<a class='ui red ok inverted button IDAgendamento' href='/issem/deleta/requerimento_sem_agendamento/"
        + id + "/'><i class='remove icon'></i>Sim</a>";
    document.getElementById("teste").innerHTML = html;
}

function atualiza_select_cargo(id_cargo) {
    $.ajax({
        type: 'POST',
        url: '/issem/atualiza/cargo/',
        data: {
            sec: $("input[name='cargo']").val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        dataType: 'json',
        success: function (dado) {
            var options = '';
            for (var i = dado.length - 1; i >= 0; i--) {
                options += '<option value="' + dado[i].pk + '">' + dado[i].fields['nome'] + '</option>';
            }
            console.log(dado);
            $("select#id_cargo").html(options);
        },
    });
}

function atualiza_select_secretaria(id_secretaria) {
    $.ajax({
        type: 'POST',
        url: '/issem/atualiza/secretaria/',
        data: {
            sec: $("input[name='secretaria']").val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        dataType: 'json',
        success: function (dado) {
            var options = '';
            for (var i = dado.length - 1; i >= 0; i--) {
                options += '<option value="' + dado[i].pk + '">' + dado[i].fields['nome'] + '</option>';
            }
            console.log(dado);
            $("select#id_secretaria").html(options);
        },
    });
}

function atualiza_select_local_trabalho(id_local_trabalho) {
    $.ajax({
        type: 'POST',
        url: '/issem/atualiza/local_trabalho/',
        data: {
            sec: $("input[name='local_trabalho']").val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        dataType: 'json',
        success: function (dado) {
            var options = '';
            for (var i = dado.length - 1; i >= 0; i--) {
                options += '<option value="' + dado[i].pk + '">' + dado[i].fields['nome'] + '</option>';
            }
            console.log(dado);
            $("select#id_local_trabalho").html(options);
        },
    });
}