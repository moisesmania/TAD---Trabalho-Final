import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt

# -------------------------------------------------
# Configuração geral da página
# -------------------------------------------------
st.set_page_config(
    page_title="Demografia Empresarial",
    layout="wide"
)

st.title("Demografia Empresarial Brasileira")

# -------------------------------------------------
# Carregamento dos dados
# -------------------------------------------------
try:
    df = pd.read_csv("df_final.csv")
except Exception as e:
    st.error(f"Erro ao carregar o arquivo CSV: {e}")
    st.stop()

# Verificação de colunas obrigatórias
colunas_necessarias = [
    "nome_municipio",
    "uf_sigla",
    "Numero_Empresas_Atuantes",
    "pib_total",
    "pop_total"
]

for col in colunas_necessarias:
    if col not in df.columns:
        st.error(f"Coluna obrigatória ausente no dataset: {col}")
        st.stop()

# -------------------------------------------------
# Carregamento do modelo
# -------------------------------------------------
try:
    modelo = joblib.load("modelo_regressao_empresas.pkl")
except Exception as e:
    st.error(f"Erro ao carregar o modelo: {e}")
    st.stop()

# -------------------------------------------------
# Filtros laterais
# -------------------------------------------------
st.sidebar.header("Filtros")

ufs = sorted(df["uf_sigla"].dropna().unique())

uf = st.sidebar.multiselect(
    "UF",
    options=ufs,
    default=ufs
)

df_filtro = df[df["uf_sigla"].isin(uf)].copy()

# Evita erros quando o filtro zera o dataset
if df_filtro.empty:
    st.warning("Nenhum dado disponível para os filtros selecionados.")
    st.stop()

# -------------------------------------------------
# Tabela de dados
# -------------------------------------------------
st.subheader("Base de dados (amostra)")

st.dataframe(
    df_filtro[colunas_necessarias],
    height=300
)

# -------------------------------------------------
# Gráfico e Ranking
# -------------------------------------------------
st.subheader("Análises")

col1, col2 = st.columns(2)

# -------- Gráfico --------
with col1:
    st.markdown("**PIB Total x Número de Empresas Atuantes**")

    fig, ax = plt.subplots(figsize=(5, 4))

    # Scatter dos dados reais
    ax.scatter(
        df_filtro["pib_total"],
        df_filtro["Numero_Empresas_Atuantes"],
        alpha=0.6,
        label="Dados reais"
    )

    # -----------------------
    # Linha de regressão
    # -----------------------
    try:
        X_reg = df_filtro[["pib_total", "pop_total"]].rename(columns={
            "pib_total": "x_pib_total",
            "pop_total": "x_pop_total"
        })

        df_filtro["empresas_previstas"] = modelo.predict(X_reg)

        df_ord = df_filtro.sort_values("pib_total")

        ax.plot(
            df_ord["pib_total"],
            df_ord["empresas_previstas"],
            linewidth=2,
            label="Regressão linear"
        )
    except Exception as e:
        st.warning("Não foi possível calcular a linha de regressão.")

    ax.set_xlabel("PIB Total")
    ax.set_ylabel("Número de Empresas Atuantes")
    ax.legend()

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
        ranking[["nome_municipio", "uf_sigla", "Numero_Empresas_Atuantes"]],
        height=300
    )

# -------------------------------------------------
# Simulação de cenários
# -------------------------------------------------
st.subheader("Simulação de Cenários")

c1, c2, c3 = st.columns(3)

with c1:
    pib = st.number_input(
        "PIB Total (R$)",
        min_value=0.0,
        step=1_000_000.0
    )

with c2:
    pop = st.number_input(
        "População",
        min_value=0,
        step=1_000
    )

with c3:
    st.write("")
    st.write("")
    if st.button("Prever"):
        if pib == 0 or pop == 0:
            st.warning("Informe valores válidos de PIB e população.")
        else:
            try:
                entrada = pd.DataFrame({
                    "x_pib_total": [pib],
                    "x_pop_total": [pop]
                })

                previsao = modelo.predict(entrada)[0]
                st.success(f"Número estimado de empresas: {int(previsao)}")
            except Exception as e:
                st.error(f"Erro ao realizar a previsão: {e}")
