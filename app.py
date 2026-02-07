import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
from pathlib import Path

# -------------------------------------------------
# Configuração geral da página
# -------------------------------------------------
st.set_page_config(
    page_title="Demografia Empresarial",
    layout="wide"  # utiliza toda a largura disponível da tela
)

st.title("Demografia Empresarial Brasileira")

# -------------------------------------------------
# Carregamento dos dados
# -------------------------------------------------
ARQUIVO_DADOS = Path("df_final.csv")
ARQUIVO_MODELO = Path("modelo_regressao_empresas.pkl")

# Verifica se o arquivo CSV existe
if not ARQUIVO_DADOS.exists():
    st.error("Arquivo df_final.csv não encontrado.")
    st.stop()

# Leitura do dataset
df = pd.read_csv(ARQUIVO_DADOS)

# Verifica se as colunas obrigatórias existem
COLUNAS_OBRIGATORIAS = [
    "nome_municipio",
    "uf_sigla",
    "Numero_Empresas_Atuantes",
    "pib_total",
    "pop_total"
]

colunas_faltando = set(COLUNAS_OBRIGATORIAS) - set(df.columns)

if colunas_faltando:
    st.error(f"Colunas ausentes no dataset: {colunas_faltando}")
    st.stop()

# -------------------------------------------------
# Carregamento do modelo de regressão
# -------------------------------------------------
# Modelo treinado previamente (regressão linear múltipla)
# Entradas: PIB total e população
# Saída: número de empresas
if not ARQUIVO_MODELO.exists():
    st.error("Arquivo do modelo não encontrado.")
    st.stop()

modelo = joblib.load(ARQUIVO_MODELO)

# -------------------------------------------------
# Filtros laterais
# -------------------------------------------------
st.sidebar.header("Filtros")

# Lista de UFs disponíveis no dataset
ufs = sorted(df["uf_sigla"].dropna().unique())

# Multiselect de UF
uf_selecionada = st.sidebar.multiselect(
    "UF",
    options=ufs,
    default=ufs
)

# Aplica filtro somente se houver UF selecionada
if uf_selecionada:
    df_filtro = df[df["uf_sigla"].isin(uf_selecionada)]
else:
    st.warning("Nenhuma UF selecionada.")
    df_filtro = df.copy()

# -------------------------------------------------
# Tabela de dados (altura controlada)
# -------------------------------------------------
st.subheader("Base de dados (amostra)")

st.dataframe(
    df_filtro[
        [
            "nome_municipio",
            "uf_sigla",
            "Numero_Empresas_Atuantes",
            "pib_total",
            "pop_total"
        ]
    ],
    height=300  # evita scroll excessivo na página
)

# -------------------------------------------------
# Gráfico e ranking lado a lado
# -------------------------------------------------
st.subheader("Análises")

col1, col2 = st.columns(2)

# -------- Gráfico de dispersão --------
with col1:
    st.markdown("**PIB Total x Número de Empresas Atuantes**")

    fig, ax = plt.subplots()

    ax.scatter(
        df_filtro["pib_total"],
        df_filtro["Numero_Empresas_Atuantes"],
        alpha=0.6
    )

    ax.set_xlabel("PIB Total (R$)")
    ax.set_ylabel("Número de Empresas Atuantes")

    st.pyplot(fig)

# -------- Ranking --------
with col2:
    st.markdown("**Top 10 Municípios com mais Empresas Atuantes**")

    ranking = (
        df_filtro
        .sort_values("Numero_Empresas_Atuantes", ascending=False)
        .head(10)
    )

    st.dataframe(
        ranking[
            ["nome_municipio", "uf_sigla", "Numero_Empresas_Atuantes"]
        ],
        height=300
    )

# -------------------------------------------------
# Simulação de cenários
# -------------------------------------------------
st.subheader("Simulação de Cenários")

c1, c2, c3 = st.columns(3)

# Entrada do PIB
with c1:
    pib = st.number_input(
        "PIB Total (R$)",
        min_value=0.0,
        step=1_000_000.0
    )

# Entrada da população
with c2:
    pop = st.number_input(
        "População",
        min_value=0,
        step=1_000
    )

# Botão de previsão
with c3:
    st.write("")  # espaçamento visual
    st.write("")

    if st.button("Prever"):
        # Validação simples dos valores
        if pib <= 0 or pop <= 0:
            st.warning("Informe valores válidos para PIB e população.")
        else:
            # DataFrame no mesmo formato usado no treino do modelo
            entrada = pd.DataFrame({
                "x_pib_total": [pib],
                "x_pop_total": [pop]
            })

            # Previsão com o modelo de regressão
            previsao = modelo.predict(entrada)[0]

            st.success(
                f"Número estimado de empresas: {int(previsao)}"
            )
