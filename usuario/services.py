# -*- coding: utf-8 -*-
from core.models import Usuario
from usuario.dao import get_usuario_dao
from django.utils.translation import ugettext as _
from django.utils import timezone

import hashlib
import re


def login_service(param):
    to_return = None

    if param.get('des_email') and param.get('des_senha'):
        to_return = Usuario.objects.all().filter(
            des_email=param.get('des_email'),
            des_senha=hashlib.sha1(param.get('des_senha')).hexdigest(),
        )

    if to_return:
        usuario = Usuario.objects.get(
            seq_usuario=to_return[0].seq_usuario
        )

        usuario.dat_ultimo_acesso = timezone.now()
        usuario.save()

        to_return = to_return[0]

    return to_return


def get_usuario_service(param):
    return get_usuario_dao(param)


def manter_usuario_service(acao, param, auth):
    """
    :param acao: (novo, alterar)
    :param param: dados para persistir
    :param auth: sessao
    :return: dict
    """
    to_return = {
        'status': True,
        'status_msg': [],
        'response': None
    }

    if len(str(param.get('nom_usuario'))) <= 4:
        to_return['status_msg'].append(_(u"Nome inválido!"))
        to_return['status'] = False

    if not len(str(param.get('des_senha'))) >= 6 and len(str(param.get('des_senha'))) <= 20:
        to_return['status_msg'].append(_(u"A senha deve ter de 6 a 20 caracteres!"))
        to_return['status'] = False

    if str(param.get('des_senha')) != str(param.get('des_senha_r')):
        to_return['status_msg'].append(_(u"As senhas não são iguais!"))
        to_return['status'] = False

    if acao == 'novo':
        if not re.match('([a-z0-9.-_]*?)@([a-z]*?)\.([a-z\.]*?)', str(param.get('des_email'))):
            to_return['status_msg'].append(_(u"Este e-mail parece ser inválido!"))
            to_return['status'] = False
        else:
            if Usuario.objects.all().filter(des_email=str(param.get('des_email'))):
                to_return['status_msg'].append(_(u"Já existe alguém usando esse email"))
                to_return['status'] = False

        if str(param.get('sit_termo')) != 'S':
            to_return['status_msg'].append(_(u"Para se cadastrar, é necessário ler e concordar com os termos"))
            to_return['status'] = False

    if acao == 'alterar':
        if hashlib.sha1(str(param.get('des_senha_atual'))).hexdigest() != auth.get('des_senha'):
            to_return['status_msg'].append(_(u"Sua senha está incorreta!"))
            to_return['status'] = False

    return to_return