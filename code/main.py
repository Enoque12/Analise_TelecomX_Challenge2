import streamlit as st
from utils import carregar_dados, metodopagamento
from graficos import (
    grafico_churn_genero, 
    grafico_churn_Contrato,
    grafico_churn_gastototal,
    grafico_churn_gastomensal,
    grafico_metodoPagamento
    )

st.set_page_config(layout="wide")

df = carregar_dados()

st.sidebar.markdown("<h1 style='text-align:center;'>Telecom - X</h1><hr>", unsafe_allow_html=True)

st.sidebar.title("Filtros")

churn_opcao = st.sidebar.radio("Churn", options=["Todos", "Churn", "Não Churn"])
generos = st.sidebar.multiselect("Gênero", options=df['Genero'].unique(), default=df['Genero'].unique())
servicos = st.sidebar.multiselect("Tipo de Serviço", options=df["Servico_Internet"].unique(), default=df["Servico_Internet"].unique())
contratos = st.sidebar.multiselect("Tipo de Contrato", options=df["Tipo_Contrato"].unique(), default=df["Tipo_Contrato"].unique())
pagamentos = st.sidebar.multiselect("Tipo Pagamento", options=df["Metodo_Pagamento"].unique(), default=df["Metodo_Pagamento"].unique())

df_filtrado = df[
    (df["Genero"].isin(generos)) &
    (df["Servico_Internet"].isin(servicos)) &
    (df["Tipo_Contrato"].isin(contratos)) &
    (df["Metodo_Pagamento"].isin(pagamentos))
]

if churn_opcao == "Churn":
    df_filtrado = df_filtrado[df_filtrado["Evasao"] == 1]
elif churn_opcao == "Não Churn":
    df_filtrado = df_filtrado[df_filtrado["Evasao"] == 0]

st.markdown(
    """
    <div style="text-align: center;">
        <h1>📊 Telecom X - Análise de Churn</h1>
        <h6>Monitoramento interativo do cancelamento de clientes</h6>
        <hr>
    </div>
    """,
    unsafe_allow_html=True
)

st.subheader("Visão Geral")

total_clientes = df_filtrado.shape[0]
percent_churn = df_filtrado[df_filtrado['Evasao'] == 1].shape[0] / total_clientes * 100 if total_clientes > 0 else 0
percent_retencao = 100 - percent_churn

# Criar 5 colunas (3 para métricas + 2 para separadores)
col1, col_sep1, col2, col_sep2, col3 = st.columns([3, 0.4, 3, 0.4, 3])

# 1ª métrica
with col1:
    st.metric("Total Clientes", total_clientes)
    
# Separador 1
with col_sep1:
    st.markdown(
        "<div style='border-left:2px solid gray; height:60px; margin:auto;'></div>",
        unsafe_allow_html=True
    )

# 2ª métrica
with col2:
    st.metric("Churn (%)", f"{percent_churn:.2f}%")

# Separador 2
with col_sep2:
    st.markdown(
        "<div style='border-left:2px solid gray; height:60px; margin:auto;'></div>",
        unsafe_allow_html=True
    )

# 3ª métrica
with col3:
    st.metric("Taxa de Retenção", f"{percent_retencao:.2f}%")
    
st.subheader("👤 Perfil dos Clientes")

col1c, col2c = st.columns(2)

with col1c:
    st.plotly_chart(grafico_churn_genero(df_filtrado), use_container_width=True)

with col2c:
    st.plotly_chart(grafico_churn_Contrato(df_filtrado), use_container_width=True)

st.subheader("📌 Factores que influenciam o Churn")

col1f, col2f = st.columns(2)

with col1f:
    st.plotly_chart(grafico_churn_gastomensal(df_filtrado), use_container_width=True)
    
with col2f:
    st.plotly_chart(grafico_churn_gastototal(df_filtrado), use_container_width=True)
    
col, = st.columns(1)

with col:
    st.plotly_chart(grafico_metodoPagamento(metodopagamento(df_filtrado, churn_opcao)), use_container_width=True)
    
st.markdown("<hr><div style='text-align:center; color:gray;'><small>Desenvolvido por Enoque Mandlate © 2025</small></div>", unsafe_allow_html=True)