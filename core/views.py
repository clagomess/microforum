# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.utils import timezone
import hashlib
import base64
import json
from core.models import Imagem
from core.models import Usuario
from core.models import Post
from core.models import Like
from core.models import Notificacao
from core.models import Seguidor


def test(request):
    template = """
    <strong>{0}:</strong><br>
    Result: {1}<br>
    <hr>
    """

    response = "<h1>TESTE:</h1>"

    Imagem(
        seq_imagem=1,
        des_hash=hashlib.sha1("foo").hexdigest(),
        nom_imagem=hashlib.sha1("foo").hexdigest() + ".jpg",
        des_diretorio="/2015/01/07/",
        dat_cadastro=timezone.now(),
    ).save()

    response = response + template.format(
        'Imagem',
        Imagem.objects.get(seq_imagem=1)
    )

    Usuario(
        seq_usuario=1,
        seq_imagem=Imagem(seq_imagem=1),
        cod_usuario="clagomess",
        nom_usuario=u"Cláudio Gomes",
        des_email="cla.gomess@gmail.com",
        des_senha=hashlib.sha1("010203").hexdigest(),
        dat_cadastro=timezone.now(),
        dat_ultimo_acesso=timezone.now()
    ).save()

    response = response + template.format(
        'Usuario',
        Usuario.objects.get(seq_usuario=1)
    )

    Post(
        seq_post=1,
        seq_usuario=Usuario(seq_usuario=1),
        cod_post=base64.b64encode(timezone.now().strftime("%H%M%S%f")).replace("=", ''),
        des_post=u"Olá Amiguinhos!",
        dat_post=timezone.now()
    ).save()

    response = response + template.format(
        'Post',
        Post.objects.get(seq_post=1)
    )

    Like(
        seq_like=1,
        seq_post=Post(seq_post=1),
        seq_usuario=Usuario(seq_usuario=1)
    ).save()

    response = response + template.format(
        'Like',
        Like.objects.get(seq_like=1)
    )

    Notificacao(
        seq_notificacao=1,
        seq_usuario=Usuario(seq_usuario=1),
        dat_notificacao=timezone.now()
    ).save()

    response = response + template.format(
        'Notificacao',
        Notificacao.objects.get(seq_usuario=1)
    )

    Seguidor(
        seq_seguidor=1,
        seq_usuario_seguidor=Usuario(seq_usuario=1),
        seq_usuario_seguido=Usuario(seq_usuario=1),
        dat_seguidor=timezone.now()
    ).save()

    response = response + template.format(
        'Seguidor',
        Seguidor.objects.get(seq_seguidor=1)
    )

    return HttpResponse(response)


def test_json(request):
    from usuario.services import manter_usuario_service
    response = json.dumps(manter_usuario_service(
        'alterar',
        {
        },
        request.session.get('twa_auth')
    ))

    return HttpResponse(response, content_type="application/json")