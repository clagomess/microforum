from django.db import connection
from core.dao import dictfetchall


def get_post_dao(param):
    """
    param {
        tipo: 'amigo', 'rede', 'filho'+seq_post_pai
        #ou campos definidos#
        seq_post_pai, seq_post, seq_usuario

        dat_post: > ?
        limit: (default 10)
        offset: (default 0)
    }
    """
    sql = """
    SELECT
      tpp.seq_post,
      tpp.seq_post_pai,
      tpp.cod_post,
      tpp.des_post,
      tpp.dat_post,
      tpp.num_like,
      tpp.num_post_filho,
      tbip.des_diretorio AS des_diretorio_post,
      tbip.nom_imagem AS nom_imagem_post,
      tbu.seq_usuario,
      tbu.cod_usuario,
      tbu.nom_usuario,
      tbiu.des_diretorio AS des_diretorio_usuario,
      tbiu.nom_imagem AS nom_imagem_usuario
    FROM tb_post AS tpp
    JOIN tb_usuario AS tbu
      ON tbu.seq_usuario = tpp.seq_usuario
    LEFT JOIN tb_imagem AS tbip
      ON tbip.seq_imagem = tpp.seq_imagem
    LEFT JOIN tb_imagem AS tbiu
      ON tbiu.seq_imagem = tbu.seq_imagem
    """

    bind_param = {}
    bind_sql = []

    if param.get('tipo') == 'amigo':
        bind_param['seq_usuario'] = param.get('seq_usuario')
        bind_sql.append("""
        JOIN tb_seguidor tbs
          ON tbs.seq_usuario_seguidor = %(seq_usuario)s
          AND tbs.seq_usuario_seguido = tbu.seq_usuario
        """)

    if param.get('tipo') == 'filho':
        bind_sql.append("""
        JOIN (
            SELECT
              row_number() OVER(PARTITION BY seq_post_pai ORDER BY dat_post DESC) AS rownum,
              seq_post
            FROM tb_post
            WHERE seq_post_pai IN(%s)
        ) vtb
            ON vtb.seq_post = tpp.seq_post
            AND vtb.rownum <= 3
        """ % ", ".join(str(seq) for seq in param.get('seq_post_pai')))

    bind_sql.append("\nWHERE 1=1\n")

    if param.get('seq_post_pai') and not param.get('tipo'):
        bind_param['seq_post_pai'] = param.get('seq_post_pai')
        bind_sql.append("AND tpp.seq_post_pai = %(seq_post_pai)s")
    else:
        if param.get('tipo') != 'filho':
            bind_sql.append("AND tpp.seq_post_pai IS NULL")

    if param.get('seq_post'):
        bind_param['seq_post'] = param.get('seq_post')
        bind_sql.append("AND tpp.seq_post = %(seq_post)s")

    if param.get('cod_post'):
        bind_param['cod_post'] = param.get('cod_post')
        bind_sql.append("AND tpp.cod_post = %(cod_post)s")

    if param.get('seq_usuario') and not param.get('tipo'):
        bind_param['seq_usuario'] = param.get('seq_usuario')
        bind_sql.append("AND tbu.seq_usuario = %(seq_usuario)s")

    if param.get('dat_post'):
        bind_param['dat_post'] = param.get('dat_post')
        bind_sql.append("AND tpp.dat_post > %(dat_post)s")

    if param.get('seq_pais'):
        bind_param['seq_pais'] = param.get('seq_pais')
        bind_sql.append("AND tbu.seq_pais = %(seq_pais)s")

    if param.get('tipo') == 'amigo':
        bind_param['seq_usuario'] = param.get('seq_usuario')
        bind_sql.append("AND tbu.seq_usuario <> %(seq_usuario)s")

    if 'limit' not in param:
        param['limit'] = 10

    if 'offset' not in param:
        param['offset'] = 0

    bind_param['offset'] = param.get('offset')
    bind_param['limit'] = param.get('limit')

    bind_sql.append("""
    ORDER BY tpp.dat_post DESC
    OFFSET %(offset)s
    LIMIT %(limit)s
    """)

    sql += "\n".join(tuple(bind_sql))

    cursor = connection.cursor()
    cursor.execute(sql, bind_param)

    return dictfetchall(cursor)