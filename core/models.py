from django.db import models


class Pais(models.Model):
    seq_pais = models.AutoField(primary_key=True)
    nom_pais = models.CharField(max_length=45, null=False)
    des_sigla = models.CharField(max_length=3, null=False)

    class Meta:
        db_table = 'tb_pais'


class Imagem(models.Model):
    seq_imagem = models.AutoField(primary_key=True)
    des_hash = models.CharField(max_length=45, null=False)
    nom_imagem = models.CharField(max_length=45, null=False)
    des_diretorio = models.CharField(max_length=45, null=False)
    dat_cadastro = models.DateTimeField(null=False)

    class Meta:
        db_table = 'tb_imagem'


class Usuario(models.Model):
    seq_usuario = models.AutoField(primary_key=True)
    seq_imagem = models.ForeignKey(Imagem, null=True, db_column="seq_imagem")
    seq_pais = models.ForeignKey(Pais, null=False, db_column="seq_pais")
    cod_usuario = models.CharField(max_length=20, null=False)
    nom_usuario = models.CharField(max_length=45, null=False)
    des_email = models.CharField(max_length=45, null=False)
    des_senha = models.CharField(max_length=45, null=False)
    dat_cadastro = models.DateTimeField(null=False)
    dat_ultimo_acesso = models.DateTimeField(null=False)
    num_seguidor = models.IntegerField(null=False, default=0)
    num_seguindo = models.IntegerField(null=False, default=0)
    sit_ativo = models.IntegerField(max_length=1, null=False, default=1)
    sit_plus = models.IntegerField(max_length=1, null=False, default=0)
    sit_email = models.IntegerField(max_length=1, null=False, default=0)

    class Meta:
        db_table = 'tb_usuario'


class Post(models.Model):
    seq_post = models.AutoField(primary_key=True)
    seq_post_pai = models.ForeignKey('self', null=True, db_column="seq_post_pai")
    seq_usuario = models.ForeignKey(Usuario, db_column="seq_usuario")
    seq_imagem = models.ForeignKey(Imagem, db_column="seq_imagem")
    cod_post = models.CharField(max_length=45, null=False)
    des_post = models.TextField()
    dat_post = models.DateTimeField(null=False)
    num_like = models.IntegerField(null=False, default=0)
    num_post_filho = models.IntegerField(null=False, default=0)

    class Meta:
        db_table = 'tb_post'

    def __unicode__(self):
        return self.des_post


class Like(models.Model):
    seq_like = models.AutoField(primary_key=True)
    seq_post = models.ForeignKey(Post, db_column="seq_post")
    seq_usuario = models.ForeignKey(Usuario, db_column="seq_usuario")

    class Meta:
        db_table = 'tb_like'

    def __unicode__(self):
        return self.seq_usuario.nom_usuario


class Notificacao(models.Model):
    seq_notificacao = models.AutoField(primary_key=True)
    seq_usuario = models.ForeignKey(Usuario, db_column="seq_usuario")
    dat_notificacao = models.DateTimeField(null=False)
    sit_email = models.IntegerField(max_length=1, null=False, default=0)

    class Meta:
        db_table = 'tb_notificacao'

    def __unicode__(self):
        return self.seq_usuario.nom_usuario


class Seguidor(models.Model):
    seq_seguidor = models.AutoField(primary_key=True)
    seq_usuario_seguidor = models.ForeignKey(Usuario, db_column="seq_usuario_seguidor")
    seq_usuario_seguido = models.ForeignKey(Usuario, db_column="seq_usuario_seguido")
    dat_seguidor = models.DateTimeField(null=False)

    class Meta:
        db_table = 'tb_seguidor'

    def __unicode__(self):
        return self.seq_usuario_seguidor.nom_usuario