# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Aliases(models.Model):
    alias = models.CharField(max_length=255, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    domain = models.CharField(max_length=255, blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    active = models.IntegerField(blank=True, null=True)
    cd_int = models.IntegerField(blank=True, null=True)
    codaliases = models.AutoField(primary_key=True)
    b = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aliases'


class Ap2BoletoBancaro(models.Model):
    bol_id = models.AutoField(primary_key=True)
    local_pagamento1 = models.CharField(max_length=58, blank=True, null=True)
    local_pagamento2 = models.CharField(max_length=58, blank=True, null=True)
    instrucoes = models.CharField(max_length=120, blank=True, null=True)
    agencia_numero = models.CharField(max_length=18, blank=True, null=True)
    agencia_dv = models.CharField(max_length=4, blank=True, null=True)
    beneficiario_nome = models.CharField(max_length=40, blank=True, null=True)
    conta_corrente_numero = models.CharField(max_length=24, blank=True, null=True)
    data_processamento = models.DateField(blank=True, null=True)
    data_vencimento = models.DateField(blank=True, null=True)
    documento_especie = models.CharField(max_length=2, blank=True, null=True)
    documento_numero = models.CharField(max_length=20, blank=True, null=True)
    documento_data = models.DateField(blank=True, null=True)
    valor_boleto = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    nosso_numero = models.CharField(max_length=20, blank=True, null=True)
    pagador_bairro = models.CharField(max_length=57, blank=True, null=True)
    pagador_logradouro = models.CharField(max_length=60, blank=True, null=True)
    pagador_cep = models.CharField(max_length=20, blank=True, null=True)
    pagador_municipio = models.CharField(max_length=60, blank=True, null=True)
    pagador_documento = models.CharField(max_length=80, blank=True, null=True)
    pagador_nome = models.CharField(max_length=60, blank=True, null=True)
    pagador_uf = models.CharField(max_length=4, blank=True, null=True)
    beneficiario_email = models.CharField(max_length=30, blank=True, null=True)
    nosso_numero_dv = models.CharField(max_length=12, blank=True, null=True)
    beneficiario_telefone = models.CharField(max_length=21, blank=True, null=True)
    beneficiario_logomarca = models.BinaryField(blank=True, null=True)
    conta_corrente_dv = models.CharField(max_length=7, blank=True, null=True)
    beneficiario_logradouro = models.CharField(max_length=72, blank=True, null=True)
    beneficiario_bairro = models.CharField(max_length=30, blank=True, null=True)
    beneficiario_municipio = models.CharField(max_length=37, blank=True, null=True)
    beneficiario_cep = models.CharField(max_length=14, blank=True, null=True)
    beneficiario_uf = models.CharField(max_length=5, blank=True, null=True)
    beneficiario_documento = models.CharField(max_length=20, blank=True, null=True)
    nosso_numero_dv_itau = models.CharField(max_length=3, blank=True, null=True)
    nosso_numero_itau = models.CharField(max_length=7, blank=True, null=True)
    conta_corrente_dv_itau = models.CharField(max_length=3, blank=True, null=True)
    conta_corrente_numero_itau = models.CharField(max_length=5, blank=True, null=True)
    agencia_numero_itau = models.CharField(max_length=18, blank=True, null=True)
    agencia_dv_itau = models.CharField(max_length=3, blank=True, null=True)
    beneficiario_cod_cliente = models.CharField(max_length=20, blank=True, null=True)
    banco = models.CharField(max_length=3, blank=True, null=True)
    carteira = models.CharField(max_length=5, blank=True, null=True)
    carteira_modalidade = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ap2_boleto_bancaro'


class Cabo(models.Model):
    cabo_id = models.CharField(primary_key=True, max_length=36)
    tipo_cabo_id = models.IntegerField(blank=True, null=True)
    elemento_id_origem = models.CharField(max_length=36, blank=True, null=True)
    cab_identificacao = models.CharField(max_length=20, blank=True, null=True)
    cab_fabricante = models.CharField(max_length=50, blank=True, null=True)
    cab_especificacao = models.CharField(max_length=40, blank=True, null=True)
    cab_quant_fibras = models.IntegerField(blank=True, null=True)
    cab_comprimento = models.IntegerField(blank=True, null=True)
    cab_cadastrado = models.IntegerField(blank=True, null=True)
    cab_caixas_emenda = models.IntegerField(blank=True, null=True)
    cab_reservas_tecnicas = models.IntegerField(blank=True, null=True)
    cab_dutos = models.IntegerField(blank=True, null=True)
    cab_postes = models.IntegerField(blank=True, null=True)
    cab_fontes = models.IntegerField(blank=True, null=True)
    cab_observacao = models.CharField(max_length=200, blank=True, null=True)
    cab_data_instalacao = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cabo'


class FrFormulario(models.Model):
    frm_codigo = models.IntegerField(primary_key=True)
    img_incluir = models.IntegerField(blank=True, null=True)
    img_alterar = models.IntegerField(blank=True, null=True)
    img_excluir = models.IntegerField(blank=True, null=True)
    img_gravar = models.IntegerField(blank=True, null=True)
    img_cancelar = models.IntegerField(blank=True, null=True)
    img_atualizar = models.IntegerField(blank=True, null=True)
    img_utilitario = models.IntegerField(blank=True, null=True)
    img_sair = models.IntegerField(blank=True, null=True)
    img_imprimir = models.IntegerField(blank=True, null=True)
    img_ajuda = models.IntegerField(blank=True, null=True)
    img_proximo = models.IntegerField(blank=True, null=True)
    img_ultimo = models.IntegerField(blank=True, null=True)
    img_primeiro = models.IntegerField(blank=True, null=True)
    img_anterior = models.IntegerField(blank=True, null=True)
    frm_descricao = models.CharField(max_length=100)
    frm_tipo = models.CharField(max_length=1, blank=True, null=True)
    frm_posicaox = models.IntegerField(blank=True, null=True)
    frm_posicaoy = models.IntegerField(blank=True, null=True)
    frm_tamanho = models.IntegerField(blank=True, null=True)
    frm_altura = models.IntegerField(blank=True, null=True)
    frm_tipo_criacao = models.CharField(max_length=1)
    frm_guid = models.CharField(max_length=38, blank=True, null=True)
    rel_codigo = models.ForeignKey('FrRelatorio', models.DO_NOTHING, db_column='rel_codigo', blank=True, null=True)
    usr_codigo = models.ForeignKey('FrUsuario', models.DO_NOTHING, db_column='usr_codigo', blank=True, null=True)
    frm_log = models.CharField(max_length=1)
    img_gravar_mais = models.IntegerField(blank=True, null=True)
    img_valores_padrao = models.IntegerField(blank=True, null=True)
    img_log = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fr_formulario'


class FrFormularioMigration(models.Model):
    frm_codigo = models.IntegerField()
    frm_descricao = models.CharField(max_length=100)
    frm_guid = models.CharField(max_length=38, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fr_formulario_migration'


class FrGrupo(models.Model):
    grp_codigo = models.IntegerField(primary_key=True)
    sis_codigo = models.CharField(max_length=3)
    grp_nome = models.CharField(max_length=40)
    grp_filtro_dicionario = models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fr_grupo'
        unique_together = (('grp_nome', 'sis_codigo'), ('grp_codigo', 'sis_codigo'),)


class FrImagem(models.Model):
    img_codigo = models.IntegerField(primary_key=True)
    img_guid = models.CharField(unique=True, max_length=38, blank=True, null=True)
    img_imagem = models.BinaryField()

    class Meta:
        managed = False
        db_table = 'fr_imagem'


class FrLogEvent(models.Model):
    log_data = models.DateTimeField(blank=True, null=True)
    log_hora = models.CharField(max_length=8, blank=True, null=True)
    log_codform = models.IntegerField(blank=True, null=True)
    log_descform = models.CharField(max_length=100, blank=True, null=True)
    log_operacao = models.CharField(max_length=1, blank=True, null=True)
    log_usuario = models.CharField(max_length=30, blank=True, null=True)
    log_sistema = models.CharField(max_length=3, blank=True, null=True)
    log_chave = models.CharField(max_length=200, blank=True, null=True)
    log_chavecont = models.CharField(max_length=128, blank=True, null=True)
    log_conteudo = models.TextField(blank=True, null=True)
    log_id = models.IntegerField()
    log_ip = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fr_log_event'


class FrPermissao(models.Model):
    grp_codigo = models.ForeignKey(FrGrupo, models.DO_NOTHING, db_column='grp_codigo')
    sis_codigo = models.CharField(max_length=3)
    rel_codigo = models.ForeignKey('FrRelatorio', models.DO_NOTHING, db_column='rel_codigo', blank=True, null=True)
    frm_codigo = models.ForeignKey(FrFormulario, models.DO_NOTHING, db_column='frm_codigo', blank=True, null=True)
    com_codigo = models.IntegerField(blank=True, null=True)
    mnu_codigo = models.IntegerField(blank=True, null=True)
    per_adicionar = models.CharField(max_length=1)
    per_excluir = models.CharField(max_length=1)
    per_editar = models.CharField(max_length=1)
    per_visualizar = models.CharField(max_length=1)
    per_habilitado = models.CharField(max_length=1)
    per_codigo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'fr_permissao'
        unique_together = (('grp_codigo', 'frm_codigo', 'com_codigo'), ('grp_codigo', 'mnu_codigo'), ('grp_codigo', 'rel_codigo'),)


class FrRegras(models.Model):
    reg_cod = models.IntegerField(primary_key=True)
    reg_nome = models.CharField(unique=True, max_length=255, blank=True, null=True)
    reg_descricao = models.CharField(max_length=2000, blank=True, null=True)
    reg_params = models.CharField(max_length=500, blank=True, null=True)
    reg_variaveis = models.CharField(max_length=500, blank=True, null=True)
    reg_params_out = models.CharField(max_length=500, blank=True, null=True)
    reg_interface = models.TextField(blank=True, null=True)
    reg_script = models.TextField(blank=True, null=True)
    reg_data = models.DateTimeField(blank=True, null=True)
    reg_hora = models.DateTimeField(blank=True, null=True)
    reg_destino = models.IntegerField(blank=True, null=True)
    reg_hash = models.CharField(max_length=50, blank=True, null=True)
    cat_cod = models.ForeignKey('FrRegrasCategorias', models.DO_NOTHING, db_column='cat_cod', blank=True, null=True)
    reg_compilada = models.CharField(max_length=1, blank=True, null=True)
    usr_codigo = models.ForeignKey('FrUsuario', models.DO_NOTHING, db_column='usr_codigo', blank=True, null=True)
    mk_dh_atualizacao = models.DateTimeField()
    mk3 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fr_regras'


class FrRegrasCategorias(models.Model):
    cat_cod = models.IntegerField(primary_key=True)
    cat_nome = models.CharField(max_length=40, blank=True, null=True)
    cat_super = models.ForeignKey('self', models.DO_NOTHING, db_column='cat_super', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fr_regras_categorias'


class FrRegrasMigration(models.Model):
    reg_cod = models.IntegerField()
    reg_nome = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fr_regras_migration'


class FrRelatorio(models.Model):
    rel_codigo = models.IntegerField(primary_key=True)
    sis_codigo = models.CharField(max_length=3)
    rel_nome = models.CharField(max_length=196)
    rel_conteudo = models.TextField(blank=True, null=True)
    rel_modificado = models.DateTimeField(blank=True, null=True)
    rel_tamanho = models.IntegerField(blank=True, null=True)
    usr_codigo = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fr_relatorio'
        unique_together = (('rel_codigo', 'sis_codigo'), ('sis_codigo', 'rel_nome'),)


class FrSistema(models.Model):
    sis_codigo = models.CharField(primary_key=True, max_length=3)
    sis_descricao = models.CharField(max_length=30)
    img_codigo = models.IntegerField(blank=True, null=True)
    img_codigo_icone = models.IntegerField(blank=True, null=True)
    sis_sqldatalimite = models.CharField(max_length=2000, blank=True, null=True)
    sis_sqldadosentidade = models.CharField(max_length=2000, blank=True, null=True)
    sis_sqlinformacoes = models.CharField(max_length=2000, blank=True, null=True)
    sis_check = models.CharField(max_length=30, blank=True, null=True)
    sis_grupoexterno = models.IntegerField(blank=True, null=True)
    sis_resumo = models.CharField(max_length=1000, blank=True, null=True)
    sis_acessoexterno = models.BooleanField(blank=True, null=True)
    sis_informacao = models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fr_sistema'


class FrUsuario(models.Model):
    usr_codigo = models.IntegerField(primary_key=True)
    usr_login = models.CharField(unique=True, max_length=20)
    usr_senha = models.CharField(max_length=64, blank=True, null=True)
    usr_administrador = models.CharField(max_length=1)
    usr_tipo_expiracao = models.CharField(max_length=1)
    usr_dias_expiracao = models.IntegerField(blank=True, null=True)
    usr_imagem_digital = models.BinaryField(blank=True, null=True)
    usr_foto = models.BinaryField(blank=True, null=True)
    usr_nome = models.CharField(max_length=60)
    usr_email = models.CharField(max_length=120, blank=True, null=True)
    usr_digital = models.BigIntegerField(blank=True, null=True)
    usr_inicio_expiracao = models.DateTimeField(blank=True, null=True)
    fone_celular = models.CharField(max_length=20, blank=True, null=True)
    id_whatsapp = models.CharField(max_length=30, blank=True, null=True)
    id_telegram = models.CharField(max_length=30, blank=True, null=True)
    setor_associado = models.CharField(max_length=20, blank=True, null=True)
    cd_perfil_acesso = models.IntegerField(blank=True, null=True)
    str_hosts_acesso = models.CharField(max_length=200, blank=True, null=True)
    dt_atu_cadastro = models.DateField(blank=True, null=True)
    token_acesso = models.CharField(max_length=50, blank=True, null=True)
    token_gcm = models.CharField(max_length=200, blank=True, null=True)
    usa_mob_os = models.CharField(max_length=1, blank=True, null=True)
    token_gcm_manager = models.CharField(max_length=200, blank=True, null=True)
    token_gcm_maps = models.CharField(max_length=200, blank=True, null=True)
    ocultar_painel_os = models.CharField(max_length=1, blank=True, null=True)
    token_gcm_crm = models.CharField(max_length=200, blank=True, null=True)
    permite_logar_todos = models.CharField(max_length=1, blank=True, null=True)
    chat_usuario = models.CharField(max_length=200, blank=True, null=True)
    chat_senha = models.CharField(max_length=80, blank=True, null=True)
    usr_sac = models.CharField(max_length=1, blank=True, null=True)
    cd_revenda = models.ForeignKey('MkRevendas', models.DO_NOTHING, db_column='cd_revenda', blank=True, null=True)
    mkbot_xmpp_senha = models.CharField(max_length=80, blank=True, null=True)
    mkbot_xmpp_usuario = models.CharField(max_length=120, blank=True, null=True)
    mkbot_chave_liberacao = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fr_usuario'


class MkAtribRadiusCheckReply(models.Model):
    codatribrdcheckreply = models.AutoField(primary_key=True)
    nome_perfil = models.CharField(max_length=50, blank=True, null=True)
    id_ope_cadastro = models.IntegerField(blank=True, null=True)
    dh = models.DateTimeField(blank=True, null=True)
    padrao = models.CharField(max_length=1, blank=True, null=True)
    tipo_insert = models.IntegerField(blank=True, null=True)
    obriga_group_reply = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mk_atrib_radius_check_reply'


class MkAtribRadiusGroupReply(models.Model):
    codatribrdgroupreply = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=50, blank=True, null=True)
    id_ope_cadastro = models.IntegerField(blank=True, null=True)
    dh = models.DateTimeField(blank=True, null=True)
    padrao = models.CharField(max_length=1, blank=True, null=True)
    tipo_insert = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mk_atrib_radius_group_reply'


class MkBairros(models.Model):
    codbairro = models.AutoField(primary_key=True)
    bairro = models.CharField(max_length=60)
    codcidade = models.ForeignKey('MkCidades', models.DO_NOTHING, db_column='codcidade')
    cd_microarea = models.IntegerField(blank=True, null=True)
    latitude = models.CharField(max_length=50, blank=True, null=True)
    longitude = models.CharField(max_length=50, blank=True, null=True)
    nao_encontrato = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mk_bairros'


class MkBoletosGerados(models.Model):
    codgeracao = models.AutoField(primary_key=True)
    valor = models.FloatField(blank=True, null=True)
    vencimento = models.CharField(max_length=30, blank=True, null=True)
    nosso_numero = models.CharField(max_length=20, blank=True, null=True)
    nome_sacado = models.CharField(max_length=100, blank=True, null=True)
    endereco = models.CharField(max_length=200, blank=True, null=True)
    cep = models.CharField(max_length=8, blank=True, null=True)
    cidade = models.CharField(max_length=50, blank=True, null=True)
    estado = models.CharField(max_length=3, blank=True, null=True)
    linha1 = models.CharField(max_length=200, blank=True, null=True)
    linha2 = models.CharField(max_length=200, blank=True, null=True)
    linha3 = models.CharField(max_length=200, blank=True, null=True)
    linha4 = models.CharField(max_length=200, blank=True, null=True)
    linha5 = models.CharField(max_length=200, blank=True, null=True)
    linha6 = models.CharField(max_length=200, blank=True, null=True)
    linha7 = models.CharField(max_length=200, blank=True, null=True)
    linha8 = models.CharField(max_length=200, blank=True, null=True)
    nome_cedente = models.CharField(max_length=100, blank=True, null=True)
    local_pgto = models.CharField(max_length=200, blank=True, null=True)
    tx_aux_1 = models.CharField(max_length=200, blank=True, null=True)
    tx_aux_2 = models.CharField(max_length=200, blank=True, null=True)
    tx_aux_3 = models.CharField(max_length=200, blank=True, null=True)
    tx_aux_4 = models.CharField(max_length=200, blank=True, null=True)
    tx_aux_5 = models.CharField(max_length=200, blank=True, null=True)
    tx_aux_6 = models.CharField(max_length=200, blank=True, null=True)
    tx_aux_7 = models.CharField(max_length=200, blank=True, null=True)
    banco = models.CharField(max_length=20, blank=True, null=True)
    agencia = models.CharField(max_length=20, blank=True, null=True)
    aceite = models.CharField(max_length=10, blank=True, null=True)
    cedente_barra = models.CharField(max_length=50, blank=True, null=True)
    cod_cliente = models.CharField(max_length=20, blank=True, null=True)
    cnpj_cedente = models.CharField(max_length=20, blank=True, null=True)
    cpf_cnpj_sacado = models.CharField(max_length=20, blank=True, null=True)
    data_processamento = models.CharField(max_length=30, blank=True, null=True)
    desconto = models.CharField(max_length=10, blank=True, null=True)
    modalidade = models.CharField(max_length=50, blank=True, null=True)
    multa = models.CharField(max_length=10, blank=True, null=True)
    num_convenio = models.CharField(max_length=30, blank=True, null=True)
    num_doc = models.CharField(max_length=30, blank=True, null=True)
    parcela = models.CharField(max_length=10, blank=True, null=True)
    carteira = models.CharField(max_length=10, blank=True, null=True)
    cod_cedente = models.CharField(max_length=15, blank=True, null=True)
    outros_acrescimos = models.CharField(max_length=10, blank=True, null=True)
    valor_cobrado = models.CharField(max_length=100, blank=True, null=True)
    codconta = models.IntegerField(blank=True, null=True)
    profile = models.ForeignKey('MkProfilePgto', models.DO_NOTHING, db_column='profile', blank=True, null=True)
    substituido = models.CharField(max_length=1, blank=True, null=True)
    data_remocao = models.DateField(blank=True, null=True)
    hora_remocao = models.CharField(max_length=10, blank=True, null=True)
    user_remocao = models.CharField(max_length=50, blank=True, null=True)
    codcontrato = models.IntegerField(blank=True, null=True)
    tx_mens_titulo = models.CharField(max_length=200, blank=True, null=True)
    tx_mens_linha1 = models.CharField(max_length=200, blank=True, null=True)
    tx_mens_linha2 = models.CharField(max_length=200, blank=True, null=True)
    tx_mens_linha3 = models.CharField(max_length=200, blank=True, null=True)
    tx_mens_linha4 = models.CharField(max_length=200, blank=True, null=True)
    tx_mens_linha5 = models.CharField(max_length=200, blank=True, null=True)
    tx_mens_linha6 = models.CharField(max_length=200, blank=True, null=True)
    tx_mens_linha7 = models.CharField(max_length=200, blank=True, null=True)
    smtp = models.CharField(max_length=100, blank=True, null=True)
    username = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=50, blank=True, null=True)
    email_origem = models.CharField(max_length=100, blank=True, null=True)
    email_destino = models.CharField(max_length=100, blank=True, null=True)
    conta_email = models.IntegerField(blank=True, null=True)
    vencimento_dt_normal = models.DateField(blank=True, null=True)
    guid = models.CharField(max_length=50, blank=True, null=True)
    arquivo_remessa = models.CharField(max_length=1, blank=True, null=True)
    gerado_transmissao = models.CharField(max_length=1, blank=True, null=True)
    dt_ger_transmissao = models.DateField(blank=True, null=True)
    tmp_trans = models.CharField(max_length=1, blank=True, null=True)
    nome_arquivo = models.CharField(max_length=50, blank=True, null=True)
    seq_arq_remessa = models.IntegerField(blank=True, null=True)
    tmp_marca_consulta = models.CharField(max_length=1, blank=True, null=True)
    guid_envio_email = models.CharField(max_length=50, blank=True, null=True)
    ret_nosso_num_banco = models.CharField(max_length=20, blank=True, null=True)
    profile_antiga = models.IntegerField(blank=True, null=True)
    entrada_confirmada = models.CharField(max_length=1, blank=True, null=True)
    nomenclatura_integracao = models.CharField(max_length=3, blank=True, null=True)
    codvinculado = models.IntegerField(blank=True, null=True)
    nosso_numero2 = models.CharField(max_length=20, blank=True, null=True)
    guid_exibicao = models.CharField(max_length=50, blank=True, null=True)
    suspenso = models.CharField(max_length=1, blank=True, null=True)
    cd_fatura = models.OneToOneField('MkFaturas', models.DO_NOTHING, db_column='cd_fatura', blank=True, null=True)
    profile_redefinida = models.CharField(max_length=1, blank=True, null=True)
    profile_original = models.IntegerField(blank=True, null=True)
    codigo_barras = models.CharField(unique=True, max_length=100, blank=True, null=True)
    linha_digitavel = models.CharField(unique=True, max_length=100, blank=True, null=True)
    nosso_numero_formatado = models.CharField(max_length=50, blank=True, null=True)
    hash_integridade = models.CharField(max_length=50, blank=True, null=True)
    instrucoes = models.TextField(blank=True, null=True)
    id_unificacao = models.IntegerField(blank=True, null=True)
    cd_boleto_replicado = models.IntegerField(blank=True, null=True)
    cd_empresa = models.IntegerField(blank=True, null=True)
    tmp_trans_em_pendencia = models.CharField(max_length=1, blank=True, null=True)
    guid_controle_back = models.CharField(max_length=50, blank=True, null=True)
    nome_file_back = models.CharField(max_length=50, blank=True, null=True)
    controle_de_ordenacao = models.IntegerField(blank=True, null=True)
    nosso_numero_dv = models.CharField(max_length=2, blank=True, null=True)
    guid_controle_troca_profile = models.CharField(max_length=50, blank=True, null=True)
    dh = models.DateTimeField(blank=True, null=True)
    cd_remessa_gerada = models.IntegerField(blank=True, null=True)
    parcela_i_carne = models.IntegerField(blank=True, null=True)
    parcela_f_carne = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mk_boletos_gerados'
        unique_together = (('nosso_numero_formatado', 'profile'), ('nosso_numero', 'id_unificacao'), ('nosso_numero', 'profile'),)


class MkCcDimensoes(models.Model):
    codccdimensao = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mk_cc_dimensoes'


class MkCcRateio(models.Model):
    codccrateio = models.AutoField(primary_key=True)
    dh = models.DateTimeField(blank=True, null=True)
    id_operador = models.IntegerField(blank=True, null=True)
    nome_regra = models.CharField(max_length=30, blank=True, null=True)
    ativo = models.CharField(max_length=1, blank=True, null=True)
    dt_limite = models.DateField(blank=True, null=True)
    cd_dimensao = models.ForeignKey(MkCcDimensoes, models.DO_NOTHING, db_column='cd_dimensao', blank=True, null=True)
    tipo_rateio = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mk_cc_rateio'


class MkCidades(models.Model):
    codcidade = models.AutoField(primary_key=True)
    codestado = models.ForeignKey('MkEstados', models.DO_NOTHING, db_column='codestado')
    cidade = models.CharField(max_length=50)
    ibge = models.CharField(max_length=10, blank=True, null=True)
    latitude = models.CharField(max_length=50, blank=True, null=True)
    longitude = models.CharField(max_length=50, blank=True, null=True)
    nao_encontrato = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mk_cidades'


class MkConexoes(models.Model):
    codconexao = models.AutoField(primary_key=True)
    codcliente = models.ForeignKey('MkPessoas', models.DO_NOTHING, db_column='codcliente')
    tipo_conexao = models.IntegerField()
    autenticacao = models.IntegerField()
    username = models.CharField(max_length=50, blank=True, null=True)
    password = models.CharField(max_length=30, blank=True, null=True)
    instalador = models.ForeignKey('MkPessoas', models.DO_NOTHING, db_column='instalador', blank=True, null=True)
    cadastrado = models.DateField()
    advertise_url = models.CharField(max_length=100, blank=True, null=True)
    advertise_time = models.IntegerField(blank=True, null=True)
    site_inicial = models.CharField(max_length=100, blank=True, null=True)
    codservidor = models.ForeignKey('MkServidores', models.DO_NOTHING, db_column='codservidor')
    codponto_acesso = models.IntegerField(blank=True, null=True)
    codplano_acesso = models.ForeignKey('MkPlanosAcesso', models.DO_NOTHING, db_column='codplano_acesso')
    codendereco_ip = models.OneToOneField('MkTabelaIps', models.DO_NOTHING, db_column='codendereco_ip', blank=True, null=True)
    mac_address = models.CharField(max_length=20)
    mac_address_aux = models.CharField(max_length=20, blank=True, null=True)
    mac_address_considerado = models.CharField(max_length=20)
    conexao_bloqueada = models.CharField(max_length=1, blank=True, null=True)
    path_monitor_grafico = models.CharField(max_length=150, blank=True, null=True)
    url_inadimplencia = models.CharField(max_length=150, blank=True, null=True)
    ponto_acesso = models.IntegerField(blank=True, null=True)
    motivo_bloqueio = models.IntegerField(blank=True, null=True)
    descricao = models.CharField(max_length=50, blank=True, null=True)
    expira_em = models.DateField(blank=True, null=True)
    velocidades_formatadas = models.CharField(max_length=70, blank=True, null=True)
    sucesso_int_01 = models.CharField(max_length=1, blank=True, null=True)
    sucesso_int_02 = models.CharField(max_length=1, blank=True, null=True)
    sucesso_int_03 = models.CharField(max_length=1, blank=True, null=True)
    wpa2_key = models.CharField(max_length=100, blank=True, null=True)
    senha_equipamento = models.CharField(max_length=30, blank=True, null=True)
    contrato = models.ForeignKey('MkContratos', models.DO_NOTHING, db_column='contrato', blank=True, null=True)
    range_rota = models.IntegerField(blank=True, null=True)
    cadastrar_portal = models.CharField(max_length=1, blank=True, null=True)
    em_excecao = models.CharField(max_length=1, blank=True, null=True)
    motivo_excecao = models.CharField(max_length=50, blank=True, null=True)
    prazo_excecao = models.DateField(blank=True, null=True)
    tmp_exibicao = models.CharField(max_length=1, blank=True, null=True)
    tmp_seria_bloqueado = models.DateField(blank=True, null=True)
    permite_acesso_sac = models.CharField(max_length=1, blank=True, null=True)
    license_ap = models.CharField(max_length=30, blank=True, null=True)
    license_server = models.CharField(max_length=30, blank=True, null=True)
    queue_mb_in = models.FloatField(blank=True, null=True)
    queue_mb_out = models.FloatField(blank=True, null=True)
    queue_packets_in = models.FloatField(blank=True, null=True)
    queue_packets_out = models.FloatField(blank=True, null=True)
    queue_data = models.DateField(blank=True, null=True)
    queue_hora = models.CharField(max_length=10, blank=True, null=True)
    queue_encerrada = models.CharField(max_length=1, blank=True, null=True)
    wire_desconectado = models.CharField(max_length=1, blank=True, null=True)
    wire_id = models.CharField(max_length=20, blank=True, null=True)
    wire_tx_rate = models.FloatField(blank=True, null=True)
    wire_rx_rate = models.FloatField(blank=True, null=True)
    wire_signal = models.CharField(max_length=5, blank=True, null=True)
    wire_tx_packets = models.FloatField(blank=True, null=True)
    wire_rx_packets = models.FloatField(blank=True, null=True)
    wire_download = models.FloatField(blank=True, null=True)
    wire_upload = models.FloatField(blank=True, null=True)
    data_login = models.DateField(blank=True, null=True)
    hora_login = models.CharField(max_length=10, blank=True, null=True)
    login_encerrado = models.CharField(max_length=1, blank=True, null=True)
    ip_add_server = models.CharField(max_length=20, blank=True, null=True)
    ip_add_pop = models.CharField(max_length=20, blank=True, null=True)
    active_revisado = models.CharField(max_length=1, blank=True, null=True)
    data_login_enc = models.DateField(blank=True, null=True)
    hora_login_enc = models.CharField(max_length=10, blank=True, null=True)
    queue_revisado = models.CharField(max_length=1, blank=True, null=True)
    wire_revisado = models.CharField(max_length=1, blank=True, null=True)
    queue_control = models.CharField(max_length=1, blank=True, null=True)
    rota_ip = models.IntegerField(blank=True, null=True)
    rota_ativa = models.CharField(max_length=1, blank=True, null=True)
    tipo_ip = models.IntegerField(blank=True, null=True)
    sera_bloqueado = models.CharField(max_length=1, blank=True, null=True)
    pool_associado = models.IntegerField(blank=True, null=True)
    lacre_equipamento = models.CharField(max_length=50, blank=True, null=True)
    address_list = models.IntegerField(blank=True, null=True)
    franquia_ativa = models.CharField(max_length=1, blank=True, null=True)
    cd_assinante = models.CharField(unique=True, max_length=30, blank=True, null=True)
    tipo_criptografia = models.IntegerField(blank=True, null=True)
    latitude = models.CharField(max_length=30, blank=True, null=True)
    longitude = models.CharField(max_length=30, blank=True, null=True)
    auto_desbloqueio = models.CharField(max_length=1, blank=True, null=True)
    pre_cadastro = models.IntegerField(blank=True, null=True)
    url_inadimplencia_dias = models.IntegerField(blank=True, null=True)
    guid_estatisticas = models.CharField(max_length=50, blank=True, null=True)
    condominio = models.IntegerField(blank=True, null=True)
    nasipaddress = models.CharField(max_length=20, blank=True, null=True)
    framedipaddress = models.CharField(max_length=20, blank=True, null=True)
    input_dia = models.BigIntegerField(blank=True, null=True)
    output_dia = models.BigIntegerField(blank=True, null=True)
    input_mes = models.BigIntegerField(blank=True, null=True)
    output_mes = models.BigIntegerField(blank=True, null=True)
    em_velocidade_temporaria = models.CharField(max_length=1, blank=True, null=True)
    velocidade_temporaria = models.CharField(max_length=70, blank=True, null=True)
    vel_temp_entrada = models.CharField(max_length=50, blank=True, null=True)
    vel_temp_saida = models.CharField(max_length=50, blank=True, null=True)
    ultimo_bloqueio_auto = models.DateField(blank=True, null=True)
    vencimento_dup_bloqueio = models.DateField(blank=True, null=True)
    vlr_duplicata_bloqueio = models.FloatField(blank=True, null=True)
    dia_vencimento_bloqueio = models.IntegerField(blank=True, null=True)
    limitacao_user = models.CharField(max_length=50, blank=True, null=True)
    limitacao_dt = models.DateField(blank=True, null=True)
    limitacao_hr = models.CharField(max_length=10, blank=True, null=True)
    acctsessionid = models.CharField(max_length=32, blank=True, null=True)
    franquia_excecao = models.CharField(max_length=1, blank=True, null=True)
    franquia_dt_excecao = models.DateField(blank=True, null=True)
    franquia_total_excecao = models.FloatField(blank=True, null=True)
    franquia_total_excecao_medida = models.CharField(max_length=2, blank=True, null=True)
    franquia_excecao_vitalicia = models.CharField(max_length=1, blank=True, null=True)
    em_inadimplencia = models.CharField(max_length=1, blank=True, null=True)
    equipamento_tx = models.TextField(blank=True, null=True)
    equipamento_modo = models.CharField(max_length=1, blank=True, null=True)
    equipamento_ip_lan = models.CharField(max_length=25, blank=True, null=True)
    equipamento_porta_http = models.CharField(max_length=5, blank=True, null=True)
    equipamento_porta_ssh = models.CharField(max_length=5, blank=True, null=True)
    equipamento_info_direct = models.TextField(blank=True, null=True)
    tmp_senha_md5 = models.CharField(max_length=100, blank=True, null=True)
    ignora_bloqueio = models.CharField(max_length=1, blank=True, null=True)
    porta_dsl = models.IntegerField(blank=True, null=True)
    porta_dg = models.IntegerField(blank=True, null=True)
    porta_telefone = models.IntegerField(blank=True, null=True)
    cep = models.CharField(max_length=8, blank=True, null=True)
    uf = models.IntegerField(blank=True, null=True)
    cidade = models.IntegerField(blank=True, null=True)
    bairro = models.IntegerField(blank=True, null=True)
    logradouro = models.IntegerField(blank=True, null=True)
    numero = models.IntegerField(blank=True, null=True)
    complemento = models.CharField(max_length=100, blank=True, null=True)
    problema_info_concentrador = models.CharField(max_length=1, blank=True, null=True)
    ip_atual_concentrador = models.CharField(max_length=20, blank=True, null=True)
    ultimo_desbloqueio = models.DateField(blank=True, null=True)
    user_eap = models.CharField(max_length=50, blank=True, null=True)
    mtu = models.CharField(max_length=4, blank=True, null=True)
    pool_mk = models.CharField(max_length=50, blank=True, null=True)
    guid_tmp = models.CharField(max_length=50, blank=True, null=True)
    cd_splitter = models.IntegerField(blank=True, null=True)
    id_porta_splitter = models.IntegerField(blank=True, null=True)
    nasportidname = models.CharField(max_length=100, blank=True, null=True)
    cd_ip_gerencia = models.IntegerField(unique=True, blank=True, null=True)
    onu_serial = models.CharField(max_length=50, blank=True, null=True)
    tecnologia = models.CharField(max_length=1, blank=True, null=True)
    cd_porta_cliente = models.IntegerField(blank=True, null=True)
    fiber_metros_usados = models.FloatField(blank=True, null=True)
    fiber_tipo_cabo = models.IntegerField(blank=True, null=True)
    interface_olt = models.CharField(max_length=10, blank=True, null=True)
    porta_condominio = models.IntegerField(blank=True, null=True)
    cd_end_ip_equipamento = models.IntegerField(unique=True, blank=True, null=True)
    hotspot_bypassed = models.CharField(max_length=1, blank=True, null=True)
    obs = models.TextField(blank=True, null=True)
    hash_webfilter_mara = models.TextField(blank=True, null=True)
    web_filter = models.CharField(max_length=1, blank=True, null=True)
    cache_rota = models.CharField(max_length=1000, blank=True, null=True)
    sera_reduzido = models.CharField(max_length=1, blank=True, null=True)
    ultima_reducao = models.DateField(blank=True, null=True)
    esta_reduzida = models.CharField(max_length=1, blank=True, null=True)
    conta_gerou_reducao = models.IntegerField(blank=True, null=True)
    ht_hr_criacao = models.DateTimeField(blank=True, null=True)
    id_netmaps = models.CharField(max_length=50, blank=True, null=True)
    cd_empresa = models.IntegerField(blank=True, null=True)
    classificacao_acesso = models.CharField(max_length=1, blank=True, null=True)
    modelo_mta = models.CharField(max_length=30, blank=True, null=True)
    mac_mta = models.CharField(max_length=30, blank=True, null=True)
    mac_cpe = models.CharField(max_length=30, blank=True, null=True)
    perfil_prov_cmts = models.IntegerField(blank=True, null=True)
    tipo_prov_cmts = models.CharField(max_length=1, blank=True, null=True)
    data_hora_criacao = models.DateTimeField(blank=True, null=True)
    cd_circuito_designador = models.CharField(max_length=30, blank=True, null=True)
    end_igual_cadastro = models.CharField(max_length=1, blank=True, null=True)
    cd_bloco_ipv6 = models.IntegerField(blank=True, null=True)
    sera_inadimplente = models.CharField(max_length=1, blank=True, null=True)
    esta_inadimplente = models.CharField(max_length=1, blank=True, null=True)
    dt_ultima_inadimplencia = models.DateField(blank=True, null=True)
    cd_conta_fat_inadimplencia = models.IntegerField(blank=True, null=True)
    hash_controle_insercao = models.CharField(max_length=50, blank=True, null=True)
    usar_ipv6 = models.CharField(max_length=1, blank=True, null=True)
    prefixo_ipv6 = models.IntegerField(blank=True, null=True)
    prefixo_delegado_ipv6 = models.IntegerField(blank=True, null=True)
    range_delegado_ipv6 = models.IntegerField(blank=True, null=True)
    range_prefixo_ipv6 = models.IntegerField(blank=True, null=True)
    nivel_sinal_ftth = models.IntegerField(blank=True, null=True)
    nivel_sinal_ftth_anterior = models.IntegerField(blank=True, null=True)
    porta_http = models.IntegerField(blank=True, null=True)
    nivel_sinal_ftth_real = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    nivel_sinal_ftth_anterior_real = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    ultima_atualizacao_sinal = models.DateTimeField(blank=True, null=True)
    cd_plano_autorizado = models.IntegerField(blank=True, null=True)
    dt_limite_autoriza_plano = models.DateField(blank=True, null=True)
    cd_lead = models.IntegerField(blank=True, null=True)
    framedipv6prefix = models.CharField(max_length=45, blank=True, null=True)
    cd_ate_ref_abertura = models.IntegerField(blank=True, null=True)
    sinal_rx_inicial = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    temperatura_inicial = models.IntegerField(blank=True, null=True)
    distancia_inicial = models.IntegerField(blank=True, null=True)
    sinal_tx_inicial = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    cd_caixa = models.ForeignKey('MkFiberCaixa', models.DO_NOTHING, db_column='cd_caixa', blank=True, null=True)
    tx_ccq = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mk_conexoes'


class MkContratos(models.Model):
    cancelado = models.CharField(max_length=1, blank=True, null=True)
    cliente = models.ForeignKey('MkPessoas', models.DO_NOTHING, db_column='cliente')
    adesao = models.DateField()
    previsao_vencimento = models.DateField(blank=True, null=True)
    plano_acesso = models.IntegerField()
    bloquear_automaticamente = models.IntegerField(blank=True, null=True)
    forma_pgto = models.IntegerField(blank=True, null=True)
    profile_pgto = models.IntegerField(blank=True, null=True)
    vendedor = models.IntegerField(blank=True, null=True)
    renovado_ate = models.DateField(blank=True, null=True)
    historico_eventos = models.TextField(blank=True, null=True)
    aceita_emails = models.CharField(max_length=1, blank=True, null=True)
    bloq_auto_contrato = models.IntegerField(blank=True, null=True)
    dia_vencimento = models.IntegerField(blank=True, null=True)
    contrato_eletronico = models.CharField(max_length=1, blank=True, null=True)
    codcontrato = models.AutoField(primary_key=True)
    vlr_adesao = models.FloatField(blank=True, null=True)
    parcelamento_adesao = models.IntegerField(blank=True, null=True)
    codigo_os = models.IntegerField(blank=True, null=True)
    numero_ips = models.IntegerField(blank=True, null=True)
    primeiro_vencimento = models.DateField(blank=True, null=True)
    percentual_multa = models.FloatField(blank=True, null=True)
    percentual_acrescimo = models.FloatField(blank=True, null=True)
    aceita_pgto_sac = models.CharField(max_length=1, blank=True, null=True)
    percentual_multa_sac = models.FloatField(blank=True, null=True)
    precisa_renovar = models.CharField(max_length=1, blank=True, null=True)
    pre_pago = models.CharField(max_length=1, blank=True, null=True)
    desconto_aplicado = models.IntegerField(blank=True, null=True)
    dt_cancelamento = models.DateField(blank=True, null=True)
    user_cancelamento = models.CharField(max_length=50, blank=True, null=True)
    motivo_cancelamento = models.TextField(blank=True, null=True)
    remover_parcelas_restantes = models.CharField(max_length=1, blank=True, null=True)
    parcelas_a_remover = models.CharField(max_length=30, blank=True, null=True)
    remover_conexao = models.CharField(max_length=1, blank=True, null=True)
    dt_agendada_remocao = models.DateField(blank=True, null=True)
    historico_alteracao = models.TextField(blank=True, null=True)
    novo_dia_vencimento = models.IntegerField(blank=True, null=True)
    novo_plano = models.IntegerField(blank=True, null=True)
    parcelas_a_alterar = models.CharField(max_length=30, blank=True, null=True)
    agencia_debito = models.IntegerField(blank=True, null=True)
    id_cliente_banco = models.CharField(max_length=14, blank=True, null=True)
    nf_21 = models.CharField(max_length=1, blank=True, null=True)
    nf_pre = models.CharField(max_length=1, blank=True, null=True)
    altera_valor_cancel = models.CharField(max_length=1, blank=True, null=True)
    vlr_parcial_cancelamento = models.FloatField(blank=True, null=True)
    altera_valor_alter = models.CharField(max_length=1, blank=True, null=True)
    vlr_parcial_alteracao = models.FloatField(blank=True, null=True)
    regra_comissao = models.IntegerField(blank=True, null=True)
    pre_cadastro = models.IntegerField(blank=True, null=True)
    contrato_assinado = models.CharField(max_length=1, blank=True, null=True)
    dt_assinatura = models.DateField(blank=True, null=True)
    grupo = models.IntegerField(blank=True, null=True)
    subgrupo = models.IntegerField(blank=True, null=True)
    bloqueia_por_os = models.CharField(max_length=1, blank=True, null=True)
    renovar_auto = models.CharField(max_length=1, blank=True, null=True)
    ignora_renovacao_auto = models.CharField(max_length=1, blank=True, null=True)
    renovar_por_valor_parcela = models.CharField(max_length=1, blank=True, null=True)
    tmp_com_mensalidade = models.CharField(max_length=1, blank=True, null=True)
    tmp_dt_vencimento = models.DateField(blank=True, null=True)
    tmp_vlr_parcela = models.FloatField(blank=True, null=True)
    inativar_conexao = models.CharField(max_length=1, blank=True, null=True)
    inativar_cliente = models.CharField(max_length=1, blank=True, null=True)
    comodato = models.IntegerField(blank=True, null=True)
    id_cliente_empresa = models.CharField(max_length=26, blank=True, null=True)
    recibo_numerado = models.CharField(max_length=1, blank=True, null=True)
    nova_forma_pgto = models.IntegerField(blank=True, null=True)
    nova_profile = models.IntegerField(blank=True, null=True)
    comodato_simples = models.CharField(max_length=1, blank=True, null=True)
    descricao_comodato = models.TextField(blank=True, null=True)
    dt_comodato = models.DateField(blank=True, null=True)
    obs_comodato = models.TextField(blank=True, null=True)
    tmp_login = models.CharField(max_length=100, blank=True, null=True)
    conceder_desconto_inatividade = models.CharField(max_length=1, blank=True, null=True)
    unidade_financeira = models.CharField(max_length=30, blank=True, null=True)
    operador = models.CharField(max_length=30, blank=True, null=True)
    com_reg_retorno = models.CharField(max_length=1, blank=True, null=True)
    com_dt_ret = models.DateField(blank=True, null=True)
    com_hr_ret = models.CharField(max_length=10, blank=True, null=True)
    com_desc_equipamento_ret = models.TextField(blank=True, null=True)
    com_obs_ret = models.TextField(blank=True, null=True)
    com_operador_ret = models.CharField(max_length=30, blank=True, null=True)
    com_os_ret = models.IntegerField(blank=True, null=True)
    vlr_renovacao = models.FloatField(blank=True, null=True)
    modelo_nf = models.CharField(max_length=5, blank=True, null=True)
    sup_plano_difere = models.CharField(max_length=1, blank=True, null=True)
    sup_contratos_vencidos = models.CharField(max_length=1, blank=True, null=True)
    sup_parcelas_por_vencer = models.IntegerField(blank=True, null=True)
    sup_parcelas_vencidas = models.IntegerField(blank=True, null=True)
    sup_canc_com_con = models.CharField(max_length=1, blank=True, null=True)
    sup_cont_sem_con = models.CharField(max_length=1, blank=True, null=True)
    sup_dias_parc_atrasadas = models.IntegerField(blank=True, null=True)
    comodato_dt_ret = models.DateField(blank=True, null=True)
    comodato_hr_ret = models.CharField(max_length=10, blank=True, null=True)
    comodato_ret = models.CharField(max_length=1, blank=True, null=True)
    comodato_info_ret = models.TextField(blank=True, null=True)
    comodato_ret_num_os = models.IntegerField(blank=True, null=True)
    sup_prob_ret_com = models.CharField(max_length=1, blank=True, null=True)
    sup_canc_com_parc = models.IntegerField(blank=True, null=True)
    sup_vlr_ult_parcela = models.FloatField(blank=True, null=True)
    sup_vlr_parc_df_plano = models.CharField(max_length=1, blank=True, null=True)
    sup_tx_como_renovar = models.CharField(max_length=20, blank=True, null=True)
    nfse = models.CharField(max_length=1, blank=True, null=True)
    motivo_cancelamento_2 = models.IntegerField(blank=True, null=True)
    ignora_update_conexao = models.CharField(max_length=1, blank=True, null=True)
    dias_referencia = models.IntegerField(blank=True, null=True)
    tx_ref_dias_cancelamento = models.CharField(max_length=50, blank=True, null=True)
    tx_ref_dias_alteracao = models.CharField(max_length=50, blank=True, null=True)
    suspenso = models.CharField(max_length=1, blank=True, null=True)
    suspenso_dt = models.DateField(blank=True, null=True)
    suspenso_hr = models.CharField(max_length=10, blank=True, null=True)
    suspenso_operador = models.CharField(max_length=50, blank=True, null=True)
    suspenso_motivo = models.IntegerField(blank=True, null=True)
    cd_conta_tmp_alteracao = models.IntegerField(blank=True, null=True)
    metodo_faturamento = models.CharField(max_length=1, blank=True, null=True)
    versao = models.CharField(max_length=1, blank=True, null=True)
    dias_red_banda = models.IntegerField(blank=True, null=True)
    fat_auto = models.CharField(max_length=1, blank=True, null=True)
    cd_regra_faturamento = models.ForeignKey('MkFaturamentosRegras', models.DO_NOTHING, db_column='cd_regra_faturamento', blank=True, null=True)
    cd_endereco_nf = models.BigIntegerField(blank=True, null=True)
    aguarda_ativacao = models.CharField(max_length=1, blank=True, null=True)
    data_hora_ativacao = models.DateTimeField(blank=True, null=True)
    user_ativacao = models.CharField(max_length=100, blank=True, null=True)
    cd_contrato_vinculado = models.IntegerField(blank=True, null=True)
    cd_endereco_nfse = models.IntegerField(blank=True, null=True)
    iptv_conteudo_adulto = models.CharField(max_length=10, blank=True, null=True)
    dt_venda = models.DateField(blank=True, null=True)
    dt_ativacao = models.DateField(blank=True, null=True)
    obs_cancelamento_sist = models.TextField(blank=True, null=True)
    obs_alteracao_sist = models.TextField(blank=True, null=True)
    obs_nf = models.TextField(blank=True, null=True)
    cd_empresa = models.IntegerField(blank=True, null=True)
    dt_agendada_inativ_conex = models.DateField(blank=True, null=True)
    dt_agendada_inativ_cli = models.DateField(blank=True, null=True)
    cd_lead = models.IntegerField(blank=True, null=True)
    cd_perfil_cartao_credito = models.IntegerField(blank=True, null=True)
    cd_regua_configuracao = models.ForeignKey('MkReguaTipo', models.DO_NOTHING, db_column='cd_regua_configuracao', blank=True, null=True)
    dt_hr_insert = models.DateTimeField(blank=True, null=True)
    guid_id_gerecao = models.CharField(max_length=50, blank=True, null=True)
    abrir_os_retirada = models.CharField(max_length=1, blank=True, null=True)
    tv_cod_assinante = models.CharField(max_length=80, blank=True, null=True)
    tv_idorder = models.CharField(max_length=-1, blank=True, null=True)
    cd_tabela_sla = models.ForeignKey('MkSla', models.DO_NOTHING, db_column='cd_tabela_sla', blank=True, null=True)
    rever_contas_antes_faturar = models.CharField(max_length=1, blank=True, null=True)
    tipo_plano = models.IntegerField(blank=True, null=True)
    ignora_fatura_na_geracao_conta = models.CharField(max_length=1, blank=True, null=True)
    criar_conta_pelo_vlr_sugerido = models.CharField(max_length=1, blank=True, null=True)
    erro_ao_ativar_auto = models.CharField(max_length=1, blank=True, null=True)
    cd_agrupador = models.ForeignKey('MkContratosAgrupadores', models.DO_NOTHING, db_column='cd_agrupador', blank=True, null=True)
    plano_contas_adesao = models.CharField(max_length=50, blank=True, null=True)
    obs_adesao = models.TextField(blank=True, null=True)
    vlr_adesao_condicao = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    parcelamento_adesao_condicao = models.IntegerField(blank=True, null=True)
    consultor_crm = models.IntegerField(blank=True, null=True)
    enviar_bv = models.CharField(max_length=1, blank=True, null=True)
    email_dst_bv = models.CharField(max_length=200, blank=True, null=True)
    assunto_bv = models.CharField(max_length=200, blank=True, null=True)
    tx_bv = models.TextField(blank=True, null=True)
    gravar_modelo_bv = models.CharField(max_length=1, blank=True, null=True)
    gravar_modelo_bv_plano = models.CharField(max_length=1, blank=True, null=True)
    gravar_bv_default = models.CharField(max_length=1, blank=True, null=True)
    cd_bv = models.IntegerField(blank=True, null=True)
    forma_pgto_ade = models.IntegerField(blank=True, null=True)
    gerar_adesao_imediata = models.CharField(max_length=1, blank=True, null=True)
    adesao_gerada = models.CharField(max_length=1, blank=True, null=True)
    gerar_ade_agora = models.CharField(max_length=1, blank=True, null=True)
    obs_extra_nf = models.CharField(max_length=50, blank=True, null=True)
    tv_usuario = models.CharField(max_length=120, blank=True, null=True)
    tv_senha = models.CharField(max_length=80, blank=True, null=True)
    conta_email_bv = models.IntegerField(blank=True, null=True)
    tv_situacao = models.CharField(max_length=1, blank=True, null=True)
    cd_composicao_derivacao = models.ForeignKey('MkPlanosAcesso', models.DO_NOTHING, db_column='cd_composicao_derivacao', blank=True, null=True)
    num_terminal_telefonico = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mk_contratos'


class MkContratosAgrupadores(models.Model):
    codcntagrupador = models.AutoField(primary_key=True)
    cd_cliente = models.ForeignKey('MkPessoas', models.DO_NOTHING, db_column='cd_cliente', blank=True, null=True)
    descricao = models.CharField(max_length=50, blank=True, null=True)
    inativo = models.CharField(max_length=1, blank=True, null=True)
    cd_endereco_doc = models.ForeignKey('MkPessoasEnderecos', models.DO_NOTHING, db_column='cd_endereco_doc', blank=True, null=True)
    tipo_endereco = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mk_contratos_agrupadores'


class MkEstados(models.Model):
    codestado = models.AutoField(primary_key=True)
    siglaestado = models.CharField(max_length=2, blank=True, null=True)
    nomeestado = models.CharField(max_length=50)
    ibge = models.IntegerField(blank=True, null=True)
    nao_encontrato = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mk_estados'


class MkFatV2(models.Model):
    codfat = models.AutoField(primary_key=True)
    id_operador = models.IntegerField(blank=True, null=True)
    dh = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    id_operador_efetiva = models.IntegerField(blank=True, null=True)
    dh_efetiva = models.DateTimeField(blank=True, null=True)
    di = models.DateField(blank=True, null=True)
    df = models.DateField(blank=True, null=True)
    vcto = models.DateField(blank=True, null=True)
    vlr_total = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    qtde_total = models.IntegerField(blank=True, null=True)
    cd_empresa = models.IntegerField(blank=True, null=True)
    cd_regra = models.ForeignKey('MkFaturamentosRegras', models.DO_NOTHING, db_column='cd_regra', blank=True, null=True)
    incluir_descontos = models.CharField(max_length=1, blank=True, null=True)
    incluir_repescagem = models.CharField(max_length=1, blank=True, null=True)
    incluir_avulsas = models.CharField(max_length=1, blank=True, null=True)
    vlr_contrato = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    vlr_desconto = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    vlr_lctos_avulsos = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    vlr_repescagem = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    processamento = models.IntegerField(blank=True, null=True)
    vlr_total_faturas = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    ref_di = models.DateField(blank=True, null=True)
    ref_df = models.DateField(blank=True, null=True)
    tipo_faturamento = models.IntegerField(blank=True, null=True)
    cd_profile = models.IntegerField(blank=True, null=True)
    dh_exclusao = models.DateTimeField(blank=True, null=True)
    id_ope_exclusao = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mk_fat_v2'


class MkFaturamentosRegras(models.Model):
    codfaturamentoregra = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=150, blank=True, null=True)
    periodo1_inicio = models.SmallIntegerField(blank=True, null=True)
    periodo1_final = models.SmallIntegerField(blank=True, null=True)
    periodo1_fechamento = models.SmallIntegerField(blank=True, null=True)
    periodo1_vencimento = models.SmallIntegerField(blank=True, null=True)
    periodo1_mes_sub = models.CharField(max_length=1, blank=True, null=True)
    habilita_periodo2 = models.CharField(max_length=1, blank=True, null=True)
    periodo2_inicio = models.SmallIntegerField(blank=True, null=True)
    periodo2_final = models.SmallIntegerField(blank=True, null=True)
    periodo2_fechamento = models.SmallIntegerField(blank=True, null=True)
    periodo2_vencimento = models.SmallIntegerField(blank=True, null=True)
    periodo2_mes_sub = models.CharField(max_length=1, blank=True, null=True)
    tipo = models.CharField(max_length=1, blank=True, null=True)
    considera_ordem_fat = models.CharField(max_length=1, blank=True, null=True)
    tipo_regra = models.IntegerField(blank=True, null=True)
    tipo_periodo = models.IntegerField(blank=True, null=True)
    dia_inicio = models.IntegerField(blank=True, null=True)
    dia_vcto = models.IntegerField(blank=True, null=True)
    pre_gerar_prox_mes = models.CharField(max_length=1, blank=True, null=True)
    inativo = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mk_faturamentos_regras'


class MkFaturas(models.Model):
    codfatura = models.AutoField(primary_key=True)
    data_lancamento = models.DateTimeField(blank=True, null=True)
    usuario_lancamento = models.CharField(max_length=100, blank=True, null=True)
    valor_total = models.FloatField(blank=True, null=True)
    data_vencimento = models.DateField(blank=True, null=True)
    excluida = models.CharField(max_length=1, blank=True, null=True)
    usuario_exclusao = models.CharField(max_length=100, blank=True, null=True)
    data_exclusao = models.DateTimeField(blank=True, null=True)
    cd_pessoa = models.ForeignKey('MkPessoas', models.DO_NOTHING, db_column='cd_pessoa', blank=True, null=True)
    tipo_lancamento = models.CharField(max_length=50, blank=True, null=True)
    liquidado = models.CharField(max_length=1, blank=True, null=True)
    data_liquidacao = models.DateField(blank=True, null=True)
    hora_liquidacao = models.CharField(max_length=8, blank=True, null=True)
    vlr_liquidacao = models.FloatField(blank=True, null=True)
    usuario_liquidacao = models.CharField(max_length=30, blank=True, null=True)
    hora_exclusao = models.CharField(max_length=8, blank=True, null=True)
    cd_faturamento = models.ForeignKey(MkFatV2, models.DO_NOTHING, db_column='cd_faturamento', blank=True, null=True)
    guid_selecao = models.CharField(max_length=100, blank=True, null=True)
    tx_multa_atraso = models.FloatField(blank=True, null=True)
    tx_juro_atraso = models.FloatField(blank=True, null=True)
    dt_ref_inicial = models.DateField(blank=True, null=True)
    dt_ref_final = models.DateField(blank=True, null=True)
    descricao = models.CharField(max_length=250, blank=True, null=True)
    forma_pgto_liquidacao = models.IntegerField(blank=True, null=True)
    obs_liquidacao = models.TextField(blank=True, null=True)
    documento_liquidacao = models.CharField(max_length=20, blank=True, null=True)
    ponto_recebimento_liquidacao = models.IntegerField(blank=True, null=True)
    dt_efetivacao_credito = models.DateField(blank=True, null=True)
    vlr_acrescimo_aplicado = models.FloatField(blank=True, null=True)
    vlr_desconto_aplicado = models.FloatField(blank=True, null=True)
    vlr_tarifa_aplicada = models.FloatField(blank=True, null=True)
    desconto_maximo_aplicavel = models.FloatField(blank=True, null=True)
    data_desconto_maximo = models.DateField(blank=True, null=True)
    suspenso = models.CharField(max_length=1, blank=True, null=True)
    data_vencimento_original = models.DateField(blank=True, null=True)
    valor_total_original = models.FloatField(blank=True, null=True)
    num_reprogramacao = models.IntegerField(blank=True, null=True)
    info_reprogramacao = models.TextField(blank=True, null=True)
    cd_motivo_suspensao = models.IntegerField(blank=True, null=True)
    exportacao = models.CharField(max_length=1, blank=True, null=True)
    exportacao_data_hora = models.DateTimeField(blank=True, null=True)
    exportacao_arquivo = models.CharField(max_length=100, blank=True, null=True)
    agrupamento = models.CharField(max_length=30, blank=True, null=True)
    usuario_suspensao = models.CharField(max_length=100, blank=True, null=True)
    data_suspensao = models.DateTimeField(blank=True, null=True)
    obs_suspensao = models.TextField(blank=True, null=True)
    obs_fatura = models.TextField(blank=True, null=True)
    liquidado_por_retorno = models.CharField(max_length=1, blank=True, null=True)
    num_arq_retorno = models.IntegerField(blank=True, null=True)
    cd_empresa = models.IntegerField(blank=True, null=True)
    estornado = models.CharField(max_length=1, blank=True, null=True)
    data_estorno = models.DateField(blank=True, null=True)
    hora_estorno = models.CharField(max_length=8, blank=True, null=True)
    vlr_estorno = models.FloatField(blank=True, null=True)
    usuario_estorno = models.CharField(max_length=30, blank=True, null=True)
    tipo = models.CharField(max_length=1, blank=True, null=True)
    documento_cobranca = models.CharField(max_length=30, blank=True, null=True)
    dt_hr_evento_liquidacao = models.DateTimeField(blank=True, null=True)
    doc_fiscais_gerados = models.CharField(max_length=1, blank=True, null=True)
    nomenclatura_integracao = models.CharField(max_length=3, blank=True, null=True)
    cd_vinculado = models.IntegerField(blank=True, null=True)
    barras_cobranca = models.CharField(unique=True, max_length=100, blank=True, null=True)
    ld_cobranca = models.CharField(unique=True, max_length=100, blank=True, null=True)
    dh_geracao = models.DateTimeField(blank=True, null=True)
    id_operador = models.IntegerField(blank=True, null=True)
    tipo_cobranca = models.IntegerField(blank=True, null=True)
    dh_registro = models.DateTimeField(blank=True, null=True)
    numero_cobranca = models.CharField(max_length=20, blank=True, null=True)
    cd_profile_cobranca = models.IntegerField(blank=True, null=True)
    cd_doc_cobranca = models.IntegerField(blank=True, null=True)
    opcao_lcto = models.IntegerField(blank=True, null=True)
    plano_contas = models.ForeignKey('MkUnidadeFinanceia', models.DO_NOTHING, db_column='plano_contas', blank=True, null=True)
    cc_departamentos = models.ForeignKey(MkCcRateio, models.DO_NOTHING, db_column='cc_departamentos', blank=True, null=True)
    cc_servicos = models.ForeignKey(MkCcRateio, models.DO_NOTHING, db_column='cc_servicos', blank=True, null=True)
    cc_projetos = models.ForeignKey(MkCcRateio, models.DO_NOTHING, db_column='cc_projetos', blank=True, null=True)
    cc_area_negocios = models.ForeignKey(MkCcRateio, models.DO_NOTHING, db_column='cc_area_negocios', blank=True, null=True)
    dh_insert = models.DateTimeField(blank=True, null=True)
    conta_fixa = models.CharField(max_length=1, blank=True, null=True)
    cd_agrupador = models.ForeignKey(MkContratosAgrupadores, models.DO_NOTHING, db_column='cd_agrupador', blank=True, null=True)
    saldo_restante = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    valor_liquidado = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    ver_geracao_doc_fiscal = models.IntegerField(blank=True, null=True)
    teve_liquidacao_parcial = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mk_faturas'


class MkFiberArmarios(models.Model):
    codarmario = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=50, blank=True, null=True)
    latitude = models.CharField(max_length=50, blank=True, null=True)
    logitude = models.CharField(max_length=50, blank=True, null=True)
    cd_uf = models.IntegerField(blank=True, null=True)
    cd_cidade = models.IntegerField(blank=True, null=True)
    cd_bairro = models.IntegerField(blank=True, null=True)
    cd_logradouro = models.IntegerField(blank=True, null=True)
    numero = models.IntegerField(blank=True, null=True)
    complemento = models.CharField(max_length=30, blank=True, null=True)
    cep = models.CharField(max_length=9, blank=True, null=True)
    capacidade_pops = models.IntegerField(blank=True, null=True)
    dt_instalacao = models.DateField(blank=True, null=True)
    hr_instalacao = models.CharField(max_length=10, blank=True, null=True)
    observacoes = models.TextField(blank=True, null=True)
    projeto = models.CharField(max_length=1, blank=True, null=True)
    valor_estimado = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    cd_projeto = models.ForeignKey('MkFiberProjeto', models.DO_NOTHING, db_column='cd_projeto', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mk_fiber_armarios'


class MkFiberCabos(models.Model):
    codcabo = models.AutoField(primary_key=True)
    identificao = models.CharField(max_length=50)
    qtde_fibras = models.IntegerField(blank=True, null=True)
    cd_cabotipo = models.IntegerField(blank=True, null=True)
    cd_splitter = models.IntegerField(blank=True, null=True)
    cd_armario = models.IntegerField(blank=True, null=True)
    cd_caixa = models.IntegerField(blank=True, null=True)
    cd_cabo_destino = models.IntegerField(blank=True, null=True)
    projeto = models.CharField(max_length=1, blank=True, null=True)
    hr_instalacao = models.CharField(max_length=16, blank=True, null=True)
    dt_instalacao = models.DateField(blank=True, null=True)
    tamanho_cabo = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    cd_projeto = models.IntegerField(blank=True, null=True)
    valor_estimado = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    qtde_fibras_tuboloose = models.IntegerField(blank=True, null=True)
    cd_fabricante = models.IntegerField(blank=True, null=True)
    cd_padrao = models.IntegerField(blank=True, null=True)
    especificacoes = models.TextField(blank=True, null=True)
    cor = models.CharField(max_length=20, blank=True, null=True)
    json_cabo = models.TextField(blank=True, null=True)
    cd_proprietario_cabo = models.IntegerField(blank=True, null=True)
    sigla = models.CharField(max_length=10, blank=True, null=True)
    perda_sinal_km = models.DecimalField(max_digits=9, decimal_places=3, blank=True, null=True)
    data_hora_atualizacao = models.DateTimeField(blank=True, null=True)
    cabo_interligacao = models.CharField(max_length=1, blank=True, null=True)
    cd_ligacao_diagrama = models.IntegerField(unique=True, blank=True, null=True)
    cabo_drop = models.CharField(max_length=1, blank=True, null=True)
    cd_porta_nap = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mk_fiber_cabos'


class MkFiberCabosFibras(models.Model):
    codcabofibra = models.AutoField(primary_key=True)
    sequencia = models.DecimalField(max_digits=9, decimal_places=2)
    cd_cabo = models.IntegerField(blank=True, null=True)
    id = models.CharField(max_length=20, blank=True, null=True)
    cor = models.CharField(max_length=20, blank=True, null=True)
    cd_splitter_porta = models.IntegerField(blank=True, null=True)
    cd_pop_porta = models.ForeignKey('MkFiberPopPortas', models.DO_NOTHING, db_column='cd_pop_porta', blank=True, null=True)
    cd_splitter = models.ForeignKey('MkFiberSplitter', models.DO_NOTHING, db_column='cd_splitter', blank=True, null=True)
    cd_conexao = models.IntegerField(blank=True, null=True)
    cd_cabofibra = models.IntegerField(blank=True, null=True)
    cd_tuboloose = models.ForeignKey('MkFiberCabosTuboLoose', models.DO_NOTHING, db_column='cd_tuboloose', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mk_fiber_cabos_fibras'


class MkFiberCabosSegmento(models.Model):
    codseguimento = models.AutoField(primary_key=True)
    cd_armario = models.ForeignKey(MkFiberArmarios, models.DO_NOTHING, db_column='cd_armario', blank=True, null=True)
    cd_splitter = models.IntegerField(blank=True, null=True)
    cd_poste_inicio = models.ForeignKey('MkFiberPostes', models.DO_NOTHING, db_column='cd_poste_inicio', blank=True, null=True)
    cd_poste_fim = models.ForeignKey('MkFiberPostes', models.DO_NOTHING, db_column='cd_poste_fim', blank=True, null=True)
    tamanho_segmento = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    cd_cabo = models.ForeignKey(MkFiberCabos, models.DO_NOTHING, db_column='cd_cabo', blank=True, null=True)
    sequencia = models.IntegerField(blank=True, null=True)
    guid_alteracao = models.CharField(max_length=50, blank=True, null=True)
    tamanho_segmento_acumulado = models.DecimalField(max_digits=18, decimal_places=3, blank=True, null=True)
    data_hora_atualizacao = models.DateTimeField(blank=True, null=True)
    cd_poste_cabo_inicio = models.IntegerField(blank=True, null=True)
    cd_poste_cabo_fim = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mk_fiber_cabos_segmento'


class MkFiberCabosTipo(models.Model):
    codcabotipo = models.AutoField(primary_key=True)
    desc_tipo = models.CharField(max_length=100)
    fibras = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    tubosloose = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    valor_estimado_m = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    cd_padrao = models.ForeignKey('MkFiberFibraCoresPadrao', models.DO_NOTHING, db_column='cd_padrao', blank=True, null=True)
    cd_fabricante = models.IntegerField(blank=True, null=True)
    especificacoes = models.TextField(blank=True, null=True)
    qtde_fibras = models.IntegerField(blank=True, null=True)
    perda_sinal_km = models.DecimalField(max_digits=9, decimal_places=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mk_fiber_cabos_tipo'


class MkFiberCabosTuboLoose(models.Model):
    codtuboloose = models.AutoField(primary_key=True)
    id = models.CharField(max_length=20)
    cor = models.CharField(max_length=20, blank=True, null=True)
    quantidade = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    cd_cabo = models.ForeignKey(MkFiberCabos, models.DO_NOTHING, db_column='cd_cabo', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mk_fiber_cabos_tubo_loose'


class MkFiberCaixa(models.Model):
    codcaixa = models.IntegerField(primary_key=True)
    identificacao = models.CharField(max_length=29)
    tipo = models.IntegerField(blank=True, null=True)
    cd_poste = models.ForeignKey('MkFiberPostes', models.DO_NOTHING, db_column='cd_poste', blank=True, null=True)
    indice_perda = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    qtde_portas = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    latitude = models.CharField(max_length=50, blank=True, null=True)
    longitude = models.CharField(max_length=50, blank=True, null=True)
    projeto = models.CharField(max_length=1, blank=True, null=True)
    data_instalacao = models.DateField(blank=True, null=True)
    hora_instalacao = models.CharField(max_length=10, blank=True, null=True)
    valor_estimado = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    cd_projeto = models.ForeignKey('MkFiberProjeto', models.DO_NOTHING, db_column='cd_projeto', blank=True, null=True)
    codtipocaixa = models.IntegerField(blank=True, null=True)
    numero_inicial = models.IntegerField(blank=True, null=True)
    numero_final = models.IntegerField(blank=True, null=True)
    auto_anuncio = models.CharField(max_length=5, blank=True, null=True)
    limite_portas_anuncio = models.IntegerField(blank=True, null=True)
    raio_atendimento = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    cd_armario = models.ForeignKey(MkFiberArmarios, models.DO_NOTHING, db_column='cd_armario', blank=True, null=True)
    desbalanceado = models.CharField(max_length=1, blank=True, null=True)
    registro_key = models.CharField(max_length=100, blank=True, null=True)
    diagrama = models.TextField(blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    diagrama_html = models.TextField(blank=True, null=True)
    prospectado = models.CharField(max_length=1, blank=True, null=True)
    qr_code = models.BinaryField(blank=True, null=True)
    json_ligacoes = models.TextField(blank=True, null=True)
    guid_caixa = models.CharField(max_length=40, blank=True, null=True)
    versao_diagrama_mk = models.IntegerField(blank=True, null=True)
    local_diagrama = models.CharField(max_length=10, blank=True, null=True)
    outras_especificacoes = models.CharField(max_length=500, blank=True, null=True)
    auto_provisionamento = models.CharField(max_length=1, blank=True, null=True)
    cd_sistema_operacional = models.ForeignKey('MkSo', models.DO_NOTHING, db_column='cd_sistema_operacional', blank=True, null=True)
    rascunho = models.CharField(max_length=1, blank=True, null=True)
    cd_ponto_acesso = models.ForeignKey('MkPontosAcesso', models.DO_NOTHING, db_column='cd_ponto_acesso', blank=True, null=True)
    cd_porta_pop = models.ForeignKey('MkFiberPortas', models.DO_NOTHING, db_column='cd_porta_pop', blank=True, null=True)
    nivel_sinal_ftth = models.IntegerField(blank=True, null=True)
    nivel_sinal_ftth_anterior = models.IntegerField(blank=True, null=True)
    nivel_sinal_ftth_real = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    nivel_sinal_ftth_anterior_real = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    ultima_atualizacao = models.DateTimeField(blank=True, null=True)
    temperatura_capturada = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    serial = models.CharField(max_length=50, blank=True, null=True)
    distancia_capturada = models.IntegerField(blank=True, null=True)
    caixa_generica = models.CharField(max_length=1, blank=True, null=True)
    cd_armario_anterior = models.IntegerField(blank=True, null=True)
    diagrama_legado = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mk_fiber_caixa'


class MkFiberCaixaTipo(models.Model):
    codtipocaixa = models.AutoField(primary_key=True)
    tipo = models.IntegerField()
    indice_perda = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    valor_estimado = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    decricao = models.TextField(blank=True, null=True)
    nome_tipo = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mk_fiber_caixa_tipo'


class MkFiberDiagramaLigacoes(models.Model):
    coddiagramaligacao = models.AutoField(primary_key=True)
    origem = models.CharField(max_length=40, blank=True, null=True)
    destino = models.CharField(max_length=40, blank=True, null=True)
    id_sentido_origem = models.IntegerField(blank=True, null=True)
    id_sentido_destino = models.IntegerField(blank=True, null=True)
    id_origem = models.IntegerField(blank=True, null=True)
    id_destino = models.IntegerField(blank=True, null=True)
    lado_sentido_destino = models.CharField(max_length=1, blank=True, null=True)
    lado_sentido_origem = models.CharField(max_length=1, blank=True, null=True)
    nome_destino = models.CharField(max_length=50, blank=True, null=True)
    nome_origem = models.CharField(max_length=50, blank=True, null=True)
    nome_ligacao = models.CharField(max_length=100, blank=True, null=True)
    porta_iluminacao_destino = models.IntegerField(blank=True, null=True)
    porta_iluminacao_origem = models.IntegerField(blank=True, null=True)
    tipo_sentido_origem = models.CharField(max_length=20, blank=True, null=True)
    tipo_sentido_destino = models.CharField(max_length=20, blank=True, null=True)
    tipo_origem = models.CharField(max_length=20, blank=True, null=True)
    tipo_destino = models.CharField(max_length=20, blank=True, null=True)
    guid_caixa_emenda = models.CharField(max_length=50, blank=True, null=True)
    cd_caixa_emenda = models.IntegerField(blank=True, null=True)
    removida = models.CharField(max_length=1, blank=True, null=True)
    hash_ligacao = models.CharField(max_length=50, blank=True, null=True)
    segmento_destino = models.IntegerField(blank=True, null=True)
    segmento_origem = models.IntegerField(blank=True, null=True)
    data_hora_alteracao = models.DateTimeField(blank=True, null=True)
    hash_alteracao = models.CharField(max_length=50, blank=True, null=True)
    cd_elemento_inicio = models.IntegerField(blank=True, null=True)
    cd_elemento_fim = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mk_fiber_diagrama_ligacoes'


class MkFiberEmendaElementos(models.Model):
    codelementoemenda = models.AutoField(primary_key=True)
    cd_cabo = models.IntegerField(blank=True, null=True)
    cd_caixa = models.IntegerField(blank=True, null=True)
    lado = models.CharField(max_length=1, blank=True, null=True)
    id_origem = models.IntegerField(blank=True, null=True)
    tipo_origem = models.CharField(max_length=50, blank=True, null=True)
    cd_caixa_emenda = models.IntegerField(blank=True, null=True)
    nome_origem = models.CharField(max_length=100, blank=True, null=True)
    guid_caixa = models.CharField(max_length=50, blank=True, null=True)
    removida = models.CharField(max_length=1, blank=True, null=True)
    copia = models.CharField(max_length=1, blank=True, null=True)
    cd_pop = models.IntegerField(blank=True, null=True)
    cd_outros_equipamentos = models.IntegerField(blank=True, null=True)
    elemento_top = models.CharField(max_length=10, blank=True, null=True)
    elemento_left = models.CharField(max_length=10, blank=True, null=True)
    hash_elemento = models.CharField(max_length=100, blank=True, null=True)
    pos_top = models.CharField(max_length=20, blank=True, null=True)
    pos_left = models.CharField(max_length=20, blank=True, null=True)
    cd_cabo_segmento = models.IntegerField(blank=True, null=True)
    caixa_versao_layout = models.CharField(max_length=10, blank=True, null=True)
    tipo_elemento = models.CharField(max_length=20, blank=True, null=True)
    sequencia_elemento = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mk_fiber_emenda_elementos'


class MkFiberFabricanteEquipamento(models.Model):
    codfabricante = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50, blank=True, null=True)
    cd_so = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mk_fiber_fabricante_equipamento'


class MkFiberFibraCoresPadrao(models.Model):
    codpadrao = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=85)
    descricao = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mk_fiber_fibra_cores_padrao'


class MkFiberMarcadores(models.Model):
    codmarcador = models.AutoField(primary_key=True)
    marcador_nome = models.CharField(max_length=50)
    marcador_descricao = models.TextField(blank=True, null=True)
    marcador_latitude = models.CharField(max_length=30, blank=True, null=True)
    marcador_longitude = models.CharField(max_length=30, blank=True, null=True)
    marcador_imagem = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mk_fiber_marcadores'


class MkFiberModeloEquipamento(models.Model):
    codmodeloequipamento = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50, blank=True, null=True)
    modelo = models.CharField(max_length=50, blank=True, null=True)
    portas = models.IntegerField(blank=True, null=True)
    especificacao = models.CharField(max_length=5000, blank=True, null=True)
    cd_tipo = models.ForeignKey('MkFiberTipoEquipamento', models.DO_NOTHING, db_column='cd_tipo', blank=True, null=True)
    cd_fabricante = models.ForeignKey(MkFiberFabricanteEquipamento, models.DO_NOTHING, db_column='cd_fabricante', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mk_fiber_modelo_equipamento'


class MkFiberOutrosEquipamentos(models.Model):
    codoutrosequipamentos = models.AutoField(primary_key=True)
    nome_equipamento = models.CharField(max_length=100, blank=True, null=True)
    especificacao_equipamento = models.TextField(blank=True, null=True)
    latitude = models.CharField(max_length=20, blank=True, null=True)
    longitude = models.CharField(max_length=20, blank=True, null=True)
    data_instalacao = models.DateField(blank=True, null=True)
    hora_instalacao = models.CharField(max_length=10, blank=True, null=True)
    icone_equipamento = models.BinaryField(blank=True, null=True)
    valor_equipamento = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    projeto = models.CharField(max_length=1, blank=True, null=True)
    cd_projeto = models.IntegerField(blank=True, null=True)
    cd_armario = models.IntegerField(blank=True, null=True)
    cd_poste = models.IntegerField(blank=True, null=True)
    cd_modelo_equipamento = models.IntegerField(blank=True, null=True)
    cd_caixa = models.IntegerField(blank=True, null=True)
    qtde_portas = models.IntegerField(blank=True, null=True)
    indice_perda_sinal = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    cd_armario_anterior = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mk_fiber_outros_equipamentos'


class MkFiberPopPortas(models.Model):
    codpopporta = models.OneToOneField('MkFiberPortas', models.DO_NOTHING, db_column='codpopporta', primary_key=True)
    id_porta = models.IntegerField(blank=True, null=True)
    cd_pop = models.ForeignKey('MkPontosAcesso', models.DO_NOTHING, db_column='cd_pop', blank=True, null=True)
    capacidade_cliente = models.IntegerField(blank=True, null=True)
    capacidade_mb = models.FloatField(blank=True, null=True)
    limitar_capacidade = models.CharField(max_length=1, blank=True, null=True)
    cor_cabo = models.CharField(max_length=30, blank=True, null=True)
    id_porta2 = models.CharField(max_length=-1, blank=True, null=True)
    alias = models.CharField(max_length=10, blank=True, null=True)
    vlan = models.CharField(max_length=10, blank=True, null=True)
    cd_cabofibra = models.IntegerField(blank=True, null=True)
    cd_cabo = models.ForeignKey(MkFiberCabos, models.DO_NOTHING, db_column='cd_cabo', blank=True, null=True)
    cd_tubo_loose = models.IntegerField(blank=True, null=True)
    potencia_sinal = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    sinal_bom = models.DecimalField(max_digits=7, decimal_places=3, blank=True, null=True)
    sinal_medio = models.DecimalField(max_digits=7, decimal_places=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mk_fiber_pop_portas'


class MkFiberPortas(models.Model):
    codporta = models.AutoField(primary_key=True)
    cd_fibra = models.IntegerField(blank=True, null=True)
    cd_caixa = models.ForeignKey(MkFiberCaixa, models.DO_NOTHING, db_column='cd_caixa', blank=True, null=True)
    reserva = models.CharField(max_length=1, blank=True, null=True)
    ft_venc_reserva = models.DateTimeField(blank=True, null=True)
    guid_caixa_emenda = models.CharField(max_length=40, blank=True, null=True)
    emenda_removida = models.CharField(max_length=1, blank=True, null=True)
    cd_destino_fibra = models.IntegerField(blank=True, null=True)
    tipo_destino_origem_fibra = models.CharField(max_length=40, blank=True, null=True)
    id_ligacao_diagrama = models.CharField(max_length=40, blank=True, null=True)
    cd_poste_emenda = models.ForeignKey('MkFiberPostes', models.DO_NOTHING, db_column='cd_poste_emenda', blank=True, null=True)
    lado_cabo_fibra = models.CharField(max_length=1, blank=True, null=True)
    id_porta = models.IntegerField(blank=True, null=True)
    tipo_ligacao = models.IntegerField(blank=True, null=True)
    cd_armario_emenda = models.ForeignKey(MkFiberArmarios, models.DO_NOTHING, db_column='cd_armario_emenda', blank=True, null=True)
    guid_caixa_emenda_interacao = models.CharField(max_length=50, blank=True, null=True)
    cd_porta_dio = models.ForeignKey('self', models.DO_NOTHING, db_column='cd_porta_dio', blank=True, null=True)
    cd_cabo_segmento = models.IntegerField(blank=True, null=True)
    sinal_saida = models.DecimalField(max_digits=9, decimal_places=3, blank=True, null=True)
    sinal_entrada = models.DecimalField(max_digits=9, decimal_places=3, blank=True, null=True)
    cd_porta_entrada = models.ForeignKey('self', models.DO_NOTHING, db_column='cd_porta_entrada', blank=True, null=True)
    nome_elemento = models.CharField(max_length=100, blank=True, null=True)
    tipo_elemento = models.CharField(max_length=20, blank=True, null=True)
    tipo_splitter = models.CharField(max_length=10, blank=True, null=True)
    sinal_bom = models.DecimalField(max_digits=7, decimal_places=3, blank=True, null=True)
    sinal_medio = models.DecimalField(max_digits=7, decimal_places=3, blank=True, null=True)
    atualizar_segmentos = models.CharField(max_length=1, blank=True, null=True)
    cd_tipo_conector = models.ForeignKey('MkFiberTipoConector', models.DO_NOTHING, db_column='cd_tipo_conector', blank=True, null=True)
    alias = models.CharField(max_length=20, blank=True, null=True)
    cd_porta_ligada = models.ForeignKey('self', models.DO_NOTHING, db_column='cd_porta_ligada', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mk_fiber_portas'


class MkFiberPorteTipo(models.Model):
    codpostetipo = models.AutoField(primary_key=True)
    nome_tipo = models.CharField(max_length=49, blank=True, null=True)
    valor_estimado = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mk_fiber_porte_tipo'


class MkFiberPosteProprietario(models.Model):
    codproprietario = models.AutoField(primary_key=True)
    proprietario_nome = models.CharField(max_length=50)
    proprietario_custo_un = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mk_fiber_poste_proprietario'


class MkFiberPostes(models.Model):
    codposte = models.AutoField(primary_key=True)
    localizacao = models.CharField(max_length=50, blank=True, null=True)
    latitude = models.CharField(max_length=50, blank=True, null=True)
    longitude = models.CharField(max_length=50, blank=True, null=True)
    cd_uf = models.IntegerField(blank=True, null=True)
    cd_cidade = models.IntegerField(blank=True, null=True)
    cd_bairro = models.IntegerField(blank=True, null=True)
    cd_logradouro = models.IntegerField(blank=True, null=True)
    numero = models.IntegerField(blank=True, null=True)
    complemento = models.CharField(max_length=30, blank=True, null=True)
    tipo_poste = models.CharField(max_length=1, blank=True, null=True)
    identificacao = models.CharField(max_length=100, blank=True, null=True)
    cd_postetiipo = models.ForeignKey(MkFiberPorteTipo, models.DO_NOTHING, db_column='cd_postetiipo', blank=True, null=True)
    projeto = models.CharField(max_length=1, blank=True, null=True)
    data_criacao = models.DateField(blank=True, null=True)
    hora_criacao = models.CharField(max_length=13, blank=True, null=True)
    cd_projeto = models.ForeignKey('MkFiberProjeto', models.DO_NOTHING, db_column='cd_projeto', blank=True, null=True)
    elemento_mapa_json = models.TextField(blank=True, null=True)
    outras_informacoes = models.TextField(blank=True, null=True)
    cd_proprietario = models.ForeignKey(MkFiberPosteProprietario, models.DO_NOTHING, db_column='cd_proprietario', blank=True, null=True)
    outras_informacoes_json = models.TextField(blank=True, null=True)
    data_hora_atualizacao = models.DateTimeField(blank=True, null=True)
    caixa_subterranea = models.CharField(max_length=1, blank=True, null=True)
    elemento_mapa_json_mobile = models.TextField(blank=True, null=True)
    latitude_n = models.DecimalField(max_digits=20, decimal_places=20, blank=True, null=True)
    longitude_n = models.DecimalField(max_digits=20, decimal_places=20, blank=True, null=True)
    retorno_consulta_endereco = models.TextField(blank=True, null=True)
    tipo_elemento = models.IntegerField(blank=True, null=True)
    cd_conexao = models.IntegerField(blank=True, null=True)
    cd_ponto_acesso = models.IntegerField(blank=True, null=True)
    tipo_conexao = models.CharField(max_length=10, blank=True, null=True)
    url_icone = models.CharField(max_length=250, blank=True, null=True)
    cd_armario = models.ForeignKey(MkFiberArmarios, models.DO_NOTHING, db_column='cd_armario', blank=True, null=True)
    cd_marcador = models.ForeignKey(MkFiberMarcadores, models.DO_NOTHING, db_column='cd_marcador', blank=True, null=True)
    cd_usuario = models.ForeignKey(FrUsuario, models.DO_NOTHING, db_column='cd_usuario', blank=True, null=True)
    cd_pop_info = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mk_fiber_postes'


class MkFiberProjeto(models.Model):
    codprojeto = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=70)
    data_inicio = models.DateField(blank=True, null=True)
    valor_total = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    valor_executado = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    valor_orcado = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    situacao = models.IntegerField(blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mk_fiber_projeto'


class MkFiberSplitter(models.Model):
    codsplitter = models.AutoField(primary_key=True)
    latitude = models.CharField(max_length=50, blank=True, null=True)
    longitude = models.CharField(max_length=50, blank=True, null=True)
    cd_uf = models.IntegerField(blank=True, null=True)
    cd_cidade = models.IntegerField(blank=True, null=True)
    cd_bairro = models.IntegerField(blank=True, null=True)
    cd_logradouro = models.IntegerField(blank=True, null=True)
    numero = models.IntegerField(blank=True, null=True)
    complemento = models.CharField(max_length=30, blank=True, null=True)
    descricao_modelo = models.CharField(max_length=50, blank=True, null=True)
    portas = models.IntegerField(blank=True, null=True)
    id_splitter = models.CharField(max_length=30, blank=True, null=True)
    cd_pop = models.IntegerField(blank=True, null=True)
    cd_pop_porta = models.IntegerField(blank=True, null=True)
    cd_poste = models.ForeignKey(MkFiberPostes, models.DO_NOTHING, db_column='cd_poste', blank=True, null=True)
    cd_caixa = models.IntegerField(blank=True, null=True)
    codtiposplitter = models.ForeignKey('MkFiberSplitterTipo', models.DO_NOTHING, db_column='codtiposplitter', blank=True, null=True)
    cd_pontoacesso = models.IntegerField(blank=True, null=True)
    cd_splitter = models.IntegerField(blank=True, null=True)
    cd_porta_splitter = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mk_fiber_splitter'


class MkFiberSplitterTipo(models.Model):
    codtiposplitter = models.AutoField(primary_key=True)
    portas = models.IntegerField(blank=True, null=True)
    desc_modelo = models.CharField(max_length=50, blank=True, null=True)
    valor_estimado = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    indice_perda = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    codtipocaixa = models.ForeignKey(MkFiberCaixaTipo, models.DO_NOTHING, db_column='codtipocaixa', blank=True, null=True)
    desbalanceado = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mk_fiber_splitter_tipo'


class MkFiberTipoConector(models.Model):
    codconector = models.AutoField(primary_key=True)
    tipo_conector = models.CharField(max_length=20, blank=True, null=True)
    outras_especificacoes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mk_fiber_tipo_conector'


class MkFiberTipoEquipamento(models.Model):
    codtipoequipamento = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mk_fiber_tipo_equipamento'


class MkFrequencias(models.Model):
    codfreq = models.AutoField(primary_key=True)
    banda = models.CharField(max_length=1, blank=True, null=True)
    frequencia = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mk_frequencias'


class MkLogradouros(models.Model):
    codlogradouro = models.AutoField(primary_key=True)
    logradouro = models.CharField(max_length=80)
    codbairro = models.ForeignKey(MkBairros, models.DO_NOTHING, db_column='codbairro')
    cep = models.CharField(max_length=10, blank=True, null=True)
    codcidade = models.IntegerField()
    nao_encontrato = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mk_logradouros'


class MkPerfilMonitoramento(models.Model):
    codperfil = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=50, blank=True, null=True)
    guid_mestre = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mk_perfil_monitoramento'


class MkPessoas(models.Model):
    codpessoa = models.AutoField(primary_key=True)
    nome_razaosocial = models.CharField(max_length=100)
    cpf = models.CharField(max_length=15, blank=True, null=True)
    cnpj = models.CharField(max_length=20, blank=True, null=True)
    rg = models.CharField(max_length=15, blank=True, null=True)
    ie = models.CharField(max_length=15, blank=True, null=True)
    nascimento = models.DateField(blank=True, null=True)
    fundacao = models.DateField(blank=True, null=True)
    cep = models.CharField(max_length=8)
    cepcobranca = models.CharField(max_length=8)
    codcidade = models.ForeignKey(MkCidades, models.DO_NOTHING, db_column='codcidade')
    codcidadecobranca = models.IntegerField()
    codlogradouro = models.ForeignKey(MkLogradouros, models.DO_NOTHING, db_column='codlogradouro')
    codlogradourocobranca = models.IntegerField()
    codbairro = models.ForeignKey(MkBairros, models.DO_NOTHING, db_column='codbairro')
    codbairrocobranca = models.IntegerField()
    codestado = models.ForeignKey(MkEstados, models.DO_NOTHING, db_column='codestado')
    codestadocobranca = models.IntegerField()
    nomepai = models.CharField(max_length=100, blank=True, null=True)
    nomemae = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=500, blank=True, null=True)
    contato = models.CharField(max_length=100, blank=True, null=True)
    fone01 = models.CharField(max_length=20)
    fone02 = models.CharField(max_length=20, blank=True, null=True)
    fax = models.CharField(max_length=20, blank=True, null=True)
    complementoendereco = models.CharField(max_length=50, blank=True, null=True)
    complementoenderecocobr = models.CharField(max_length=50, blank=True, null=True)
    diapgto = models.IntegerField(blank=True, null=True)
    tipopgtoobservacoes = models.TextField(blank=True, null=True)
    datacadastro = models.DateField()
    enderecoweb = models.CharField(max_length=100, blank=True, null=True)
    horarioparaatendimento = models.CharField(max_length=50, blank=True, null=True)
    tipopessoa = models.IntegerField(blank=True, null=True)
    classificacao = models.IntegerField()
    tipopgto = models.IntegerField(blank=True, null=True)
    numero = models.IntegerField()
    numerocobranca = models.IntegerField()
    observacoes = models.TextField(blank=True, null=True)
    igualresidencia = models.CharField(max_length=1, blank=True, null=True)
    aceita_emails = models.CharField(max_length=1, blank=True, null=True)
    foto = models.BinaryField(blank=True, null=True)
    atualizado_sac = models.DateField(blank=True, null=True)
    id_alternativo = models.IntegerField(blank=True, null=True)
    usar_id_alternativo = models.CharField(max_length=1, blank=True, null=True)
    tmp_aniversariante = models.CharField(max_length=1, blank=True, null=True)
    nome_exibicao_chat = models.CharField(max_length=30, blank=True, null=True)
    passwd_chat = models.CharField(max_length=30, blank=True, null=True)
    mensagem_exibicao_chat = models.CharField(max_length=100, blank=True, null=True)
    senha_email = models.CharField(max_length=50, blank=True, null=True)
    inativo = models.CharField(max_length=1, blank=True, null=True)
    motivo_inatividade = models.ForeignKey('MkPessoasInatividade', models.DO_NOTHING, db_column='motivo_inatividade', blank=True, null=True)
    plano_padrao = models.IntegerField(blank=True, null=True)
    dia_vencimento = models.IntegerField(blank=True, null=True)
    profile_padrao = models.IntegerField(blank=True, null=True)
    mensagem_nf = models.CharField(max_length=200, blank=True, null=True)
    tmp_sem_boleto_gerado = models.CharField(max_length=1, blank=True, null=True)
    dt_inatividade = models.DateField(blank=True, null=True)
    observacoes2 = models.TextField(blank=True, null=True)
    com_conexao = models.CharField(max_length=1, blank=True, null=True)
    retorno_serasa = models.TextField(blank=True, null=True)
    mensgem_nf2 = models.TextField(blank=True, null=True)
    autorizado_abrir_suporte = models.CharField(max_length=100, blank=True, null=True)
    autorizado_abrir_suporte_cpf = models.CharField(max_length=20, blank=True, null=True)
    cfop = models.CharField(max_length=4, blank=True, null=True)
    condominio = models.IntegerField(blank=True, null=True)
    user_sac = models.CharField(max_length=100, blank=True, null=True)
    pass_sac = models.CharField(max_length=30, blank=True, null=True)
    acesso_sac = models.CharField(max_length=1, blank=True, null=True)
    mensagem_para_cliente = models.TextField(blank=True, null=True)
    dt_max_mensagem_cliente = models.DateField(blank=True, null=True)
    cd_revenda = models.IntegerField(blank=True, null=True)
    natureza_juridica = models.IntegerField(blank=True, null=True)
    controle_assinante = models.IntegerField(blank=True, null=True)
    cd_pessoa_externo = models.IntegerField(unique=True, blank=True, null=True)
    im = models.CharField(max_length=20, blank=True, null=True)
    grupo_atendimento = models.ForeignKey('MkPessoasGrupos', models.DO_NOTHING, db_column='grupo_atendimento', blank=True, null=True)
    operadora_fone = models.CharField(max_length=50, blank=True, null=True)
    whatsapp = models.CharField(max_length=1, blank=True, null=True)
    nome_fantasia = models.CharField(max_length=100, blank=True, null=True)
    token_gcm = models.CharField(max_length=200, blank=True, null=True)
    token_sac = models.CharField(max_length=32, blank=True, null=True)
    login_sac_hotspot = models.CharField(max_length=1, blank=True, null=True)
    cd_agente_cobranca = models.IntegerField(blank=True, null=True)
    login_sac_espn = models.CharField(max_length=1, blank=True, null=True)
    funcionario_terceirizado = models.CharField(max_length=1, blank=True, null=True)
    cd_empresa = models.IntegerField(blank=True, null=True)
    classificacao_tipo_cliente_com = models.CharField(max_length=2, blank=True, null=True)
    sinc_auto_multiempresa = models.CharField(max_length=1, blank=True, null=True)
    id_telegram = models.CharField(max_length=100, blank=True, null=True)
    tx_spc_black_list = models.TextField(blank=True, null=True)
    controle_restricao_cadastro = models.IntegerField(blank=True, null=True)
    guid_controle_insert = models.CharField(max_length=50, blank=True, null=True)
    tipo_assinante = models.IntegerField(blank=True, null=True)
    nivel_validacao_email = models.IntegerField(blank=True, null=True)
    sucesso_valida_email = models.CharField(max_length=1, blank=True, null=True)
    endereco_prestacao_servico = models.CharField(max_length=1, blank=True, null=True)
    latitude = models.CharField(max_length=25, blank=True, null=True)
    longitude = models.CharField(max_length=25, blank=True, null=True)
    sexo = models.IntegerField(blank=True, null=True)
    chat_ignora_ate_auto = models.CharField(max_length=1, blank=True, null=True)
    id_estrangeiro = models.CharField(max_length=50, blank=True, null=True)
    cd_pais = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mk_pessoas'


class MkPessoasEnderecos(models.Model):
    codpessoaend = models.AutoField(primary_key=True)
    cd_mk_pessoas_enderecos_tipo = models.IntegerField(blank=True, null=True)
    descricao = models.CharField(max_length=50)
    cep = models.CharField(max_length=8)
    cdpessoa_mk_pessoas = models.ForeignKey(MkPessoas, models.DO_NOTHING, db_column='cdpessoa_mk_pessoas', blank=True, null=True)
    cdestado_mk_estados = models.IntegerField()
    cdcidade_mk_cidades = models.IntegerField()
    cdbairro_mk_bairros = models.IntegerField()
    cdlogradouro_mk_logradouros = models.IntegerField()
    numero = models.IntegerField()
    complemento = models.CharField(max_length=50, blank=True, null=True)
    cd_empresa = models.IntegerField(blank=True, null=True)
    id_hash_pessoa = models.CharField(max_length=50, blank=True, null=True)
    dt = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mk_pessoas_enderecos'


class MkPessoasGrupos(models.Model):
    nome_grupo = models.CharField(unique=True, max_length=50, blank=True, null=True)
    observacoes = models.TextField(blank=True, null=True)
    codpesgrupo = models.AutoField(primary_key=True)
    prioridade = models.IntegerField(blank=True, null=True)
    grupo_envio_men_atendimento = models.IntegerField(blank=True, null=True)
    processo_sac_ate = models.IntegerField(blank=True, null=True)
    classificacao_sac_ate = models.IntegerField(blank=True, null=True)
    processo_sac_ate_fin = models.IntegerField(blank=True, null=True)
    classificacao_sac_ate_fin = models.IntegerField(blank=True, null=True)
    processo_sac_ate_com = models.IntegerField(blank=True, null=True)
    classificacao_sac_ate_com = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mk_pessoas_grupos'


class MkPessoasInatividade(models.Model):
    codpesinat = models.AutoField(primary_key=True)
    descricao_motivo = models.CharField(max_length=30, blank=True, null=True)
    obs = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mk_pessoas_inatividade'


class MkPlanosAcesso(models.Model):
    codplano = models.AutoField(primary_key=True)
    codservidor = models.ForeignKey('MkServidores', models.DO_NOTHING, db_column='codservidor', blank=True, null=True)
    descricao = models.CharField(max_length=50)
    meses_contrato = models.IntegerField()
    vel_up = models.CharField(max_length=10, blank=True, null=True)
    vel_down = models.CharField(max_length=10, blank=True, null=True)
    brt_thre_up = models.CharField(max_length=10, blank=True, null=True)
    brt_thre_down = models.CharField(max_length=10, blank=True, null=True)
    burst_up = models.CharField(max_length=10, blank=True, null=True)
    burst_down = models.CharField(max_length=10, blank=True, null=True)
    burst_time = models.IntegerField(blank=True, null=True)
    ativar_burst = models.CharField(max_length=1, blank=True, null=True)
    vlr_mensalidade = models.FloatField(blank=True, null=True)
    cir_up = models.CharField(max_length=10, blank=True, null=True)
    cir_down = models.CharField(max_length=10, blank=True, null=True)
    perfil_contrato = models.IntegerField(blank=True, null=True)
    ativar_plano_personalizado = models.CharField(max_length=1, blank=True, null=True)
    ativar_personal = models.CharField(max_length=1, blank=True, null=True)
    ativar_diario = models.CharField(max_length=1, blank=True, null=True)
    ativar_semanal = models.CharField(max_length=1, blank=True, null=True)
    ativar_mensal = models.CharField(max_length=1, blank=True, null=True)
    regra_diaria = models.IntegerField(blank=True, null=True)
    regra_semanal = models.IntegerField(blank=True, null=True)
    regra_mensal = models.IntegerField(blank=True, null=True)
    compor_valor = models.CharField(max_length=1, blank=True, null=True)
    cfop = models.IntegerField(blank=True, null=True)
    tx_icms = models.FloatField(blank=True, null=True)
    tx_fust = models.FloatField(blank=True, null=True)
    tx_funtel = models.FloatField(blank=True, null=True)
    base_calculo_icms = models.FloatField(blank=True, null=True)
    valor_base = models.FloatField(blank=True, null=True)
    descricao_nf = models.CharField(max_length=50, blank=True, null=True)
    plano_livre_servidor = models.CharField(max_length=1, blank=True, null=True)
    outro_planos = models.CharField(max_length=1, blank=True, null=True)
    aplicacao = models.TextField(blank=True, null=True)
    compor_valor_nf_pre = models.CharField(max_length=1, blank=True, null=True)
    descricao_nf_pre = models.CharField(max_length=50, blank=True, null=True)
    cfop_nf_pre = models.IntegerField(blank=True, null=True)
    vlr_nf_pre = models.FloatField(blank=True, null=True)
    aliquota_nf_pre = models.FloatField(blank=True, null=True)
    valor_total_nf = models.FloatField(blank=True, null=True)
    considerar_vlr_conta = models.CharField(max_length=1, blank=True, null=True)
    pis = models.FloatField(blank=True, null=True)
    cofins = models.FloatField(blank=True, null=True)
    iss = models.FloatField(blank=True, null=True)
    pnbl = models.CharField(max_length=1, blank=True, null=True)
    dedicado = models.CharField(max_length=1, blank=True, null=True)
    vlr_velocidade = models.IntegerField(blank=True, null=True)
    vlr_velocidade_garantido = models.IntegerField(blank=True, null=True)
    mes_limite_parcelas = models.IntegerField(blank=True, null=True)
    address_list = models.IntegerField(blank=True, null=True)
    inativo = models.CharField(max_length=1, blank=True, null=True)
    compor_valor_avancado = models.CharField(max_length=1, blank=True, null=True)
    ativa_recibo_numerado = models.CharField(max_length=1, blank=True, null=True)
    fracao_recibo_numerado = models.FloatField(blank=True, null=True)
    descricao_recibo_numerado = models.CharField(max_length=100, blank=True, null=True)
    obs_recibo_numerado = models.TextField(blank=True, null=True)
    tabela_descontos = models.IntegerField(blank=True, null=True)
    prioridade = models.IntegerField(blank=True, null=True)
    str_mt = models.CharField(max_length=50, blank=True, null=True)
    und_fin_sugerida = models.CharField(max_length=30, blank=True, null=True)
    ncm = models.CharField(max_length=20, blank=True, null=True)
    filter_id = models.CharField(max_length=200, blank=True, null=True)
    ingress_policy_ipv6 = models.CharField(max_length=100, blank=True, null=True)
    egress_policy_ipv6 = models.CharField(max_length=100, blank=True, null=True)
    ingress_policy_ipv4 = models.CharField(max_length=100, blank=True, null=True)
    egress_policy_ipv4 = models.CharField(max_length=100, blank=True, null=True)
    voip_empresa = models.IntegerField(blank=True, null=True)
    tx_up_red_velocidade = models.IntegerField(blank=True, null=True)
    tx_down_red_velocidade = models.IntegerField(blank=True, null=True)
    tx_up_red_velocidade_med = models.CharField(max_length=5, blank=True, null=True)
    tx_down_red_velocidade_med = models.CharField(max_length=5, blank=True, null=True)
    def_bloq_cnt = models.IntegerField(blank=True, null=True)
    def_bloq_red_vel = models.IntegerField(blank=True, null=True)
    def_dias_bloq = models.IntegerField(blank=True, null=True)
    def_ips = models.IntegerField(blank=True, null=True)
    def_grupo = models.IntegerField(blank=True, null=True)
    def_subgrupo = models.IntegerField(blank=True, null=True)
    def_und_fin = models.CharField(max_length=30, blank=True, null=True)
    def_modelo_nf = models.IntegerField(blank=True, null=True)
    def_desconto = models.IntegerField(blank=True, null=True)
    tipo = models.IntegerField(blank=True, null=True)
    cd_batch = models.IntegerField(blank=True, null=True)
    vlr_velocidade_up = models.IntegerField(blank=True, null=True)
    cd_plano_iptv = models.IntegerField(blank=True, null=True)
    rate_id = models.IntegerField(blank=True, null=True)
    telefonia_blq_a_cobrar = models.IntegerField(blank=True, null=True)
    telefonia_ldn = models.IntegerField(blank=True, null=True)
    telefonia_ldi = models.IntegerField(blank=True, null=True)
    telefonia_vc1 = models.IntegerField(blank=True, null=True)
    composicao_plano_vlr = models.CharField(max_length=1, blank=True, null=True)
    grupo = models.IntegerField(blank=True, null=True)
    limite = models.IntegerField(blank=True, null=True)
    habilitar_mk_hotspot = models.CharField(max_length=1, blank=True, null=True)
    cd_empresa = models.IntegerField(blank=True, null=True)
    cd_telefonia_plataforma = models.IntegerField(blank=True, null=True)
    str_velocidade_cmts = models.CharField(max_length=30, blank=True, null=True)
    ingress_policy_ipv6_reducao = models.CharField(max_length=100, blank=True, null=True)
    ingress_policy_ipv4_reducao = models.CharField(max_length=100, blank=True, null=True)
    egress_policy_ipv4_reducao = models.CharField(max_length=100, blank=True, null=True)
    egress_policy_ipv6_reducao = models.CharField(max_length=100, blank=True, null=True)
    cd_regua_configuracao = models.ForeignKey('MkReguaTipo', models.DO_NOTHING, db_column='cd_regua_configuracao', blank=True, null=True)
    tv_operadora = models.CharField(max_length=20, blank=True, null=True)
    tv_codigo_oferta = models.CharField(max_length=20, blank=True, null=True)
    status_teste_plano = models.IntegerField(blank=True, null=True)
    cd_group_reply = models.ForeignKey(MkAtribRadiusGroupReply, models.DO_NOTHING, db_column='cd_group_reply', blank=True, null=True)
    velocidades_formatadas = models.CharField(max_length=100, blank=True, null=True)
    in_cisco_v4 = models.CharField(max_length=100, blank=True, null=True)
    in_cisco_v4_r = models.CharField(max_length=100, blank=True, null=True)
    e_cisco_v4 = models.CharField(max_length=100, blank=True, null=True)
    e_cisco_v4_r = models.CharField(max_length=100, blank=True, null=True)
    in_cisco_v6 = models.CharField(max_length=100, blank=True, null=True)
    in_cisco_v6_r = models.CharField(max_length=100, blank=True, null=True)
    e_cisco_v6 = models.CharField(max_length=100, blank=True, null=True)
    e_cisco_v6_r = models.CharField(max_length=100, blank=True, null=True)
    in_huawei_v4 = models.CharField(max_length=100, blank=True, null=True)
    in_huawei_v4_r = models.CharField(max_length=100, blank=True, null=True)
    e_huawei_v4 = models.CharField(max_length=100, blank=True, null=True)
    e_huawei_v4_r = models.CharField(max_length=100, blank=True, null=True)
    in_huawei_v6 = models.CharField(max_length=100, blank=True, null=True)
    in_huawei_v6_r = models.CharField(max_length=100, blank=True, null=True)
    e_huawei_v6 = models.CharField(max_length=100, blank=True, null=True)
    e_huawei_v6_r = models.CharField(max_length=100, blank=True, null=True)
    in_ipoe_v4 = models.CharField(max_length=150, blank=True, null=True)
    in_ipoe_v4_r = models.CharField(max_length=150, blank=True, null=True)
    e_ipoe_v4 = models.CharField(max_length=150, blank=True, null=True)
    e_ipoe_v4_r = models.CharField(max_length=150, blank=True, null=True)
    in_ipoe_v6 = models.CharField(max_length=150, blank=True, null=True)
    in_ipoe_v6_r = models.CharField(max_length=150, blank=True, null=True)
    e_ipoe_v6 = models.CharField(max_length=150, blank=True, null=True)
    e_ipoe_v6_r = models.CharField(max_length=150, blank=True, null=True)
    velocidades_formatadas_r = models.CharField(max_length=70, blank=True, null=True)
    exclusivo_compo_crm = models.CharField(max_length=1, blank=True, null=True)
    guid_tmp = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mk_planos_acesso'


class MkPontoAcessoTipo(models.Model):
    cod_pop_tipo = models.AutoField(primary_key=True)
    nome_tipo = models.CharField(max_length=86)
    tecnologia = models.CharField(max_length=1, blank=True, null=True)
    abriga_servidor = models.CharField(max_length=1, blank=True, null=True)
    polarizacao = models.CharField(max_length=1, blank=True, null=True)
    banda = models.CharField(max_length=6, blank=True, null=True)
    frequencia = models.ForeignKey(MkFrequencias, models.DO_NOTHING, db_column='frequencia', blank=True, null=True)
    tamanho_canal = models.CharField(max_length=2, blank=True, null=True)
    outras_caracteristicas = models.TextField(blank=True, null=True)
    valor_estimado = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    indice_perda = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mk_ponto_acesso_tipo'


class MkPontosAcesso(models.Model):
    codpontoacesso = models.AutoField(primary_key=True)
    ssid = models.CharField(max_length=50)
    localizacao = models.CharField(max_length=50, blank=True, null=True)
    sistema_operacional = models.IntegerField()
    software_id = models.CharField(max_length=20, blank=True, null=True)
    bloqueia_mac = models.CharField(max_length=1, blank=True, null=True)
    mac_passagem = models.CharField(max_length=20, blank=True, null=True)
    funcao = models.IntegerField(blank=True, null=True)
    remoto_user = models.CharField(max_length=20, blank=True, null=True)
    remoto_password = models.CharField(max_length=50, blank=True, null=True)
    remoto_porta_ftp = models.CharField(max_length=5, blank=True, null=True)
    nas_address = models.CharField(max_length=15, blank=True, null=True)
    remoto_ip_address = models.CharField(unique=True, max_length=20, blank=True, null=True)
    integra_info = models.CharField(max_length=1, blank=True, null=True)
    regra_plantao = models.IntegerField(blank=True, null=True)
    integra_conectividade = models.CharField(max_length=1, blank=True, null=True)
    integra_neighboards = models.CharField(max_length=1, blank=True, null=True)
    remoto_porta_ssh = models.CharField(max_length=5, blank=True, null=True)
    remoto_user_ssh = models.CharField(max_length=50, blank=True, null=True)
    habilita_ssh = models.CharField(max_length=1, blank=True, null=True)
    ack_aceito = models.IntegerField(blank=True, null=True)
    ack_bom = models.IntegerField(blank=True, null=True)
    sinal_aceito = models.IntegerField(blank=True, null=True)
    sinal_bom = models.IntegerField(blank=True, null=True)
    responde_pelo_servidor = models.CharField(max_length=1, blank=True, null=True)
    integra_active = models.CharField(max_length=1, blank=True, null=True)
    nas_port_id = models.CharField(max_length=50, blank=True, null=True)
    bkp_auto = models.CharField(max_length=1, blank=True, null=True)
    longitude = models.CharField(max_length=30, blank=True, null=True)
    latitude = models.CharField(max_length=30, blank=True, null=True)
    endereco = models.CharField(max_length=100, blank=True, null=True)
    cidade = models.CharField(max_length=50, blank=True, null=True)
    estado = models.CharField(max_length=2, blank=True, null=True)
    porta_api = models.IntegerField(blank=True, null=True)
    mkbox_considerar_nas = models.CharField(max_length=1, blank=True, null=True)
    limite_conexoes = models.IntegerField(blank=True, null=True)
    tipo_aviso_limite = models.CharField(max_length=1, blank=True, null=True)
    obter_info_trafego = models.CharField(max_length=1, blank=True, null=True)
    servidor_indicado = models.IntegerField(blank=True, null=True)
    obrigar_servidor = models.CharField(max_length=1, blank=True, null=True)
    tecnologia = models.CharField(max_length=1, blank=True, null=True)
    inativo = models.CharField(max_length=1, blank=True, null=True)
    bairro = models.CharField(max_length=40, blank=True, null=True)
    cep = models.CharField(max_length=8, blank=True, null=True)
    polarizacao = models.CharField(max_length=1, blank=True, null=True)
    banda = models.CharField(max_length=10, blank=True, null=True)
    frequencia = models.IntegerField(blank=True, null=True)
    tamanho_canal = models.IntegerField(blank=True, null=True)
    descritivo_abrangência = models.TextField(blank=True, null=True)
    descritivo_equipamentos = models.TextField(blank=True, null=True)
    comportamento_rest_ruas = models.CharField(max_length=1, blank=True, null=True)
    prioridade = models.IntegerField(blank=True, null=True)
    api_status = models.CharField(max_length=30, blank=True, null=True)
    api_status_user = models.CharField(max_length=30, blank=True, null=True)
    api_status_dt = models.DateField(blank=True, null=True)
    api_status_ok = models.CharField(max_length=1, blank=True, null=True)
    mt_identify = models.CharField(max_length=50, blank=True, null=True)
    api_status_aux = models.TextField(blank=True, null=True)
    api_status_hr = models.CharField(max_length=10, blank=True, null=True)
    ssh_status_ok = models.CharField(max_length=1, blank=True, null=True)
    ssh_user_test = models.CharField(max_length=30, blank=True, null=True)
    ssh_porta_test = models.IntegerField(blank=True, null=True)
    ssh_dt_test = models.DateField(blank=True, null=True)
    ssh_hr_test = models.CharField(max_length=10, blank=True, null=True)
    ssh_status = models.CharField(max_length=30, blank=True, null=True)
    indicar_nas_auth_login = models.CharField(max_length=1, blank=True, null=True)
    nas_add_auth_login = models.CharField(max_length=50, blank=True, null=True)
    nas_port_auth_login = models.CharField(max_length=50, blank=True, null=True)
    cd_armario = models.ForeignKey(MkFiberArmarios, models.DO_NOTHING, db_column='cd_armario', blank=True, null=True)
    projeto = models.CharField(max_length=1, blank=True, null=True)
    cd_pop_tipo = models.ForeignKey(MkPontoAcessoTipo, models.DO_NOTHING, db_column='cd_pop_tipo', blank=True, null=True)
    cd_projeto = models.ForeignKey(MkFiberProjeto, models.DO_NOTHING, db_column='cd_projeto', blank=True, null=True)
    snmp_porta = models.IntegerField(blank=True, null=True)
    snmp_comunidade = models.CharField(max_length=20, blank=True, null=True)
    monitora_cpu = models.CharField(max_length=1, blank=True, null=True)
    monitora_interface = models.CharField(max_length=1, blank=True, null=True)
    monitora_memoria = models.CharField(max_length=1, blank=True, null=True)
    monitora_sinal_onu = models.CharField(max_length=1, blank=True, null=True)
    snmp_tst_porta = models.IntegerField(blank=True, null=True)
    snmp_tst_user = models.CharField(max_length=17, blank=True, null=True)
    snmp_tst_status = models.CharField(max_length=17, blank=True, null=True)
    snmp_tst_data = models.DateField(blank=True, null=True)
    snmp_tst_hora = models.CharField(max_length=8, blank=True, null=True)
    monitora_queue = models.CharField(max_length=1, blank=True, null=True)
    tipo_ip_sugerido = models.IntegerField(blank=True, null=True)
    pool_sugerido = models.IntegerField(blank=True, null=True)
    ip_address_anm = models.CharField(max_length=64, blank=True, null=True)
    porta_telnet = models.IntegerField(blank=True, null=True)
    cd_empresa = models.IntegerField(blank=True, null=True)
    associacao = models.IntegerField()
    cd_pop = models.ForeignKey('MkPopInfo', models.DO_NOTHING, db_column='cd_pop', blank=True, null=True)
    potencia_sinal = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    obs = models.TextField(blank=True, null=True)
    cd_perfil_monitoramento = models.ForeignKey(MkPerfilMonitoramento, models.DO_NOTHING, db_column='cd_perfil_monitoramento', blank=True, null=True)
    snmp_versao = models.CharField(max_length=2, blank=True, null=True)
    cd_poste = models.ForeignKey(MkFiberPostes, models.DO_NOTHING, db_column='cd_poste', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mk_pontos_acesso'


class MkPopInfo(models.Model):
    codpopinfo = models.AutoField(primary_key=True)
    nome_pop = models.CharField(max_length=50, blank=True, null=True)
    endereco_localizacao = models.IntegerField(blank=True, null=True)
    bairro_localizacao = models.IntegerField(blank=True, null=True)
    cidade_localizacao = models.IntegerField(blank=True, null=True)
    estado_localizacao = models.IntegerField(blank=True, null=True)
    cep_localizacao = models.CharField(max_length=8, blank=True, null=True)
    latitude = models.CharField(max_length=20, blank=True, null=True)
    longitude = models.CharField(max_length=20, blank=True, null=True)
    altitude = models.FloatField(blank=True, null=True)
    dicas_localizacao = models.TextField(blank=True, null=True)
    nome_proprietario = models.CharField(max_length=100, blank=True, null=True)
    endereco_proprietario = models.IntegerField(blank=True, null=True)
    cidade_proprietario = models.IntegerField(blank=True, null=True)
    estado_proprietario = models.IntegerField(blank=True, null=True)
    bairro_proprietario = models.IntegerField(blank=True, null=True)
    cep_proprietario = models.IntegerField(blank=True, null=True)
    numero_localizacao = models.CharField(max_length=15, blank=True, null=True)
    numero_proprietario = models.CharField(max_length=15, blank=True, null=True)
    fone1 = models.CharField(max_length=20, blank=True, null=True)
    fone2 = models.CharField(max_length=20, blank=True, null=True)
    fone3 = models.CharField(max_length=20, blank=True, null=True)
    cpf = models.CharField(max_length=20, blank=True, null=True)
    rg = models.CharField(max_length=20, blank=True, null=True)
    valor_aluguel = models.FloatField(blank=True, null=True)
    info_bancarias = models.TextField(blank=True, null=True)
    info_espaco = models.TextField(blank=True, null=True)
    procedimentos_energia = models.TextField(blank=True, null=True)
    nome_titular_conta = models.CharField(max_length=100, blank=True, null=True)
    numero_cliente = models.CharField(max_length=20, blank=True, null=True)
    contato_concessionaria = models.CharField(max_length=20, blank=True, null=True)
    data_contratacao = models.DateField(blank=True, null=True)
    int_imagem = models.CharField(max_length=5, blank=True, null=True)
    cd_poste = models.ForeignKey(MkFiberPostes, models.DO_NOTHING, db_column='cd_poste', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mk_pop_info'


class MkProfilePgto(models.Model):
    codprofile = models.AutoField(primary_key=True)
    nome_profile = models.CharField(max_length=50)
    forma_pgto = models.IntegerField(blank=True, null=True)
    codigo_cedente = models.CharField(max_length=15, blank=True, null=True)
    agencia = models.CharField(max_length=10, blank=True, null=True)
    conta_corrente = models.CharField(max_length=20, blank=True, null=True)
    instrucoes_boleto = models.TextField(blank=True, null=True)
    valor_boleto = models.FloatField(blank=True, null=True)
    posto = models.CharField(max_length=2, blank=True, null=True)
    banco = models.CharField(max_length=3, blank=True, null=True)
    ano = models.CharField(max_length=2, blank=True, null=True)
    sequencial = models.IntegerField(blank=True, null=True)
    entidade = models.IntegerField(blank=True, null=True)
    nome_cedente = models.CharField(max_length=100, blank=True, null=True)
    doc_cedente = models.CharField(max_length=30, blank=True, null=True)
    liberacao_automatica = models.CharField(max_length=1, blank=True, null=True)
    msg_linha1 = models.CharField(max_length=200, blank=True, null=True)
    msg_linha2 = models.CharField(max_length=200, blank=True, null=True)
    msg_linha3 = models.CharField(max_length=200, blank=True, null=True)
    msg_linha4 = models.CharField(max_length=200, blank=True, null=True)
    msg_linha5 = models.CharField(max_length=200, blank=True, null=True)
    msg_linha6 = models.CharField(max_length=200, blank=True, null=True)
    msg_linha7 = models.CharField(max_length=200, blank=True, null=True)
    msg_linha8 = models.CharField(max_length=200, blank=True, null=True)
    tx_aux1 = models.CharField(max_length=200, blank=True, null=True)
    tx_aux2 = models.CharField(max_length=200, blank=True, null=True)
    tx_aux3 = models.CharField(max_length=200, blank=True, null=True)
    tx_aux4 = models.CharField(max_length=200, blank=True, null=True)
    tx_aux5 = models.CharField(max_length=200, blank=True, null=True)
    tx_aux6 = models.CharField(max_length=200, blank=True, null=True)
    tx_aux7 = models.CharField(max_length=200, blank=True, null=True)
    local_pgto = models.CharField(max_length=200, blank=True, null=True)
    aceite = models.CharField(max_length=10, blank=True, null=True)
    carteira = models.CharField(max_length=10, blank=True, null=True)
    cedente_barra = models.CharField(max_length=100, blank=True, null=True)
    modalidade = models.CharField(max_length=30, blank=True, null=True)
    num_convenio = models.CharField(max_length=30, blank=True, null=True)
    url_jsp = models.CharField(max_length=200, blank=True, null=True)
    empresa = models.IntegerField(blank=True, null=True)
    seq_remessa = models.IntegerField(blank=True, null=True)
    dv_conta = models.CharField(max_length=2, blank=True, null=True)
    ativar_sms = models.CharField(max_length=1, blank=True, null=True)
    ativar_email = models.CharField(max_length=1, blank=True, null=True)
    tx_sms = models.TextField(blank=True, null=True)
    tx_email = models.TextField(blank=True, null=True)
    smtp = models.CharField(max_length=100, blank=True, null=True)
    login_smtp = models.CharField(max_length=100, blank=True, null=True)
    password_smtp = models.CharField(max_length=30, blank=True, null=True)
    email_autenticao = models.CharField(max_length=100, blank=True, null=True)
    nome_do_banco = models.CharField(max_length=30, blank=True, null=True)
    ret_remove_dv = models.CharField(max_length=1, blank=True, null=True)
    dias_reagendamento = models.IntegerField(blank=True, null=True)
    regra_formatacao = models.IntegerField(blank=True, null=True)
    tipo_cobranca = models.CharField(max_length=1, blank=True, null=True)
    postar_titulo = models.CharField(max_length=1, blank=True, null=True)
    percentual_multa_atraso = models.CharField(max_length=5, blank=True, null=True)
    especie = models.CharField(max_length=2, blank=True, null=True)
    dias_para_protesto = models.IntegerField(blank=True, null=True)
    percentual_juros_dia = models.CharField(max_length=5, blank=True, null=True)
    percentual_desconto_antecipacao = models.CharField(max_length=5, blank=True, null=True)
    protestar = models.CharField(max_length=2, blank=True, null=True)
    controle_ano = models.IntegerField(blank=True, null=True)
    aux_tipo_layout = models.IntegerField(blank=True, null=True)
    agencia_dv = models.CharField(max_length=2, blank=True, null=True)
    cd_operacao = models.CharField(max_length=10, blank=True, null=True)
    local_pgto2 = models.CharField(max_length=200, blank=True, null=True)
    cd_fornecido_agencia = models.CharField(max_length=30, blank=True, null=True)
    cd_fornecido_agencia_dv = models.CharField(max_length=2, blank=True, null=True)
    modelo_impressao = models.CharField(max_length=5, blank=True, null=True)
    link_imagem = models.CharField(max_length=200, blank=True, null=True)
    mensagens_cabecalho = models.TextField(blank=True, null=True)
    sigcb = models.CharField(max_length=1, blank=True, null=True)
    img_cabecalho = models.BinaryField(blank=True, null=True)
    layout_retorno = models.IntegerField(blank=True, null=True)
    layout_remessa = models.IntegerField(blank=True, null=True)
    aux_frente_preencher_recibo = models.CharField(max_length=1, blank=True, null=True)
    aux_frente_linha7 = models.CharField(max_length=250, blank=True, null=True)
    aux_frente_linha8 = models.CharField(max_length=250, blank=True, null=True)
    aux_frente_linha9 = models.CharField(max_length=250, blank=True, null=True)
    gerar_nosso_num = models.CharField(max_length=1, blank=True, null=True)
    quebrar_pagina = models.CharField(max_length=10, blank=True, null=True)
    cc_alternativa = models.CharField(max_length=15, blank=True, null=True)
    rem_gerar_carne = models.CharField(max_length=1, blank=True, null=True)
    beta = models.CharField(max_length=1, blank=True, null=True)
    imp_nosso_num_ret_banco = models.CharField(max_length=1, blank=True, null=True)
    operacao_conta = models.IntegerField(blank=True, null=True)
    margem_superior = models.FloatField(blank=True, null=True)
    lyt_personalizado = models.IntegerField(blank=True, null=True)
    apelido = models.CharField(max_length=30, blank=True, null=True)
    nomen_liquidacao = models.CharField(max_length=30, blank=True, null=True)
    comportamento_tarifa = models.CharField(max_length=1, blank=True, null=True)
    comportamento_acresimos = models.CharField(max_length=1, blank=True, null=True)
    comportamento_descontos = models.CharField(max_length=1, blank=True, null=True)
    comportamento_a_menos = models.CharField(max_length=1, blank=True, null=True)
    nomen_acrescimos = models.CharField(max_length=30, blank=True, null=True)
    nomen_descontos = models.CharField(max_length=30, blank=True, null=True)
    nomen_tarifas = models.CharField(max_length=30, blank=True, null=True)
    aviso_liquida_a_menos = models.CharField(max_length=1, blank=True, null=True)
    flags = models.CharField(max_length=200, blank=True, null=True)
    cd_peculiaridade = models.IntegerField(blank=True, null=True)
    observacoes = models.TextField(blank=True, null=True)
    homologado = models.CharField(max_length=1, blank=True, null=True)
    dv_cedente = models.CharField(max_length=3, blank=True, null=True)
    flags_2 = models.CharField(max_length=50, blank=True, null=True)
    cd_flash = models.CharField(max_length=10, blank=True, null=True)
    cd_unificacao_profile = models.IntegerField(blank=True, null=True)
    nomen_scm = models.CharField(max_length=30, blank=True, null=True)
    nomen_sva = models.CharField(max_length=30, blank=True, null=True)
    praca_devolucao = models.CharField(max_length=50, blank=True, null=True)
    ocultar_doc = models.CharField(max_length=1, blank=True, null=True)
    tipo_impressao = models.CharField(max_length=1, blank=True, null=True)
    profile_cons_ent_confirmada = models.IntegerField(blank=True, null=True)
    cd_modelo_impressao = models.IntegerField(blank=True, null=True)
    febraban_segmento = models.CharField(max_length=1, blank=True, null=True)
    febraban_identificacao = models.CharField(max_length=20, blank=True, null=True)
    modelo_impressao_envio = models.IntegerField(blank=True, null=True)
    desativar_profile = models.CharField(max_length=1, blank=True, null=True)
    cd_empresa = models.IntegerField(blank=True, null=True)
    aceita_baixa_alteracao = models.CharField(max_length=1, blank=True, null=True)
    aceita_alteracao = models.CharField(max_length=1, blank=True, null=True)
    febraban_formato_venc = models.CharField(max_length=8, blank=True, null=True)
    status_profile = models.IntegerField(blank=True, null=True)
    beneficiario_nome = models.CharField(max_length=100, blank=True, null=True)
    beneficiario_documento = models.CharField(max_length=30, blank=True, null=True)
    beneficiario_logradouro = models.CharField(max_length=70, blank=True, null=True)
    beneficiario_bairro = models.CharField(max_length=50, blank=True, null=True)
    beneficiario_cep = models.CharField(max_length=15, blank=True, null=True)
    beneficiario_uf = models.CharField(max_length=2, blank=True, null=True)
    beneficiario_municipio = models.CharField(max_length=50, blank=True, null=True)
    beneficiario_email = models.CharField(max_length=70, blank=True, null=True)
    beneficiario_cod_cliente = models.CharField(max_length=10, blank=True, null=True)
    beneficiario_telefone = models.CharField(max_length=20, blank=True, null=True)
    l2_agencia_numero = models.CharField(max_length=10, blank=True, null=True)
    l2_agencia_dv = models.CharField(max_length=2, blank=True, null=True)
    l2_conta_corrente_numero = models.CharField(max_length=15, blank=True, null=True)
    l2_conta_corrente_dv = models.CharField(max_length=2, blank=True, null=True)
    l2_carteira = models.CharField(max_length=3, blank=True, null=True)
    l2_carteira_modalidade = models.CharField(max_length=30, blank=True, null=True)
    l2_carteira_tipo = models.CharField(max_length=20, blank=True, null=True)
    l2_carteira_convenio = models.CharField(max_length=20, blank=True, null=True)
    l2_carteira_convenio_dv = models.CharField(max_length=2, blank=True, null=True)
    l2_ios = models.CharField(max_length=10, blank=True, null=True)
    l2_modelo_default = models.CharField(max_length=2, blank=True, null=True)
    l2_modelo_sac = models.CharField(max_length=2, blank=True, null=True)
    l2_convenio_numero = models.CharField(max_length=10, blank=True, null=True)
    l2_multa_atraso = models.FloatField(blank=True, null=True)
    l2_acrescimos_diario = models.FloatField(blank=True, null=True)
    l2_layout_remessa = models.IntegerField(blank=True, null=True)
    gateway_id = models.CharField(max_length=100, blank=True, null=True)
    gateway_secret = models.CharField(max_length=100, blank=True, null=True)
    gerencianet_sandbox = models.CharField(max_length=5, blank=True, null=True)
    url_notificacoes_gw = models.CharField(max_length=100, blank=True, null=True)
    gw_producao = models.CharField(max_length=10, blank=True, null=True)
    gw_dias_frente_monitoramento = models.IntegerField(blank=True, null=True)
    gw_dias_atras_monitoramento = models.IntegerField(blank=True, null=True)
    gw_tempo_renova_token = models.IntegerField(blank=True, null=True)
    l2_codigo_cedente = models.CharField(max_length=30, blank=True, null=True)
    cartao_loja_numero = models.CharField(max_length=200, blank=True, null=True)
    cartao_loja_chave = models.CharField(max_length=200, blank=True, null=True)
    cartao_padrao = models.CharField(max_length=1, blank=True, null=True)
    cartao_producao = models.CharField(max_length=5, blank=True, null=True)
    l2_controle_impressao = models.CharField(max_length=1, blank=True, null=True)
    ordem_pgto_ativa = models.CharField(max_length=1, blank=True, null=True)
    cd_layout_ordem_pgto = models.IntegerField(blank=True, null=True)
    path_logo = models.CharField(max_length=50, blank=True, null=True)
    cartao_hab_testes_homologacao = models.CharField(max_length=1, blank=True, null=True)
    l2_posto = models.CharField(max_length=2, blank=True, null=True)
    cd_pessoa_cartao_homologa = models.IntegerField(blank=True, null=True)
    num_banco_extra = models.CharField(max_length=3, blank=True, null=True)
    cooperativa = models.CharField(max_length=10, blank=True, null=True)
    ignorar_nosso_numero_dv = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mk_profile_pgto'


class MkProfilesAutenticacao(models.Model):
    codprofile = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=50)
    user_password = models.CharField(max_length=1, blank=True, null=True)
    controle_banda = models.CharField(max_length=1, blank=True, null=True)
    autenticacao_wireless = models.CharField(max_length=1, blank=True, null=True)
    ip_mac = models.CharField(max_length=1, blank=True, null=True)
    pagina_inicial = models.CharField(max_length=1, blank=True, null=True)
    advertise_url = models.CharField(max_length=1, blank=True, null=True)
    metodo_bloqueio = models.IntegerField(blank=True, null=True)
    nas_address = models.CharField(max_length=1, blank=True, null=True)
    wireless_psk = models.CharField(max_length=1, blank=True, null=True)
    tabela_roteamento = models.CharField(max_length=1, blank=True, null=True)
    banda_mac = models.CharField(max_length=1, blank=True, null=True)
    nas_port_id = models.CharField(max_length=1, blank=True, null=True)
    wireless_comment = models.CharField(max_length=1, blank=True, null=True)
    pppoe_hotspot = models.CharField(max_length=1, blank=True, null=True)
    tempo_acct = models.IntegerField(blank=True, null=True)
    simultaneous_use = models.CharField(max_length=1, blank=True, null=True)
    metodo_dir_inadimplencia = models.CharField(max_length=1, blank=True, null=True)
    primary_dns_ipv4 = models.CharField(max_length=50, blank=True, null=True)
    primary_dns_ipv6 = models.CharField(max_length=50, blank=True, null=True)
    secondary_dns_ipv6 = models.CharField(max_length=50, blank=True, null=True)
    secondary_dns_ipv4 = models.CharField(max_length=50, blank=True, null=True)
    pool_name_bloqueado = models.CharField(max_length=30, blank=True, null=True)
    pool_name_pendencia = models.CharField(max_length=30, blank=True, null=True)
    policy_name_bloqueado = models.CharField(max_length=30, blank=True, null=True)
    policy_name_pendencia = models.CharField(max_length=30, blank=True, null=True)
    pool_name_cancelado = models.CharField(max_length=30, blank=True, null=True)
    policy_name_cancelado = models.CharField(max_length=30, blank=True, null=True)
    framed_route = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mk_profiles_autenticacao'


class MkReguaTipo(models.Model):
    codreguatipo = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=80)
    tipo = models.CharField(max_length=1)
    tipo_debito = models.IntegerField(blank=True, null=True)
    hrs_bloqueio = models.IntegerField(blank=True, null=True)
    hrs_mensagem = models.IntegerField(blank=True, null=True)
    padrao = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mk_regua_tipo'


class MkRevendas(models.Model):
    codrevenda = models.AutoField(primary_key=True)
    nome_revenda = models.CharField(max_length=50, blank=True, null=True)
    responsavel = models.CharField(max_length=70, blank=True, null=True)
    fone_celular = models.CharField(max_length=20, blank=True, null=True)
    fone_01 = models.CharField(max_length=20, blank=True, null=True)
    fone_02 = models.CharField(max_length=20, blank=True, null=True)
    email_operacional = models.CharField(max_length=500, blank=True, null=True)
    email_financeiro = models.CharField(max_length=200, blank=True, null=True)
    email_administrativo = models.CharField(max_length=200, blank=True, null=True)
    uf = models.IntegerField(blank=True, null=True)
    cidade = models.IntegerField(blank=True, null=True)
    bairro = models.IntegerField(blank=True, null=True)
    logradouro = models.IntegerField(blank=True, null=True)
    num = models.CharField(max_length=20, blank=True, null=True)
    complemento = models.CharField(max_length=30, blank=True, null=True)
    site = models.CharField(max_length=50, blank=True, null=True)
    regra_comissao_sugerida = models.IntegerField(blank=True, null=True)
    descritivo_abrangencia = models.TextField(blank=True, null=True)
    cnpj = models.CharField(max_length=20, blank=True, null=True)
    cep = models.CharField(max_length=8, blank=True, null=True)
    ponto_recebimento = models.IntegerField(blank=True, null=True)
    ie = models.CharField(max_length=30, blank=True, null=True)
    coringa_extra_01 = models.CharField(max_length=200, blank=True, null=True)
    coringa_extra_02 = models.CharField(max_length=200, blank=True, null=True)
    coringa_extra_03 = models.CharField(max_length=200, blank=True, null=True)
    coringa_extra_04 = models.CharField(max_length=200, blank=True, null=True)
    coringa_extra_05 = models.CharField(max_length=200, blank=True, null=True)
    usar_info_para_contratos = models.CharField(max_length=1, blank=True, null=True)
    tmp_mensagem1 = models.CharField(max_length=300, blank=True, null=True)
    tmp_mensagem2 = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mk_revendas'


class MkServidores(models.Model):
    codmovimento = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=50)
    sistemaoperacional = models.IntegerField()
    localizacao = models.CharField(max_length=50, blank=True, null=True)
    codprofile = models.ForeignKey(MkProfilesAutenticacao, models.DO_NOTHING, db_column='codprofile')
    software_id = models.CharField(max_length=20, blank=True, null=True)
    ip_comunicacao = models.CharField(max_length=15)
    acesso_user = models.CharField(max_length=30, blank=True, null=True)
    acesso_password = models.CharField(max_length=50, blank=True, null=True)
    porta_ftp = models.CharField(max_length=5, blank=True, null=True)
    habilita_rd01 = models.CharField(max_length=1, blank=True, null=True)
    habilita_rd02 = models.CharField(max_length=1, blank=True, null=True)
    integra_radius_local = models.CharField(max_length=1, blank=True, null=True)
    nas_address = models.CharField(max_length=15, blank=True, null=True)
    radius01 = models.IntegerField(blank=True, null=True)
    radius02 = models.IntegerField(blank=True, null=True)
    integra_info = models.CharField(max_length=1, blank=True, null=True)
    regra_plantao = models.IntegerField(blank=True, null=True)
    integra_active = models.CharField(max_length=1, blank=True, null=True)
    integra_neighboards = models.CharField(max_length=1, blank=True, null=True)
    remoto_porta_ssh = models.CharField(max_length=5, blank=True, null=True)
    remoto_user_ssh = models.CharField(max_length=50, blank=True, null=True)
    habilita_ssh = models.CharField(max_length=1, blank=True, null=True)
    bkp_auto = models.CharField(max_length=1, blank=True, null=True)
    porta_api = models.IntegerField(blank=True, null=True)
    tempo_conexao = models.FloatField(blank=True, null=True)
    obter_info_trafego = models.CharField(max_length=1, blank=True, null=True)
    api_status = models.CharField(max_length=30, blank=True, null=True)
    api_status_user = models.CharField(max_length=30, blank=True, null=True)
    api_status_dt = models.DateField(blank=True, null=True)
    api_status_ok = models.CharField(max_length=1, blank=True, null=True)
    mt_identify = models.CharField(max_length=50, blank=True, null=True)
    api_status_aux = models.TextField(blank=True, null=True)
    api_status_hr = models.CharField(max_length=10, blank=True, null=True)
    ssh_status_ok = models.CharField(max_length=1, blank=True, null=True)
    ssh_user_test = models.CharField(max_length=30, blank=True, null=True)
    ssh_porta_test = models.IntegerField(blank=True, null=True)
    ssh_dt_test = models.DateField(blank=True, null=True)
    ssh_hr_test = models.CharField(max_length=10, blank=True, null=True)
    ssh_status = models.CharField(max_length=30, blank=True, null=True)
    nas_port_id = models.CharField(max_length=50, blank=True, null=True)
    monitora_cpu = models.CharField(max_length=1, blank=True, null=True)
    monitora_memoria = models.CharField(max_length=1, blank=True, null=True)
    snmp_porta = models.IntegerField(blank=True, null=True)
    snmp_comunidade = models.CharField(max_length=20, blank=True, null=True)
    snmp_tst_hora = models.CharField(max_length=8, blank=True, null=True)
    snmp_tst_data = models.DateField(blank=True, null=True)
    snmp_tst_status = models.CharField(max_length=18, blank=True, null=True)
    snmp_tst_user = models.CharField(max_length=22, blank=True, null=True)
    snmp_tst_porta = models.IntegerField(blank=True, null=True)
    monitora_queue = models.CharField(max_length=1, blank=True, null=True)
    porta_radclient = models.IntegerField(blank=True, null=True)
    cd_cluster = models.IntegerField(blank=True, null=True)
    cd_empresa = models.IntegerField(blank=True, null=True)
    cd_perfil_check_reply = models.ForeignKey(MkAtribRadiusCheckReply, models.DO_NOTHING, db_column='cd_perfil_check_reply', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mk_servidores'


class MkSla(models.Model):
    codsla = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=30, blank=True, null=True)
    tipo_controle = models.IntegerField(blank=True, null=True)
    tempo_duvida = models.IntegerField(blank=True, null=True)
    tempo_preventiva = models.IntegerField(blank=True, null=True)
    tempo_ativacao = models.IntegerField(blank=True, null=True)
    tempo_corretiva = models.IntegerField(blank=True, null=True)
    tempo_emergencial = models.IntegerField(blank=True, null=True)
    tempo_outros = models.IntegerField(blank=True, null=True)
    cd_perfil_hora_util = models.ForeignKey('MkSlaPerfilHorasUteis', models.DO_NOTHING, db_column='cd_perfil_hora_util', blank=True, null=True)
    hr_duvida = models.IntegerField(blank=True, null=True)
    hr_preventiva = models.IntegerField(blank=True, null=True)
    hr_ativacao = models.IntegerField(blank=True, null=True)
    hr_corretiva = models.IntegerField(blank=True, null=True)
    hr_emergencial = models.IntegerField(blank=True, null=True)
    hr_outros = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mk_sla'


class MkSlaPerfilHorasUteis(models.Model):
    codperfilhorautil = models.AutoField(primary_key=True)
    descricao = models.CharField(unique=True, max_length=30, blank=True, null=True)
    seg_inicio = models.CharField(max_length=5, blank=True, null=True)
    seg_inicio_int = models.IntegerField(blank=True, null=True)
    seg_fim = models.CharField(max_length=5, blank=True, null=True)
    seg_fim_int = models.IntegerField(blank=True, null=True)
    ter_inicio = models.CharField(max_length=5, blank=True, null=True)
    ter_inicio_int = models.IntegerField(blank=True, null=True)
    ter_fim = models.CharField(max_length=5, blank=True, null=True)
    ter_fim_int = models.IntegerField(blank=True, null=True)
    qua_inicio = models.CharField(max_length=5, blank=True, null=True)
    qua_inicio_int = models.IntegerField(blank=True, null=True)
    qua_fim = models.CharField(max_length=5, blank=True, null=True)
    qua_fim_int = models.IntegerField(blank=True, null=True)
    qui_inicio = models.CharField(max_length=5, blank=True, null=True)
    qui_inicio_int = models.IntegerField(blank=True, null=True)
    qui_fim = models.CharField(max_length=5, blank=True, null=True)
    qui_fim_int = models.IntegerField(blank=True, null=True)
    sex_inicio = models.CharField(max_length=5, blank=True, null=True)
    sex_inicio_int = models.IntegerField(blank=True, null=True)
    sab_inicio = models.CharField(max_length=5, blank=True, null=True)
    sab_inicio_int = models.IntegerField(blank=True, null=True)
    sab_fim = models.CharField(max_length=5, blank=True, null=True)
    sab_fim_int = models.IntegerField(blank=True, null=True)
    fer_inicio = models.CharField(max_length=5, blank=True, null=True)
    fer_inicio_int = models.IntegerField(blank=True, null=True)
    fer_fim = models.CharField(max_length=5, blank=True, null=True)
    fer_fim_int = models.IntegerField(blank=True, null=True)
    sex_fim = models.CharField(max_length=5, blank=True, null=True)
    sex_fim_int = models.IntegerField(blank=True, null=True)
    dom_inicio = models.CharField(max_length=5, blank=True, null=True)
    dom_inicio_int = models.IntegerField(blank=True, null=True)
    dom_fim = models.CharField(max_length=5, blank=True, null=True)
    dom_fim_int = models.IntegerField(blank=True, null=True)
    seg_total = models.IntegerField(blank=True, null=True)
    ter_total = models.IntegerField(blank=True, null=True)
    qua_total = models.IntegerField(blank=True, null=True)
    qui_total = models.IntegerField(blank=True, null=True)
    sex_total = models.IntegerField(blank=True, null=True)
    sab_total = models.IntegerField(blank=True, null=True)
    dom_total = models.IntegerField(blank=True, null=True)
    fer_total = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mk_sla_perfil_horas_uteis'


class MkSo(models.Model):
    codso = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=-1, blank=True, null=True)
    concentrador = models.CharField(max_length=1, blank=True, null=True)
    ponto_acesso = models.CharField(max_length=1, blank=True, null=True)
    cdscript_pesquisa_serial = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mk_so'


class MkTabelaIps(models.Model):
    codip = models.AutoField(primary_key=True)
    codrange = models.IntegerField(blank=True, null=True)
    numero_ip = models.CharField(unique=True, max_length=50, blank=True, null=True)
    status = models.CharField(max_length=1)
    historico = models.CharField(max_length=100, blank=True, null=True)
    associacao_atual = models.IntegerField(blank=True, null=True)
    numero_ip_bloqueio = models.CharField(max_length=20, blank=True, null=True)
    ocultar = models.CharField(max_length=1, blank=True, null=True)
    usado_para_equipamento = models.CharField(max_length=1, blank=True, null=True)
    cd_conexao_equip = models.IntegerField(blank=True, null=True)
    usado_para_rota = models.CharField(max_length=1, blank=True, null=True)
    ignora_duplicidade = models.CharField(max_length=1, blank=True, null=True)
    cd_rota = models.IntegerField(blank=True, null=True)
    guid_referencia = models.CharField(max_length=50, blank=True, null=True)
    cd_empresa = models.IntegerField(blank=True, null=True)
    familia = models.IntegerField(blank=True, null=True)
    numero_ipv6 = models.CharField(unique=True, max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mk_tabela_ips'


class MkTelefoniaPlataformas(models.Model):
    codtelefoniaplataforma = models.AutoField()
    cd_batch_inadiplente = models.IntegerField(blank=True, null=True)
    telefonia_bd_senha_tip = models.CharField(max_length=20, blank=True, null=True)
    telefonia_bd_usuario_tip = models.CharField(max_length=21, blank=True, null=True)
    telefonia_bd_tip = models.CharField(max_length=21, blank=True, null=True)
    telefonia_servidor_bd_tip = models.CharField(max_length=79, blank=True, null=True)
    telefone_url_sip = models.CharField(max_length=101, blank=True, null=True)
    telefonia_senha_tip = models.CharField(max_length=20, blank=True, null=True)
    telefonia_usuario_tip = models.CharField(max_length=21, blank=True, null=True)
    telefone_url_tip = models.CharField(max_length=102, blank=True, null=True)
    telefone_url_vsc = models.CharField(max_length=51, blank=True, null=True)
    telefonia_usuario_vsc = models.CharField(max_length=21, blank=True, null=True)
    telefonia_senha_vsc = models.CharField(max_length=21, blank=True, null=True)
    telefonia_sip_dominio = models.CharField(max_length=75, blank=True, null=True)
    telefonia_prefixo_ddi = models.IntegerField(blank=True, null=True)
    telefonia_prefixo_ddd = models.IntegerField(blank=True, null=True)
    telefonia_cod_area = models.IntegerField(blank=True, null=True)
    telefonia_cod_pais = models.IntegerField(blank=True, null=True)
    telefone_usuario_sip = models.CharField(max_length=21, blank=True, null=True)
    telefone_senha_sip = models.CharField(max_length=20, blank=True, null=True)
    telefone_servidorbd_sip = models.CharField(max_length=79, blank=True, null=True)
    telefone_bd_sip = models.CharField(max_length=21, blank=True, null=True)
    telefone_identificacao = models.CharField(max_length=100, blank=True, null=True)
    telefonia_sip_usuario_bd = models.CharField(max_length=21, blank=True, null=True)
    telefonia_sip_senha_bd = models.CharField(max_length=20, blank=True, null=True)
    voip_empresa = models.CharField(max_length=1, blank=True, null=True)
    ip_saperx = models.CharField(max_length=50, blank=True, null=True)
    porta_saperx = models.CharField(max_length=10, blank=True, null=True)
    usuario_saperx = models.CharField(max_length=50, blank=True, null=True)
    senha_saperx = models.CharField(max_length=50, blank=True, null=True)
    banco_saperx = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mk_telefonia_plataformas'


class MkTelefoniaVscBatch(models.Model):
    codbatch = models.AutoField()
    batch_id = models.IntegerField()
    batch_descricao = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mk_telefonia_vsc_batch'


class MkUnidadeDre(models.Model):
    codunddre = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=100, blank=True, null=True)
    pai = models.IntegerField(blank=True, null=True)
    tipo = models.CharField(max_length=1, blank=True, null=True)
    cd_empresa = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mk_unidade_dre'


class MkUnidadeFinanceia(models.Model):
    codundfinanceira = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=35, blank=True, null=True)
    grau = models.IntegerField(blank=True, null=True)
    str_permissao_usuarios = models.CharField(max_length=200, blank=True, null=True)
    nomenclatura = models.CharField(unique=True, max_length=50, blank=True, null=True)
    classificacao_contabil = models.CharField(max_length=30, blank=True, null=True)
    classificacao_fiscal = models.CharField(max_length=10, blank=True, null=True)
    cd_empresa = models.IntegerField(blank=True, null=True)
    debito_credito = models.CharField(max_length=1, blank=True, null=True)
    em_uso = models.CharField(max_length=1, blank=True, null=True)
    cd_unid_dre = models.ForeignKey(MkUnidadeDre, models.DO_NOTHING, db_column='cd_unid_dre', blank=True, null=True)
    pai = models.IntegerField(blank=True, null=True)
    permite_lcto = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mk_unidade_financeia'


class Projeto(models.Model):
    projeto_id = models.CharField(primary_key=True, max_length=36)
    pro_nome = models.CharField(max_length=40, blank=True, null=True)
    pro_latitude = models.DecimalField(max_digits=11, decimal_places=9, blank=True, null=True)
    pro_longitude = models.DecimalField(max_digits=11, decimal_places=9, blank=True, null=True)
    pro_descricao = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'projeto'


class TipoElemento(models.Model):
    tipo_elemento_id = models.IntegerField(primary_key=True)
    tpe_icone = models.CharField(max_length=255, blank=True, null=True)
    tpe_descricao = models.CharField(max_length=40, blank=True, null=True)
    tpe_sigla = models.CharField(max_length=5, blank=True, null=True)
    frm_guid = models.CharField(max_length=38, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_elemento'


class Username(models.Model):
    codigo = models.IntegerField(blank=True, null=True)
    login = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'username'
