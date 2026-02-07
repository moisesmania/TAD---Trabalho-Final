# TAD---Trabalho-Final
# 📊 Demografia Empresarial Brasileira

Aplicação interativa desenvolvida em **Streamlit** para análise da demografia empresarial no Brasil, utilizando dados de municípios, PIB, população e um **modelo de regressão linear** para estimar o número de empresas atuantes.

O projeto permite:

* Filtrar municípios por **UF**
* Visualizar dados tabulares e gráficos
* Analisar a relação entre **PIB x Número de Empresas**
* Exibir ranking dos municípios com mais empresas
* Simular cenários usando um **modelo preditivo treinado previamente**

---

## 🧱 Estrutura do Projeto

```
TAD---Trabalho-Final/
│
├── app.py                         # Aplicação Streamlit
├── df_final.csv                   # Base de dados final tratada
├── modelo_regressao_empresas.pkl  # Modelo de regressão linear treinado
├── requirements.txt               # Dependências do projeto
└── README.md                      # Documentação do projeto
```

---

## ⚙️ Tecnologias Utilizadas

* Python 3.10+
* Streamlit
* Pandas
* Matplotlib
* Scikit-learn
* Joblib
* Visual Studio Code

---

## 📦 Instalação e Execução (Windows + VS Code)

### 1️⃣ Pré-requisitos

* Windows 10 ou superior
* Python instalado (recomendado **Python 3.10 ou 3.11**)
* VS Code instalado

Verifique o Python no terminal:

```bash
python --version
```

---

### 2️⃣ Clonar o repositório

No terminal do VS Code:

```bash
git clone https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git
cd NOME_DO_REPOSITORIO
```

---

### 3️⃣ Criar ambiente virtual (opcional, mas recomendado)

```bash
python -m venv venv
```

Ativar o ambiente virtual:

```bash
venv\Scripts\activate
```

---

### 4️⃣ Instalar dependências

Crie um arquivo `requirements.txt` com o conteúdo abaixo (caso ainda não exista):

```txt
streamlit
pandas
matplotlib
scikit-learn
joblib
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

---

### 5️⃣ Executar a aplicação

No terminal do VS Code:

```bash
streamlit run app.py
```

O navegador será aberto automaticamente em:

```
http://localhost:8501
```

---

## 📈 Modelo de Regressão

O modelo utilizado é uma **regressão linear múltipla**, treinada previamente com as variáveis:

* `x_pib_total`
* `x_pop_total`

Objetivo:

> Estimar o **Número de Empresas Atuantes** em um município.

O modelo é carregado via arquivo:

```python
modelo_regressao_empresas.pkl
```

---

## 🧪 Funcionalidades da Aplicação

* ✅ Filtro por Unidade Federativa (UF)
* ✅ Tabela com altura controlada (menos scroll)
* ✅ Gráfico de dispersão com **linha de regressão**
* ✅ Ranking Top 10 municípios
* ✅ Simulação de cenários econômicos
* ✅ Tratamento de erros (dataset vazio, colunas ausentes, erro de modelo)

---

## 🛡️ Tratamento de Erros Implementado

* Verificação de colunas obrigatórias
* Validação de filtros vazios
* Proteção contra falhas no modelo
* Prevenção de entradas inválidas na simulação

---

## 👨‍💻 Autor(es):

Projeto desenvolvido como **Trabalho Final (TAD)** para fins acadêmicos.

**Autor 1:** Moisés José do Nascimento 
**Autor 2:** Mateus Samuel de Oliveira Félix

---

## 📄 Licença

Este projeto é de uso acadêmico e educacional.

Sinta-se à vontade para estudar, adaptar e evoluir o código.
