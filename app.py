import streamlit as st 
import pandas as pd
import plotly.express as px
from wordcloud import WordCloud

st.set_page_config(layout="wide")


st.sidebar.title("Painel de Controle")
st.sidebar.markdown("Use os filtros abaixo para atualizar os gráficos:")

df_ia = pd.read_csv('data/ai_chip_market_limpo.csv')
df_precos = pd.read_csv('data/chip_prices_limpo.csv')
df_precos['year_month'] = pd.to_datetime(df_precos['year_month'])
df_agrupado = df_precos.groupby(['year_month', 'product'])['price'].mean().reset_index()

lista_de_anos = df_ia['year'].unique()
ano_selecionado = st.sidebar.selectbox("Escolha o Ano de Vendas:", lista_de_anos)

lista_produtos = df_agrupado['product'].unique()
produtos_escolhidos = st.sidebar.multiselect(
    "Compare os Componentes:",
    options=lista_produtos,
    default=['DRAM_DDR4_8Gb', 'NAND_64Gb_MLC'] 
)

st.sidebar.divider()
st.sidebar.info("Dashboard - Indústria de Semicondutores")

col1, col2 = st.columns(2)

with col1:
    df_cruzado = pd.read_csv('data/dados_cruzados_ia_financas.csv')
    st.subheader("Impacto do Preço (ASP) na Margem")
    fig1 = px.scatter(df_cruzado, x='estimated_asp_usd', y='operating_margin_pct', color='vendor', size='revenue_usd_bn')
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.subheader(f"Vendas de Chips em {ano_selecionado}")
    df_filtrado_ia = df_ia[df_ia['year'] == ano_selecionado] 
    fig2 = px.bar(df_filtrado_ia, x='chip_name', y='estimated_revenue_usd_m', color='vendor')
    st.plotly_chart(fig2, use_container_width=True)

st.divider() 

col3, col4 = st.columns(2)

with col3:
    st.subheader("Evolução Mensal de Preços")
    df_filtrado_linhas = df_agrupado[df_agrupado['product'].isin(produtos_escolhidos)] 
    fig_linhas = px.line(df_filtrado_linhas, x='year_month', y='price', color='product')
    st.plotly_chart(fig_linhas, use_container_width=True)

with col4:
    st.subheader("Market Share por Segmento")
    df_fin = pd.read_csv('data/chip_companies_financials_limpo.csv')
    fig_treemap = px.treemap(df_fin, path=[px.Constant("Indústria Global"), 'segment', 'company_name'], values='revenue_usd_bn', color='operating_margin_pct', color_continuous_scale='RdYlGn')
    st.plotly_chart(fig_treemap, use_container_width=True)

st.divider()

st.subheader("Termos nas descrições dos chips")
texto_completo = " ".join(df_ia['description'].dropna())
nuvem = WordCloud(width=1200, height=300, background_color=None, mode='RGBA', max_words=100).generate(texto_completo)
st.image(nuvem.to_array(), use_container_width=True)