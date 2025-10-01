import pandas as pd

def carregar_dados():
    df = pd.read_json('../Dados_API/dados_tratados.json')
    return df

def metodopagamento(df, churn):
    df_pagamento = pd.crosstab(df['Metodo_Pagamento'], df['Evasao']).reset_index()
    
    df_pagamento.rename(columns={0:'Não Churn', 1:'Churn'}, inplace=True)

    if churn == "Churn":
        df_pagamento['Percentagem'] = round(df_pagamento['Churn'] / (df_pagamento['Churn']) * 100, 2)
    elif churn == "Não Churn":
        df_pagamento['Percentagem'] = round(df_pagamento['Não Churn'] / (df_pagamento['Não Churn']) * 100, 2)
    else:
        df_pagamento['Percentagem'] = round(df_pagamento['Churn'] / (df_pagamento['Churn'] + df_pagamento['Não Churn']) * 100, 2)
    return df_pagamento