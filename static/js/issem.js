$(document).ready(function () {


    $('.ui.modal')
        .modal('setting', 'closable', false)
        .modal('attach events', '#cadastro-secretaria', 'show');
    });