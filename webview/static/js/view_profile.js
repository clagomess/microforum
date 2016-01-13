$(document).ready(function(){
    $('#bt-seguidor a').click(function(e){
        e.preventDefault();

        fn_seguir($(this));
    })
});