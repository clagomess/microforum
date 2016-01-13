from django.db import connection
from core.dao import dictfetchall


def get_usuario_dao(param):
    sql = """
    SELECT
      tbu.seq_usuario,
      tbu.cod_usuario,
      tbu.nom_usuario,
      tbu.num_seguidor,
      tbu.num_seguindo,
      tbi.nom_imagem,
      tbi.des_diretorio,
      tbs.dat_seguidor AS dat_seguindo -- vinculo com auth
    FROM tb_usuario tbu
    LEFT JOIN tb_imagem tbi
      ON tbi.seq_imagem = tbu.seq_imagem
    LEFT JOIN tb_seguidor tbs
      ON tbs.seq_usuario_seguido = tbu.seq_usuario
      AND tbs.seq_usuario_seguidor = %(seq_usuario_auth)s
    WHERE tbu.sit_ativo = 1
    """

    bind_param = {
        'seq_usuario_auth': param.get('seq_usuario_auth')
    }

    bind_sql = []

    if param.get('seq_usuario'):
        bind_param['seq_usuario'] = param.get('seq_usuario')
        bind_sql.append("AND tbu.seq_usuario = %(seq_usuario)s")

    if param.get('cod_usuario'):
        bind_param['cod_usuario'] = param.get('cod_usuario')
        bind_sql.append("AND tbu.cod_usuario = %(cod_usuario)s")

    sql += "\n".join(tuple(bind_sql))

    if len(bind_param):
        cursor = connection.cursor()
        cursor.execute(sql, bind_param)
        to_return = dictfetchall(cursor)

        if len(to_return):
            to_return = to_return[0]
    else:
        to_return = {}

    return to_return