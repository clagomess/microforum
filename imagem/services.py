# -*- coding: utf-8 -*-
from django.conf import settings
from django.utils import timezone
from django.utils.translation import ugettext as _

from PIL import Image, ImageOps
from boto.s3.connection import S3Connection
from boto.s3.key import Key

from core.models import Imagem

import hashlib
import os


def upload_service(filedata):
    the_name = hashlib.sha1(timezone.now().strftime("%H%M%S%f")).hexdigest() + ".jpg"
    to_return = {
        'status': True,
        'status_msg': None,
        'response': {}
    }

    tmp_name = timezone.now().strftime("%H%M%S%f") + str(filedata)
    bin_file = filedata.read()
    des_diretorio = timezone.now().strftime("/%Y/%m/%d/")

    to_return['response']['des_hash'] = hashlib.sha1(bin_file).hexdigest()
    to_return['response']['nom_imagem'] = the_name
    to_return['response']['des_diretorio'] = des_diretorio

    fp = open(settings.MEDIA_ROOT + tmp_name, 'w+')
    fp.write(bin_file)
    fp.close()

    image = None

    try:
        image = Image.open(settings.MEDIA_ROOT + tmp_name)
    except IOError:
        to_return['status'] = False
        to_return['status_msg'] = _(u"Imagem Inválida:")
        to_return['response'] = {}
        os.remove(settings.MEDIA_ROOT + tmp_name)

    rs_imagem = Imagem.objects.all().filter(
        des_hash=to_return['response']['des_hash']
    )

    if len(rs_imagem):
        to_return['response']['seq_imagem'] = rs_imagem[0].seq_imagem
        os.remove(settings.MEDIA_ROOT + tmp_name)

    if image and not len(rs_imagem):
        if image.mode not in ("L", "RGB"):
            image = image.convert("RGB")

        modes = [32, 50, 70, 300, 900]

        for mode in modes:
            mode_path = settings.MEDIA_ROOT + str(mode) + '_' + the_name

            if mode >= 300:
                image.thumbnail((mode, mode), Image.ANTIALIAS)
                image.save(mode_path, 'JPEG', quality=75)
            else:
                imagefit = ImageOps.fit(image, (mode, mode), Image.ANTIALIAS)
                imagefit.save(mode_path, 'JPEG', quality=75)

        os.remove(settings.MEDIA_ROOT + tmp_name)

        conn_s3 = S3Connection(
            settings.AMAZON_AWS.get('AWS_ACCESS_KEY_ID'),
            settings.AMAZON_AWS.get('AWS_SECRET_ACCESS_KEY')
        )

        s3_bucket = conn_s3.get_bucket(settings.AMAZON_AWS.get('S3_BUCKET'))

        for mode in modes:
            mode_path = settings.MEDIA_ROOT + str(mode) + '_' + the_name

            s3_key = Key(s3_bucket)
            s3_key.key = des_diretorio + str(mode) + '_' + the_name
            s3_key.set_contents_from_filename(mode_path)
            s3_key.set_acl('public-read')

            os.remove(mode_path)

        rs_imagem = Imagem(
            des_hash=to_return['response']['des_hash'],
            nom_imagem=to_return['response']['nom_imagem'],
            des_diretorio=to_return['response']['des_diretorio'],
            dat_cadastro=timezone.now(),
        )

        rs_imagem.save()
        to_return['response']['seq_imagem'] = rs_imagem.seq_imagem

    return to_return