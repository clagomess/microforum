CREATE TABLE randomwords (
  palavra VARCHAR(100)
);

INSERT INTO randomwords VALUES('Mussum ipsum');
INSERT INTO randomwords VALUES('litro abertis.');
INSERT INTO randomwords VALUES('elitis. Pra');
INSERT INTO randomwords VALUES('depois divoltis');
INSERT INTO randomwords VALUES('Paisis, filhis,');
INSERT INTO randomwords VALUES('Mé faiz');
INSERT INTO randomwords VALUES('nisi eros');
INSERT INTO randomwords VALUES('elementis mé');
INSERT INTO randomwords VALUES('é amistosis');
INSERT INTO randomwords VALUES('Manduma pindureta');
INSERT INTO randomwords VALUES('nois paga.');
INSERT INTO randomwords VALUES('monti palavris');
INSERT INTO randomwords VALUES('significa nadis');
INSERT INTO randomwords VALUES('latim. Interessantiss');
INSERT INTO randomwords VALUES('ce receita');
INSERT INTO randomwords VALUES('mais bolis');
INSERT INTO randomwords VALUES('Suco de');
INSERT INTO randomwords VALUES('um leite');
INSERT INTO randomwords VALUES('tem lupuliz,');
INSERT INTO randomwords VALUES('e fermentis.');
INSERT INTO randomwords VALUES('mé, cursus');
INSERT INTO randomwords VALUES('ac nisi.');
INSERT INTO randomwords VALUES('dui dui.');
INSERT INTO randomwords VALUES('erat, aliquet');
INSERT INTO randomwords VALUES('a, posuere');
INSERT INTO randomwords VALUES('Ut scelerisque');
INSERT INTO randomwords VALUES('turpis posuere');
INSERT INTO randomwords VALUES('nibh ullamcorper.');
INSERT INTO randomwords VALUES('mattis molestie,');
INSERT INTO randomwords VALUES('justo. Aenean');
INSERT INTO randomwords VALUES('turpis. Pellentesque');
INSERT INTO randomwords VALUES('vel lectus');
INSERT INTO randomwords VALUES('cursus velit');
INSERT INTO randomwords VALUES('ipsum dolor');
INSERT INTO randomwords VALUES('consectetur adipiscing');
INSERT INTO randomwords VALUES('ac mauris');
INSERT INTO randomwords VALUES('scelerisque augue.');
INSERT INTO randomwords VALUES('Casamentiss faiz');
INSERT INTO randomwords VALUES('pirulitá, Nam');
INSERT INTO randomwords VALUES('cum soluta');
INSERT INTO randomwords VALUES('option congue');
INSERT INTO randomwords VALUES('doming id');
INSERT INTO randomwords VALUES('placerat facer');
INSERT INTO randomwords VALUES('Lorem ipsum');
INSERT INTO randomwords VALUES('amet, consectetuer');
INSERT INTO randomwords VALUES('mé intende');
INSERT INTO randomwords VALUES('golada, vinho,');
INSERT INTO randomwords VALUES('rum da');
INSERT INTO randomwords VALUES('num pode');
INSERT INTO randomwords VALUES('Adipiscing elit,');
INSERT INTO randomwords VALUES('nonummy nibh');
INSERT INTO randomwords VALUES('ut laoreet');
INSERT INTO randomwords VALUES('aliquam erat');
INSERT INTO randomwords VALUES('wisi enim');
INSERT INTO randomwords VALUES('veniam, quis');
INSERT INTO randomwords VALUES('tation ullamcorper');
INSERT INTO randomwords VALUES('nisl ut');
INSERT INTO randomwords VALUES('ea commodo consequat.');
INSERT INTO randomwords VALUES('Cevadis im');
INSERT INTO randomwords VALUES('arma uma');
INSERT INTO randomwords VALUES('varius eleifend');
INSERT INTO randomwords VALUES('viverra nisl');
INSERT INTO randomwords VALUES('Donec eget');
INSERT INTO randomwords VALUES('Atirei o');
INSERT INTO randomwords VALUES('gatis. Viva');
INSERT INTO randomwords VALUES('taciti sociosqu');
INSERT INTO randomwords VALUES('torquent per');
INSERT INTO randomwords VALUES('per inceptos');
INSERT INTO randomwords VALUES('furadis é');
INSERT INTO randomwords VALUES('babadis, arcu');
INSERT INTO randomwords VALUES('magna, bibendum');
INSERT INTO randomwords VALUES('arcu ut');
INSERT INTO randomwords VALUES('gente finis.');
INSERT INTO randomwords VALUES('amet mattis');
INSERT INTO randomwords VALUES('Paisis, filhis,');
INSERT INTO randomwords VALUES('Mé faiz');
INSERT INTO randomwords VALUES('Pellentesque viverra');
INSERT INTO randomwords VALUES('elementum gravidis.');
INSERT INTO randomwords VALUES('Forevis aptent');
INSERT INTO randomwords VALUES('ad litora');
INSERT INTO randomwords VALUES('conubia nostra,');
INSERT INTO randomwords VALUES('himenaeos. Copo');
INSERT INTO randomwords VALUES('disculpa de');
INSERT INTO randomwords VALUES('quam euismod');
INSERT INTO randomwords VALUES('egestas augue');
INSERT INTO randomwords VALUES('est. Etiam');
INSERT INTO randomwords VALUES('ligula, sed');
INSERT INTO randomwords VALUES('mollis et.');
INSERT INTO randomwords VALUES('finis. In');
INSERT INTO randomwords VALUES('mattis porris,');
INSERT INTO randomwords VALUES('filhis, espiritis');
INSERT INTO randomwords VALUES('faiz elementum');
INSERT INTO randomwords VALUES('viverra accumsan');
INSERT INTO randomwords VALUES('gravida. Quisque');
INSERT INTO randomwords VALUES('id massa');
INSERT INTO randomwords VALUES('sed sed');
INSERT INTO randomwords VALUES('viverra lobortis');
INSERT INTO randomwords VALUES('et turpis.');
INSERT INTO randomwords VALUES('Vitis e');
INSERT INTO randomwords VALUES('Nam varius');
INSERT INTO randomwords VALUES('sed viverra');
INSERT INTO randomwords VALUES('ut. Donec');
INSERT INTO randomwords VALUES('enim. Atirei');
INSERT INTO randomwords VALUES('no gatis.');
INSERT INTO randomwords VALUES('felis quis');
INSERT INTO randomwords VALUES('varius tempor');
INSERT INTO randomwords VALUES('Vivamus lobortis');
INSERT INTO randomwords VALUES('Sed auctor');
INSERT INTO randomwords VALUES('sapien sagittis');
INSERT INTO randomwords VALUES('semper accumsan');
INSERT INTO randomwords VALUES('aliquam nisl');
INSERT INTO randomwords VALUES('Nullam pellentesque');
INSERT INTO randomwords VALUES('libero laoreet');
INSERT INTO randomwords VALUES('ante ultricies.');
INSERT INTO randomwords VALUES('mollis purus.');
INSERT INTO randomwords VALUES('lacus dolor.');
INSERT INTO randomwords VALUES('mi nec');
INSERT INTO randomwords VALUES('ullamcorper vel');
INSERT INTO randomwords VALUES('Nulla et');

insert into tb_usuario (
  seq_imagem,
  cod_usuario,
  nom_usuario,
  des_email,
  des_senha,
  dat_cadastro,
  dat_ultimo_acesso,
  num_seguidor,
  num_seguindo,
  sit_ativo,
  sit_plus,
  sit_email,
  seq_pais
)
SELECT
  (select seq_imagem from tb_imagem where gs=gs order by random() limit 1),
  to_char(cast(now() - '1 year'::interval * random()  as TIMESTAMPTZ), 'YYMMDDHH24MIMSUS'),
  (select replace(replace(palavra, '.', ''),',','') from randomwords where gs=gs ORDER BY random() limit 1),
  to_char(cast(now() - '1 year'::interval * random()  as TIMESTAMPTZ), 'YYMMDDHH24MIMSUS') || '@foo.bar',
  md5('010203'),
  cast(now() - '1 year'::interval * random()  as TIMESTAMPTZ),
  cast(now() - '1 year'::interval * random()  as TIMESTAMPTZ),
  0, 0, 1, 0, 1,
  (select seq_pais from tb_pais where gs=gs order by random() limit 1)
from generate_series(1,8000) as gs;

drop TABLE randomwords;