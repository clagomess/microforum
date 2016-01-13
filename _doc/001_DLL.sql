DROP SCHEMA IF EXISTS public CASCADE;
CREATE SCHEMA IF NOT EXISTS public;

create sequence seq_imagem;
create sequence seq_usuario;
create sequence seq_post;
create sequence seq_notificacao;
create sequence seq_like;
create sequence seq_seguidor;
create sequence seq_pais;

-- -----------------------------------------------------
-- Table tb_imagem
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS tb_imagem (
  seq_imagem BIGINT NOT NULL DEFAULT NEXTVAL('seq_imagem'),
  des_hash VARCHAR(45) NOT NULL,
  nom_imagem VARCHAR(45) NOT NULL,
  des_diretorio VARCHAR(20) NOT NULL,
  dat_cadastro TIMESTAMPTZ NOT NULL,
  CONSTRAINT pk_imagem PRIMARY KEY (seq_imagem),
  CONSTRAINT pk_imagem_unique UNIQUE (des_hash)
);

CREATE INDEX idx_imagem_des_hash ON tb_imagem (des_hash ASC);

-- -----------------------------------------------------
-- Table tb_pais
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS tb_pais (
  seq_pais BIGINT NOT NULL DEFAULT NEXTVAL('seq_pais'),
  nom_pais VARCHAR(45) NOT NULL,
  des_sigla VARCHAR(3) NOT NULL,
  CONSTRAINT pk_pais PRIMARY KEY (seq_pais)
);

INSERT INTO tb_pais (nom_pais, des_sigla) VALUES ('Brasil', 'BRL');
INSERT INTO tb_pais (nom_pais, des_sigla) VALUES ('World', 'WRL');

-- -----------------------------------------------------
-- Table tb_usuario
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS tb_usuario (
  seq_usuario BIGINT NOT NULL DEFAULT NEXTVAL('seq_usuario'),
  seq_imagem BIGINT NULL,
  seq_pais BIGINT NOT NULL,
  cod_usuario VARCHAR(20) NOT NULL,
  nom_usuario VARCHAR(45) NOT NULL,
  des_email VARCHAR(45) NOT NULL,
  des_senha VARCHAR(45) NOT NULL,
  dat_cadastro TIMESTAMPTZ NOT NULL,
  dat_ultimo_acesso TIMESTAMPTZ NOT NULL,
  num_seguidor INT NOT NULL DEFAULT 0,
  num_seguindo INT NOT NULL DEFAULT 0,
  sit_ativo NUMERIC(1) NOT NULL DEFAULT 1,
  sit_plus NUMERIC(1) NOT NULL DEFAULT 0,
  sit_email NUMERIC(1) NOT NULL DEFAULT 0,
  CONSTRAINT pk_usuario PRIMARY KEY (seq_usuario),
  CONSTRAINT pk_usuario_des_email_unique UNIQUE (des_email),
  CONSTRAINT pk_usuario_cod_usuario_unique UNIQUE (cod_usuario),
  CONSTRAINT fk_usuario_imagem
    FOREIGN KEY (seq_imagem)
    REFERENCES tb_imagem (seq_imagem)
    ON DELETE restrict ON UPDATE restrict,
  CONSTRAINT fk_usuario_pais
    FOREIGN KEY (seq_pais)
    REFERENCES tb_pais (seq_pais)
    ON DELETE restrict ON UPDATE restrict,
  CHECK(sit_ativo IN(0,1)),
  CHECK(sit_plus IN(0,1)),
  CHECK(sit_email IN(0,1))
);

CREATE INDEX idx_usuario_seq_imagem ON tb_usuario (seq_imagem DESC);
CREATE INDEX idx_usuario_cod_usuario ON tb_usuario (cod_usuario ASC);
CREATE INDEX idx_usuario_des_email ON tb_usuario (des_email ASC);
CREATE INDEX idx_usuario_des_senha ON tb_usuario (des_senha ASC);
CREATE INDEX idx_usuario_sit_ativo ON tb_usuario (sit_ativo ASC);


-- -----------------------------------------------------
-- Table tb_post
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS tb_post (
  seq_post BIGINT NOT NULL DEFAULT NEXTVAL('seq_post'),
  seq_post_pai BIGINT NULL,
  seq_usuario BIGINT NOT NULL,
  seq_imagem BIGINT NULL,
  cod_post VARCHAR(45) NULL,
  des_post TEXT NOT NULL,
  dat_post TIMESTAMPTZ NOT NULL,
  num_like INT NOT NULL DEFAULT 0,
  num_post_filho INT NOT NULL DEFAULT 0,
  CONSTRAINT pk_post primary key (seq_post),
  CONSTRAINT pk_post_unique UNIQUE (cod_post),
  CONSTRAINT fk_post_usuario
    FOREIGN KEY (seq_usuario)
    REFERENCES tb_usuario (seq_usuario)
    ON DELETE restrict ON UPDATE restrict,
  CONSTRAINT fk_post_post_pai
    FOREIGN KEY (seq_post_pai)
    REFERENCES tb_post (seq_post)
    ON DELETE restrict ON UPDATE restrict,
  CONSTRAINT fk_post_imagem
    FOREIGN KEY (seq_imagem)
    REFERENCES tb_imagem (seq_imagem)
    ON DELETE restrict ON UPDATE restrict
);

CREATE INDEX idx_post_seq_post_pai ON tb_post (seq_post_pai DESC);
CREATE INDEX idx_post_seq_usuario ON tb_post (seq_usuario DESC);
CREATE INDEX idx_post_cod_post ON tb_post (cod_post ASC);


-- -----------------------------------------------------
-- Table tb_like
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS tb_like (
  seq_like BIGINT NOT NULL DEFAULT NEXTVAL('seq_like'),
  seq_post BIGINT NOT NULL,
  seq_usuario BIGINT NOT NULL,
  CONSTRAINT pk_like PRIMARY KEY (seq_like),
  CONSTRAINT pk_like_unique UNIQUE (seq_post, seq_usuario),
  CONSTRAINT fk_like_post
    FOREIGN KEY (seq_post)
    REFERENCES tb_post (seq_post)
    ON DELETE restrict ON UPDATE restrict,
  CONSTRAINT fk_like_usuario
    FOREIGN KEY (seq_usuario)
    REFERENCES tb_usuario (seq_usuario)
    ON DELETE restrict ON UPDATE restrict
);


-- -----------------------------------------------------
-- Table tb_notificacao
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS tb_notificacao (
  seq_notificacao BIGINT NOT NULL DEFAULT NEXTVAL('seq_notificacao'),
  seq_usuario BIGINT NOT NULL,
  dat_notificacao TIMESTAMPTZ NULL,
  sit_email NUMERIC(1) NOT NULL DEFAULT 0,
  CONSTRAINT pk_notificacao PRIMARY KEY (seq_notificacao),
  CONSTRAINT fk_notificacao_usuario
    FOREIGN KEY (seq_usuario)
    REFERENCES tb_usuario (seq_usuario)
    ON DELETE restrict ON UPDATE restrict,
  CHECK(sit_email IN(0,1))
);

CREATE INDEX idx_notificacao_seq_usuario ON tb_notificacao (seq_usuario DESC);
CREATE INDEX idx_notificacao_sit_email ON tb_notificacao (sit_email ASC);


-- -----------------------------------------------------
-- Table tb_seguidor
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS tb_seguidor (
  seq_seguidor BIGINT NOT NULL DEFAULT NEXTVAL('seq_seguidor'),
  seq_usuario_seguidor BIGINT NOT NULL,
  seq_usuario_seguido BIGINT NOT NULL,
  dat_seguidor TIMESTAMPTZ NULL,
  CONSTRAINT pk_seguidor PRIMARY KEY (seq_seguidor),
  -- CONSTRAINT pk_seguidor_unique UNIQUE (seq_usuario_seguidor, seq_usuario_seguido),
  CONSTRAINT fk_sequidor_usuario_seguidor
    FOREIGN KEY (seq_usuario_seguidor)
    REFERENCES tb_usuario (seq_usuario)
    ON DELETE restrict ON UPDATE restrict,
  CONSTRAINT fk_sequidor_usuario_seguido
    FOREIGN KEY (seq_usuario_seguido)
    REFERENCES tb_usuario (seq_usuario)
    ON DELETE restrict ON UPDATE restrict
);
