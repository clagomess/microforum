#!/usr/bin/python
import os

STATIC = os.path.dirname(os.path.abspath(__file__)) + "/../../webview/static/"

to_join_js = [
    'js/jquery-2.0.3.min.js',
    'js/jquery.uploadifive.min.js',
    'js/bootstrap.min.js'
]

to_join_css = [
    'css/bootstrap.min.css'
]

to_compress_js = [
    'js/core.js',
    'js/view_config.js',
    'js/view_profile.js'
]

to_compress_css = [
    'css/style.css'
]


def compress(to_join, to_compress, tipo):
    if len(to_compress):
        for itemfile in to_compress:
            source_name = STATIC + itemfile
            mini_name = STATIC + itemfile.replace('.' + tipo, '.min.' + tipo, 1)
            os.system("java -jar yuicompressor-2.4.8.jar {0} -o {1}".format(source_name, mini_name))
            to_join.append(mini_name.replace(STATIC, ''))


def joinfile(to_join, tipo):
    fpmain = open(STATIC + '{0}/main.{0}'.format(tipo), 'w+')
    fpmain.close()
    fpmain = open(STATIC + '{0}/main.{0}'.format(tipo), 'a')

    if len(to_join):
        for item in to_join:
            fp = open(STATIC + item)
            fpmain.write("/* " + item + " */\n")
            fpmain.write(fp.read())
            fpmain.write("\n\n")
            fp.close()

    fpmain.close()

compress(to_join_css, to_compress_css, 'css')
compress(to_join_js, to_compress_js, 'js')

joinfile(to_join_css, 'css')
joinfile(to_join_js, 'js')

