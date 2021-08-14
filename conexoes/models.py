from django.db import models

# Create your models here.
class MkConexoes(models.Model):
    codconexao = models.AutoField(primary_key=True)
    codcliente = models.ForeignKey('MkPessoas', models.DO_NOTHING, db_column='codcliente', related_name='cod_cliente')
    tipo_conexao = models.IntegerField()
    autenticacao = models.IntegerField()
    username = models.CharField(max_length=50, blank=True, null=True)
    password = models.CharField(max_length=30, blank=True, null=True)
    instalador = models.ForeignKey('MkPessoas', models.DO_NOTHING, db_column='instalador', blank=True, null=True)
    cadastrado = models.DateField()
    advertise_url = models.CharField(max_length=100, blank=True, null=True)
    advertise_time = models.IntegerField(blank=True, null=True)
    site_inicial = models.CharField(max_length=100, blank=True, null=True)
    # codservidor = models.ForeignKey('MkServidores', models.DO_NOTHING, db_column='codservidor')
    codponto_acesso = models.IntegerField(blank=True, null=True)
    # codplano_acesso = models.ForeignKey('MkPlanosAcesso', models.DO_NOTHING, db_column='codplano_acesso')
    # codendereco_ip = models.OneToOneField('MkTabelaIps', models.DO_NOTHING, db_column='codendereco_ip', blank=True, null=True)
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
    # cd_caixa = models.ForeignKey('MkFiberCaixa', models.DO_NOTHING, db_column='cd_caixa', blank=True, null=True)
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
#    cd_regra_faturamento = models.ForeignKey('MkFaturamentosRegras', models.DO_NOTHING, db_column='cd_regra_faturamento', blank=True, null=True)
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
 #   cd_regua_configuracao = models.ForeignKey('MkReguaTipo', models.DO_NOTHING, db_column='cd_regua_configuracao', blank=True, null=True)
    dt_hr_insert = models.DateTimeField(blank=True, null=True)
    guid_id_gerecao = models.CharField(max_length=50, blank=True, null=True)
    abrir_os_retirada = models.CharField(max_length=1, blank=True, null=True)
    tv_cod_assinante = models.CharField(max_length=80, blank=True, null=True)
    tv_idorder = models.CharField(max_length=200, blank=True, null=True)
   # cd_tabela_sla = models.ForeignKey('MkSla', models.DO_NOTHING, db_column='cd_tabela_sla', blank=True, null=True)
    rever_contas_antes_faturar = models.CharField(max_length=1, blank=True, null=True)
    tipo_plano = models.IntegerField(blank=True, null=True)
    ignora_fatura_na_geracao_conta = models.CharField(max_length=1, blank=True, null=True)
    criar_conta_pelo_vlr_sugerido = models.CharField(max_length=1, blank=True, null=True)
    erro_ao_ativar_auto = models.CharField(max_length=1, blank=True, null=True)
    #cd_agrupador = models.ForeignKey('MkContratosAgrupadores', models.DO_NOTHING, db_column='cd_agrupador', blank=True, null=True)
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
    #cd_composicao_derivacao = models.ForeignKey('MkPlanosAcesso', models.DO_NOTHING, db_column='cd_composicao_derivacao', blank=True, null=True)
    num_terminal_telefonico = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mk_contratos'


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

class MkCidades(models.Model):
    codcidade = models.AutoField(primary_key=True)
    #codestado = models.ForeignKey('MkEstados', models.DO_NOTHING, db_column='codestado')
    cidade = models.CharField(max_length=50)
    ibge = models.CharField(max_length=10, blank=True, null=True)
    latitude = models.CharField(max_length=50, blank=True, null=True)
    longitude = models.CharField(max_length=50, blank=True, null=True)
    nao_encontrato = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mk_cidades'

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
    #codestado = models.ForeignKey(MkEstados, models.DO_NOTHING, db_column='codestado')
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
    # motivo_inatividade = models.ForeignKey('MkPessoasInatividade', models.DO_NOTHING, db_column='motivo_inatividade', blank=True, null=True)
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
   # grupo_atendimento = models.ForeignKey('MkPessoasGrupos', models.DO_NOTHING, db_column='grupo_atendimento', blank=True, null=True)
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
