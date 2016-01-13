$(document).ready(function () {
    $('#imagem').uploadifive({
        'auto': true,
        'queueID': 'queue',
        'formData': {
            'tipo': 'usuario'
        },
        'buttonText': 'Selecionar Foto',
        'uploadScript': "/upload",
        'multi':false,
        'onQueueComplete': function () {
            $('#imagem').uploadifive('clearQueue');
        },
        'onUploadComplete': function (file, data) {

        }
    });
});