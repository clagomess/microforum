from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.utils.translation import ugettext as _
from django.views.decorators.cache import cache_page
from django.views.decorators.cache import never_cache
from django.conf import settings

import json

from usuario.services import login_service
from post.services import get_post_service
from usuario.services import get_usuario_service
from seguidor.services import get_seguidor_service
from imagem.services import upload_service

from core.models import Usuario
from core.models import Imagem

layoutparam = {
    'title': 'Trash Of WEB',
    'description': _("Uma rede social de postagens publicas simples e underground."),
    'keywords': _("rede, social, network, socialmedia"),
    'favicon': 'img/favicon.png',
    'contextpage': 'public',
    'contentsize': None,
    'production': settings.PRODUCTION
}


def check_auth(request):
    if request.session.get('twa_auth'):
        to_return = None
    else:
        to_return = HttpResponseRedirect('/')

    return to_return


def index(request):
    response = None
    loginerror = False
    layoutparam['contextpage'] = 'index'
    layoutparam['contentsize'] = 800

    if not request.session.get('twa_auth'):
        if request.META['REQUEST_METHOD'] == 'POST':
            usuario = login_service({
                'des_email': request.POST.get('twa_email'),
                'des_senha': request.POST.get('twa_senha')
            })

            if usuario:
                request.session['twa_auth'] = {
                    'seq_usuario': usuario.seq_usuario,
                    'cod_usuario': usuario.cod_usuario,
                    'des_senha': usuario.des_senha,
                    'seq_pais': usuario.seq_pais.seq_pais
                }

                response = HttpResponseRedirect('/home/')
            else:
                loginerror = True

    else:
        response = HttpResponseRedirect('/home/')

    if not response:
        response = render(request, 'view_index.html', {
            'layoutparam': layoutparam,
            'twa_email': request.POST.get('twa_email'),
            'loginerror': loginerror
        })

    return response


@never_cache
def home(request):
    response = check_auth(request)

    layoutparam['contextpage'] = None
    layoutparam['contentsize'] = None

    if not response:
        friend_post = get_post_service({
            'tipo': 'amigo',
            'seq_usuario': request.session.get('twa_auth').get('seq_usuario')
        })

        network_post = get_post_service({
            'seq_pais': request.session.get('twa_auth').get('seq_pais')
        })

        usuario = get_usuario_service({
            'seq_usuario': request.session.get('twa_auth').get('seq_usuario'),
            'seq_usuario_auth': None
        })

        seguindo = get_seguidor_service({
            'tipo': 'seguindo',
            'seq_usuario': request.session.get('twa_auth').get('seq_usuario')
        })

        seguidores = get_seguidor_service({
            'tipo': 'seguidores',
            'seq_usuario': request.session.get('twa_auth').get('seq_usuario')
        })

        response = render(request, 'view_home.html', {
            'layoutparam': layoutparam,
            'friend_post': friend_post,
            'network_post': network_post,
            'auth': request.session.get('twa_auth'),
            'usuario': usuario,
            'seguindo': seguindo,
            'seguidores': seguidores
        })

    return response


def post(request, cod_post):
    layoutparam['contextpage'] = 'content'
    layoutparam['contentsize'] = 400

    if not request.session.get('twa_auth'):
        layoutparam['contextpage'] = 'public'

    rs_post = get_post_service({
        'cod_post': cod_post
    })

    if len(rs_post):
        response = render(request, 'view_post.html', {
            'layoutparam': layoutparam,
            'post': rs_post,
            'auth': request.session.get('twa_auth')
        })
    else:
        response = render(request, 'view_404.html', {
            'layoutparam': layoutparam,
            'request': request
        })

    return response


def profile(request, cod_usuario):
    layoutparam['contextpage'] = 'content'
    layoutparam['contentsize'] = 800

    if not request.session.get('twa_auth'):
        layoutparam['contextpage'] = 'public'

    usuario = get_usuario_service({
        'cod_usuario': cod_usuario,
        'seq_usuario_auth': request.session.get('twa_auth').get('seq_usuario')
    })

    if len(usuario):
        post_usuario = get_post_service({
            'seq_usuario': usuario.get('seq_usuario')
        })

        seguindo = get_seguidor_service({
            'tipo': 'seguindo',
            'seq_usuario': usuario.get('seq_usuario')
        })

        seguidores = get_seguidor_service({
            'tipo': 'seguidores',
            'seq_usuario': usuario.get('seq_usuario')
        })

        response = render(request, 'view_profile.html', {
            'layoutparam': layoutparam,
            'auth': request.session.get('twa_auth'),
            'usuario': usuario,
            'post': post_usuario,
            'seguindo': seguindo,
            'seguidores': seguidores
        })
    else:
        response = render(request, 'view_404.html', {
            'layoutparam': layoutparam,
            'request': request
        })

    return response


def config(request):
    response = check_auth(request)

    layoutparam['contextpage'] = 'content'
    layoutparam['contentsize'] = None

    if not response:
        usuario = get_usuario_service({
            'seq_usuario': request.session.get('twa_auth').get('seq_usuario'),
            'seq_usuario_auth': None
        })

        response = render(request, 'view_config.html', {
            'layoutparam': layoutparam,
            'usuario': usuario
        })

    return response


def upload(request):
    response = []

    if request.method == 'POST':
        if request.FILES.get('Filedata'):
            response = upload_service(request.FILES.get('Filedata'))

            if response.get('status'):
                if request.POST.get('tipo') == 'usuario':
                    rs_usuario = Usuario.objects.get(
                        seq_usuario=request.session.get('twa_auth').get('seq_usuario')
                    )

                    rs_usuario.seq_imagem = Imagem(
                        seq_imagem=response.get('response').get('seq_imagem')
                    )

                    rs_usuario.save()

    return HttpResponse(json.dumps(response), content_type="application/json")


def logout(request):
    request.session.flush()
    return HttpResponseRedirect('/')
