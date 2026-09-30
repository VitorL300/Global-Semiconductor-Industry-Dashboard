# 💻 Dashboard da Indústria de Semicondutores

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](COLE_AQUI_O_LINK_DO_SEU_APP)

Este projeto é uma aplicação web interativa desenvolvida em Python (usando Streamlit) para analisar o mercado global de semicondutores. O painel cruza dados financeiros das maiores empresas de hardware do mundo com o histórico de preços de componentes básicos (memórias DRAM e NAND) e o cenário em expansão de aceleradores e chips de Inteligência Artificial.

## ✨ Funcionalidades Principais

* **📈 Impacto de Preço na Margem:** Gráfico de dispersão relacionando o Preço Médio de Venda (ASP) dos chips com a margem operacional das fabricantes.
* **📊 Receita de Chips de IA:** Análise interativa da receita estimada por fabricante e modelo de chip, com filtros dinâmicos por ano de lançamento/venda.
* **📉 Evolução Histórica de Preços:** Monitoramento mensal de preços de componentes (como DDR4 e NAND MLC). O usuário pode comparar múltiplos produtos simultaneamente através do menu lateral.
* **🗺️ Market Share por Segmento:** Treemap hierárquico detalhando a receita global e a saúde financeira (com escala de cor baseada na margem operacional) das companhias, divididas por setor de atuação.
* **☁️ Nuvem de Palavras:** Visualização dos termos técnicos mais frequentes utilizados nas especificações descritivas dos chips de IA.

## 🛠️ Tecnologias e Bibliotecas

O projeto foi construído utilizando as seguintes ferramentas:
* **Streamlit:** Criação da interface web interativa.
* **Pandas:** Leitura, limpeza e manipulação de dados.
* **Plotly Express:** Renderização de visualizações gráficas interativas.
* **WordCloud:** Geração da nuvem de palavras.

## 📁 Estrutura de Dados

O painel espera encontrar um diretório chamado `data/` na raiz do projeto contendo quatro arquivos CSV para funcionar corretamente:
* `ai_chip_market_limpo.csv`: Informações sobre modelos, descrições, fornecedores e receita de chips focados em IA.
* `chip_prices_limpo.csv`: Série histórica mensal do preço de componentes de hardware.
* `dados_cruzados_ia_financas.csv`: Métricas de correlação entre o ASP (Average Selling Price) e as margens operacionais.
* `chip_companies_financials_limpo.csv`: Dados de faturamento, margem e segmentação de mercado de cada empresa global.

## 🚀 Como Executar Localmente

Siga os passos abaixo para rodar o projeto na sua máquina:

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/VitorL300/Global-Semiconductor-Industry-Dashboard.git](https://github.com/VitorL300/Global-Semiconductor-Industry-Dashboard.git)
   cd Global-Semiconductor-Industry-Dashboard

2. **Crie e ative um ambiente virtual (recomendado):**
   python -m venv venv

   # Para ativar no Windows:
   venv\Scripts\activate
   # Para ativar no Mac/Linux:
   source venv/bin/activate

3. **Instale as dependências:**
   Com o ambiente virtual ativado, instale as bibliotecas listadas no arquivo de requisitos:
   
   pip install -r requirements.txt
   
4. **Verifique os dados:**
   Certifique-se de que a pasta data/ com os arquivos CSV correspondentes está na mesma raiz do script principal (app.py).

5. **Inicie a aplicação:**
   streamlit run app.py
   O terminal exibirá um endereço local (geralmente http://localhost:8501) que você pode abrir no seu navegador para interagir com o dashboard.

☁️ **Deploy**

   A aplicação está hospedada e em produção no Streamlit Community Cloud.
   🔗 https://eda-industriadesemicondutores.streamlit.app/

   


<img width="1920" height="822" alt="Captura de Tela (258)" src="https://github.com/user-attachments/assets/f89c7dfa-a17d-4370-ba55-399b79f8c77c" />
<img width="1920" height="815" alt="Captura de Tela (259)" src="https://github.com/user-attachments/assets/38f3b319-d164-4b87-8aaf-18da3244c8af" />
<img width="1920" height="804" alt="Captura de Tela (260)" src="https://github.com/user-attachments/assets/aba6b8f9-2936-4ed8-a38d-8c860d714f24" />


