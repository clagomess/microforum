insert into tb_imagem (
  des_hash,
  nom_imagem,
  des_diretorio,
  dat_cadastro
)
  SELECT
    to_char(cast(now() - '1 year'::interval * random()  as TIMESTAMPTZ), 'YYMMDDHH24MIMS'),
    to_char(cast(now() - '1 year'::interval * random()  as TIMESTAMPTZ), 'YYMMDDHH24MIMS') || '.jpg',
    TO_CHAR(cast(now() - '1 year'::interval * random()  as TIMESTAMPTZ), '/YYYY/MM/DD/'),
    cast(now() - '1 year'::interval * random()  as TIMESTAMPTZ)
  from generate_series(1, 10000) as gs;