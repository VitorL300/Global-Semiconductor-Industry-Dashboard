import pandas as pd


df_ia = pd.read_csv("data/ai_chip_market_limpo.csv")
df_fin = pd.read_csv("data/chip_companies_financials_limpo.csv")


df_cruzado = pd.merge(
    df_ia,
    df_fin,
    left_on=['vendor', 'year'],          
    right_on=['company_name', 'year'],  
    how='inner'                         
)


print(df_cruzado.shape) 
print(df_cruzado.head())
df_cruzado.to_csv("data/dados_cruzados_ia_financas.csv", index=False)




