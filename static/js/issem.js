  $(document).ready(function(){

    $('.fazul').click(function(){

        id = $(this).attr('id')
        $('.'+id).transition('slide down')
    })

  })