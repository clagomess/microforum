from django.db import connection
from core.dao import dictfetchall


def get_seguidor_dao(param):
    sql = """
    SELECT
        tbu.seq_usuario,
        tbu.cod_usuario,
        tbu.nom_usuario,
        tbi.nom_imagem,
        tbi.des_diretorio
    FROM tb_seguidor tbs
        JOIN tb_usuario tbu
    """

    if param.get('tipo') == 'seguindo':
        sql += """
        -- seguindo
        ON tbu.seq_usuario = tbs.seq_usuario_seguido
        """
    if param.get('tipo') == 'seguidores':
        sql += """
        -- seguidores
        ON tbu.seq_usuario = tbs.seq_usuario_seguidor
        """

    sql += """
    LEFT JOIN tb_imagem tbi
        ON tbi.seq_imagem = tbu.seq_imagem
    WHERE
    """

    if param.get('tipo') == 'seguindo':
        sql += """
        -- seguindo
        tbs.seq_usuario_seguidor = %(seq_usuario)s
        """

    if param.get('tipo') == 'seguidores':
        sql += """
        -- seguidores
        tbs.seq_usuario_seguido = %(seq_usuario)s
        """

    sql += """
    ORDER BY tbs.dat_seguidor DESC
    OFFSET 0
    LIMIT 12
    """

    bind_param = {
        'seq_usuario': param.get('seq_usuario')
    }

    if len(bind_param):
        cursor = connection.cursor()
        cursor.execute(sql, bind_param)
        to_return = dictfetchall(cursor)
    else:
        to_return = []

    return to_return