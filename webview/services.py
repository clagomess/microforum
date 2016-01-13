from core.models import Imagem


def get_log():
    sql = """
    SELECT DISTINCT
        attk.cnt,
        tl.seq_log,
        tl.tx_ip,
        tl.tx_usuario,
        tl.dt_log,
        tl.tx_comando,
        tl.tx_endereco,
        tl.tx_agent,
        tl.tx_http_status,
        tl.tx_response_lenght
      FROM tb_log tl
      JOIN tb_log_hash tlh ON tlh.seq_log = tl.seq_log
      JOIN (
        SELECT tl_1.tx_ip,
        tlh_1.tx_hs_comando,
        count(*) AS cnt
        FROM tb_log tl_1
        JOIN tb_log_hash tlh_1 ON tl_1.seq_log = tlh_1.seq_log
        GROUP BY tl_1.tx_ip, tlh_1.tx_hs_comando
        HAVING count(*) > 2
      ) attk
        ON attk.tx_ip = tl.tx_ip
        AND attk.tx_hs_comando = tlh.tx_hs_comando
      ORDER BY attk.cnt DESC
      LIMIT 10
    """

    return Imagem.objects.raw(sql)