  $(document).ready(function(){

    $('.fazul').click(function(){

        id = $(this).attr('id')
        $('.'+id).transition('slide down')
    })

  })

  function formatar(mascara, documento){
  var i = documento.value.length;
  var saida = mascara.substring(0,1);
  var texto = mascara.substring(i)

  if (texto.substring(0,1) != saida){
            documento.value += texto.substring(0,1);
  }

}