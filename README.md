# TAD---Trabalho-Final
# 📊 Demografia Empresarial Brasileira

Aplicação interativa desenvolvida em **Streamlit** para análise da demografia empresarial no Brasil, utilizando dados de municípios, PIB, população e um **modelo de regressão linear** para estimar o número de empresas atuantes.

O projeto permite:

- Filtrar municípios por **UF**
- Visualizar dados tabulares e gráficos
- Analisar a relação entre **PIB x Número de Empresas**
- Exibir ranking dos municípios com mais empresas
- Simular cenários usando um **modelo preditivo treinado previamente**

---

## 🧱 Estrutura do Projeto

```text
TAD---Trabalho-Final/
│
├── app.py
├── df_final.csv
├── modelo_regressao_empresas.pkl
├── requirements.txt
└── README.md
⚙️ Tecnologias Utilizadas
Python 3.10+

Streamlit

Pandas

Matplotlib

Scikit-learn

Joblib

Visual Studio Code

📦 Instalação e Execução (Windows + VS Code)
1️⃣ Clonar o repositório
git clone https://github.com/moisesmania/TAD---Trabalho-Final.git
cd TAD---Trabalho-Final
2️⃣ Criar ambiente virtual
python -m venv .venv
Ativar o ambiente virtual:

.venv\Scripts\activate
3️⃣ Instalar dependências
pip install -r requirements.txt
4️⃣ Executar a aplicação
streamlit run app.py
A aplicação será aberta em:

http://localhost:8501
📈 Modelo de Regressão
O modelo utilizado é uma Regressão Linear Múltipla, treinada previamente no Google Colab e salva com joblib.

Variáveis de entrada:
x_pib_total

x_pop_total

Variável alvo:
Numero_Empresas_Atuantes

Arquivo do modelo:

modelo_regressao_empresas.pkl
⚠️ Observação
O modelo deve ser carregado com a mesma versão do scikit-learn usada no treinamento para evitar warnings de incompatibilidade.

🧪 Funcionalidades da Aplicação
✅ Filtro por Unidade Federativa (UF)

✅ Tabela com altura controlada

✅ Gráfico de dispersão PIB x Empresas

✅ Ranking Top 10 municípios

✅ Simulação de cenários econômicos

✅ Uso de modelo preditivo treinado

🛡️ Tratamento de Erros
Verificação de colunas obrigatórias

Proteção contra dataset vazio

Validação de entradas do usuário

Tratamento de erro ao carregar o modelo .pkl

👨‍💻 Autor(es)
Projeto desenvolvido como Trabalho Final (TAD) para fins acadêmicos.

Moisés José do Nascimento

Mateus Samuel de Oliveira Félix