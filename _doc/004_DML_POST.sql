CREATE TABLE randomwords (
  palavra VARCHAR(4000)
);

INSERT INTO randomwords VALUES('Mussum ipsum cacilds, vidis litro abertis. Consetis adipiscings elitis. Pra lá , depois divoltis porris,paradis.');
INSERT INTO randomwords VALUES('Paisis, filhis, espiritis santis. Mé faiz elementum girarzis, nisi eros vermeio, in elementis mépra quem');
INSERT INTO randomwords VALUES('é amistosis quis leo. Manduma pindureta quium dia nois paga. Sapien in montipalavris qui num significa nadis i pareci latim. Interessantiss quisso pudia ce receita de bolis,mais bolis eu num');
INSERT INTO randomwords VALUES('gostis.');
INSERT INTO randomwords VALUES('Suco de cevadiss, é um leite divinis, qui tem lupuliz, matis, aguis e fermentis. Interagino');
INSERT INTO randomwords VALUES('mé, cursus quis, vehicula ac nisi. Aenean vel dui dui. Nullam leo erat, aliquetquis tempus');
INSERT INTO randomwords VALUES('a, posuere ut mi. Ut scelerisque neque et turpis posuere pulvinar pellentesque nibhullamcorper. Pharetra in');
INSERT INTO randomwords VALUES('mattis molestie, volutpat elementum justo. Aenean ut ante turpis. Pellentesque laoreet mével lectus scelerisque interdum');
INSERT INTO randomwords VALUES('cursus velit auctor. Lorem ipsum dolor sit amet, consectetur adipiscing elit.Etiam ac mauris lectus, non');
INSERT INTO randomwords VALUES('scelerisque augue. Aenean justo massa.');
INSERT INTO randomwords VALUES('Casamentiss faiz malandris se pirulitá, Nam liber tempor cum soluta nobis eleifend option congue nihilimperdiet');
INSERT INTO randomwords VALUES('doming id quod mazim placerat facer possim assum. Lorem ipsum dolor sit amet, consectetuerIspecialista im');
INSERT INTO randomwords VALUES('mé intende tudis nuam golada, vinho, uiski, carirí, rum da jamaikis, só numpode ser mijis.');
INSERT INTO randomwords VALUES('Adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magnaaliquam erat volutpat. Ut');
INSERT INTO randomwords VALUES('wisi enim ad minim veniam, quis nostrud exerci tation ullamcorper suscipitlobortis nisl ut aliquip ex');
INSERT INTO randomwords VALUES('ea commodo consequat.');
INSERT INTO randomwords VALUES('Cevadis im ampola pa arma uma pindureta. Nam varius eleifend orci, sed viverra nisl condimentumut.');
INSERT INTO randomwords VALUES('Donec eget justis enim. Atirei o pau no gatis. Viva Forevis aptent taciti sociosquad litora');
INSERT INTO randomwords VALUES('torquent per conubia nostra, per inceptos himenaeos. Copo furadis é disculpa de babadis,arcu quam euismod');
INSERT INTO randomwords VALUES('magna, bibendum egestas augue arcu ut est. Delegadis gente finis. In sitamet mattis porris, paradis.');
INSERT INTO randomwords VALUES('Paisis, filhis, espiritis santis. Mé faiz elementum girarzis. Pellentesque viverra accumsanipsum elementum gravidis.');
INSERT INTO randomwords VALUES('Forevis aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Copo furadisé');
INSERT INTO randomwords VALUES('disculpa de babadis, arcu quam euismod magna, bibendum egestas augue arcu ut est. Etiamultricies tincidunt');
INSERT INTO randomwords VALUES('ligula, sed accumsan sapien mollis et. Delegadis gente finis. In sit amet mattisporris, paradis. Paisis,');
INSERT INTO randomwords VALUES('filhis, espiritis santis. Mé faiz elementum girarzis. Pellentesque viverra accumsan ipsum elementumgravida. Quisque vitae metus');
INSERT INTO randomwords VALUES('id massa tincidunt iaculis sed sed purus. Vestibulum viverra lobortis faucibus.Vestibulum et turpis.');
INSERT INTO randomwords VALUES('Vitis e adipiscing enim. Nam varius eleifend orci, sed viverra nisl condimentum ut. Donec egetjusto');
INSERT INTO randomwords VALUES('enim. Atirei o pau no gatis. Quisque dignissim felis quis sapien ullamcorper varius temporsem varius.');
INSERT INTO randomwords VALUES('Vivamus lobortis posuere facilisis. Sed auctor eros ac sapien sagittis accumsan. Integer semperaccumsan arcu, at');
INSERT INTO randomwords VALUES('aliquam nisl sollicitudin non. Nullam pellentesque metus nec libero laoreet vitae vestibulumante ultricies. Phasellus non');
INSERT INTO randomwords VALUES('mollis purus. Integer vel lacus dolor. Proin eget mi nec maurisconvallis ullamcorper vel ac nulla.');
INSERT INTO randomwords VALUES('Nulla et semper metus.');

insert into tb_post (
  seq_post_pai,
  seq_usuario,
  cod_post,
  des_post,
  dat_post,
  seq_imagem
)
SELECT
  (select seq_post from tb_post where gs=gs order by random() limit 1),
  (select seq_usuario from tb_usuario where gs=gs order by random() limit 1),
  to_char(cast(now() - '1 year'::interval * random()  as TIMESTAMPTZ), 'YYMMDDHH24MIMSUS'),
  (select replace(replace(palavra, '.', ''),',','') from randomwords where gs=gs ORDER BY random() limit 1),
  cast(now() - '1 year'::interval * random()  as TIMESTAMPTZ),
  (select seq_imagem from tb_imagem where gs=gs order by random() limit 1)
from generate_series(1,5000) as gs;

insert into tb_post (
  seq_post_pai,
  seq_usuario,
  cod_post,
  des_post,
  dat_post,
  seq_imagem
)
SELECT
  (select seq_post from tb_post where gs=gs order by random() limit 1),
  (select seq_usuario from tb_usuario where gs=gs order by random() limit 1),
  to_char(cast(now() - '1 year'::interval * random()  as TIMESTAMPTZ), 'YYMMDDHH24MIMSUS'),
  (select replace(replace(palavra, '.', ''),',','') from randomwords where gs=gs ORDER BY random() limit 1),
  cast(now() - '1 year'::interval * random()  as TIMESTAMPTZ),
  (select seq_imagem from tb_imagem where gs=gs order by random() limit 1)
from generate_series(1,5000) as gs;

drop TABLE randomwords;