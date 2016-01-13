from django import template
from django.conf import settings
register = template.Library()


@register.inclusion_tag('partial_li_post.html')
def li_post(post, auth):
    return {
        'post': post,
        'auth': auth
    }


@register.inclusion_tag('partial_box_publicar.html')
def box_publicar():
    return {}


@register.inclusion_tag('partial_box_usuario.html')
def box_usuario(usuario, perfil, auth, seguindo, seguidores):
    """
    :param usuario: dict com dados do usuario
    :param perfil: boolean se a partial e para home ou perfil
    :param auth: dict dados sessao
    :param seguindo: dict seguindo
    :param seguidores: dict seguidores
    """
    return {
        'usuario': usuario,
        'perfil': perfil,
        'auth': auth,
        'seguindo': seguindo,
        'seguidores': seguidores
    }


@register.inclusion_tag('partial_img_usuario.html')
def img_usuario(nom_imagem, des_diretorio, size):
    return {
        'S3_BUCKET': settings.AMAZON_AWS.get('S3_BUCKET'),
        'nom_imagem': nom_imagem,
        'des_diretorio': des_diretorio,
        'size': size
    }

@register.inclusion_tag('partial_bt_seguir.html')
def bt_seguir(vinculo, cod_usuario):
    return {
        'vinculo': vinculo,
        'cod_usuario': cod_usuario
    }


@register.inclusion_tag('partial_li_grid.html')
def li_grid(seguidor):
    return {
        'seguidor': seguidor
    }


@register.inclusion_tag('partial_mail_codecadastro.html')
def mail_codecadastro():
    return {}


@register.inclusion_tag('partial_mail_novocadastro.html')
def mail_novocadastro():
    return {}