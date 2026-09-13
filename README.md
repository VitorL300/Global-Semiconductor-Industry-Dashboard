

    <h1>Dashboard da Indústria de Semicondutores</h1>

    <p>Este projeto é uma aplicação web interativa desenvolvida em Python para analisar o mercado global de semicondutores. O painel (<em>dashboard</em>) cruza dados financeiros das maiores empresas de hardware do mundo com o histórico de preços de componentes básicos (memórias DRAM e NAND) e o cenário em expansão de aceleradores e chips de Inteligência Artificial.</p>

    <h2>Funcionalidades Principais</h2>
    <ul>
        <li><strong>Impacto de Preço na Margem:</strong> Gráfico de dispersão relacionando o Preço Médio de Venda (ASP) dos chips com a margem operacional das fabricantes.</li>
        <li><strong>Receita de Chips de IA:</strong> Análise interativa da receita estimada por fabricante e modelo de chip, filtrável por ano de lançamento/venda.</li>
        <li><strong>Evolução Histórica de Preços:</strong> Monitoramento mensal de preços de componentes (como DDR4 e NAND MLC). O usuário pode comparar múltiplos produtos simultaneamente através do menu lateral.</li>
        <li><strong>Market Share por Segmento:</strong> Treemap hierárquico detalhando a receita global e a saúde financeira (escala de cor baseada na margem operacional) das companhias, divididas por setor de atuação.</li>
        <li><strong>Nuvem de Palavras:</strong> Visualização dos termos técnicos mais frequentes utilizados nas especificações dos chips de IA.</li>
    </ul>

    <h2>Tecnologias e Bibliotecas</h2>
    <ul>
        <li><strong>Interface Web:</strong> Streamlit</li>
        <li><strong>Manipulação de Dados:</strong> Pandas</li>
        <li><strong>Visualizações Gráficas:</strong> Plotly (Plotly Express)</li>
        <li><strong>Geração de Imagens:</strong> WordCloud</li>
    </ul>

    <h2>Estrutura de Dados</h2>
    <p>O painel espera encontrar quatro arquivos na pasta <code>data/</code> para funcionar corretamente:</p>
    <ul>
        <li><code>ai_chip_market_limpo.csv</code>: Informações sobre modelos, descrições, fornecedores e receita de chips focados em IA.</li>
        <li><code>chip_prices_limpo.csv</code>: Série histórica mensal do preço de componentes de hardware.</li>
        <li><code>dados_cruzados_ia_financas.csv</code>: Métricas de correlação entre o ASP (Average Selling Price) e as margens operacionais.</li>
        <li><code>chip_companies_financials_limpo.csv</code>: Dados de faturamento, margem e segmentação de mercado de cada empresa global.</li>
    </ul>

    <h2>Como Executar Localmente</h2>
    <ol>
        <li>Clone o repositório para a sua máquina.</li>
        <li>Instale as bibliotecas necessárias:
            <pre><code>pip install streamlit pandas plotly wordcloud</code></pre>
        </li>
        <li>Certifique-se de que a pasta <code>data/</code> com os arquivos CSV correspondentes está na mesma raiz do script.</li>
        <li>Inicie a aplicação executando:
            <pre><code>streamlit run nome_do_arquivo.py</code></pre>
        </li>
    </ol>


<img width="1920" height="822" alt="Captura de Tela (258)" src="https://github.com/user-attachments/assets/f89c7dfa-a17d-4370-ba55-399b79f8c77c" />
<img width="1920" height="815" alt="Captura de Tela (259)" src="https://github.com/user-attachments/assets/38f3b319-d164-4b87-8aaf-18da3244c8af" />
<img width="1920" height="804" alt="Captura de Tela (260)" src="https://github.com/user-attachments/assets/aba6b8f9-2936-4ed8-a38d-8c860d714f24" />


