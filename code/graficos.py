import plotly.express as px

def grafico_churn_genero(df):
    fig = px.histogram(
        df,
        x="Genero",
        color="Evasao",
        barmode="group",
        title="Distribuição de Churn por Gênero",   
    )
    return fig

def grafico_churn_Contrato(df):
    fig = px.histogram(
        df,
        x="Tipo_Contrato",
        color="Evasao",
        barmode="group",
        title="Churn pelo Tipo de Contrato",   
    )
    return fig

def grafico_churn_gastomensal(df):
    fig = px.box(
        df,
        x="Evasao",
        y="Gasto_Mensal",
        title="Distribuição dos Churn pelo Gasto Mensal"
    )
    return fig

def grafico_churn_gastototal(df):
    fig = px.box(
        df,
        x="Evasao",
        y="Gasto_Total",
        title="Distribuição dos Churn pelo Gasto Total"
    )
    return fig

def grafico_metodoPagamento(df):
    fig = px.bar(
        df,
        x="Percentagem",              # valores
        y="Metodo_Pagamento",         # categorias
        orientation="h",              # barras horizontais
        text="Percentagem",           # rótulos nas barras
        color="Metodo_Pagamento",     # cor diferente para cada método
        color_discrete_sequence=px.colors.sequential.Tealgrn,  # paleta
        title="Distribuição de Churn pelo Método de Pagamento"
    )
    
    fig.update_traces(
        texttemplate='%{text:.2f}%',   # mostra valores com duas casas decimais
        textposition="outside"         # rótulos para fora da barra
    )
    
    fig.update_layout(
        xaxis_title="",                # remove label do eixo X
        yaxis_title="",                # remove label do eixo Y
        showlegend=False,              # esconde legenda (opcional)
        bargap=0.3                     # espaçamento entre as barras
    )
    return fig