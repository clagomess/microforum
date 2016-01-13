$(document).ready(function () {
    var focused = true;

    window.onblur = function () {
        focused = false;
    };

    window.onfocus = function (){
        focused = true;
    };

    // CRON JOB
    window.setInterval(function(){

    }, 1000 * 8);
});

function fn_seguir(botao){
    $(botao).fadeTo('fast', 0.5);

    $.ajax({
        url: '/seguidor/seguir/',
        type: "POST",
        dataType: 'JSON',
        data: {
            cod_usuario: $(botao).attr('cod_usuario'),
            modo: $(botao).attr('modo')
        },
        success: function (jx) {
            console.log(jx);

            $(botao).fadeTo('fast', 1);
        }
    });
}