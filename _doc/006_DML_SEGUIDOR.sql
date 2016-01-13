insert into tb_seguidor (
  seq_usuario_seguidor,
  seq_usuario_seguido,
  dat_seguidor
)
SELECT
  (select seq_usuario from tb_usuario where gs=gs order by random() limit 1),
  (select seq_usuario from tb_usuario where gs=gs order by random() limit 1),
  cast(now() - '1 year'::interval * random()  as TIMESTAMPTZ)
from generate_series(1,10000) as gs;