DO
$do$
DECLARE
  c1 CURSOR FOR
  select seq_usuario, cnt_seguidor,  cnt_seguindo from
  (select count(*) as cnt_seguidor, seq_usuario_seguido as seq_usuario from tb_seguidor GROUP BY seq_usuario_seguido) as vtba
  left join (
    select count(*) as cnt_seguindo, seq_usuario_seguidor from tb_seguidor GROUP BY seq_usuario_seguidor
  ) as vtbb on vtbb.seq_usuario_seguidor = vtba.seq_usuario;
BEGIN
  for item in c1 loop
  update tb_usuario set num_seguidor = item.cnt_seguidor,
    num_seguindo = COALESCE(item.cnt_seguindo, 0)
  where seq_usuario = COALESCE(item.seq_usuario, 0);
  end loop;
END;
$do$;

DO
$do$
DECLARE
  c1 CURSOR FOR
  SELECT
  count(*)     AS cnt_post,
  seq_post_pai AS seq_post
  FROM tb_post
  WHERE seq_post_pai IS NOT NULL
  GROUP BY seq_post_pai;
BEGIN
  for item in c1 loop
  update tb_post set num_post_filho = item.cnt_post where seq_post = item.seq_post;
  end loop;
END;
$do$;

DO
$do$
DECLARE
  c1 CURSOR FOR
  select count(*) as cnt_like, seq_post from tb_like
  GROUP BY seq_post;
BEGIN
  for item in c1 loop
  update tb_post set num_like = item.cnt_like where seq_post = item.seq_post;
  end loop;
END;
$do$;