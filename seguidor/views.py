from django.http import HttpResponse
from django.utils import timezone

import json

from core.models import Seguidor
from core.models import Usuario

default_response = {
    'status': True,
    'status_msg': None,
    'response': None
}


def seguir(resquest):
    response = default_response

    if resquest.method == 'POST':
        if resquest.POST.get('modo') == 'seguir':
            Seguidor(
                seq_usuario_seguidor=Usuario.objects.get(seq_usuario=resquest.session.get('twa_auth').get('seq_usuario')),
                seq_usuario_seguido=Usuario.objects.get(cod_usuario=resquest.POST.get('cod_usuario')),
                dat_seguidor=timezone.now()
            ).save()

            # @TODO: Disparar email, de preferencia transformar em services

        if resquest.POST.get('modo') == 'naoseguir':
            Seguidor.objects.get(
                seq_usuario_seguidor=Usuario.objects.get(seq_usuario=resquest.session.get('twa_auth').get('seq_usuario')),
                seq_usuario_seguido=Usuario.objects.get(cod_usuario=resquest.POST.get('cod_usuario'))
            ).delete()

    return HttpResponse(json.dumps(response), content_type="application/json")