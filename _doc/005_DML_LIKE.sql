insert into tb_like (
  seq_post,
  seq_usuario
)
SELECT
  (select seq_post from tb_post where gs=gs order by random() limit 1),
  (select seq_usuario from tb_usuario where gs=gs order by random() limit 1)
from generate_series(1,5000) as gs;