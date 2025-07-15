
# Previsão de Preços Agrícolas em Moçambique

Este projecto utiliza Machine Learning para prever os preços de produtos agrícolas em Moçambique com base em dados históricos da WFP (World Food Programme). Inclui análise exploratória, modelagem, visualização com Power BI e uma aplicação interativa com Streamlit.

---

## Objectivo

- Apoiar agricultores, gestores e analistas com previsões de preços agrícolas
- Explorar dados reais e públicos para análise de tendências
- Fornecer um app e dashboard intuitivos para apoio à decisão

---

## Tecnologias Utilizadas

- Python (Pandas, Scikit-learn, XGBoost, Streamlit, Joblib)
- Power BI
- Google Drive (armazenamento de modelo)
- Git & GitHub

---

## Estrutura do Projecto

```
previsao_precos_agricolas/
├── app_streamlit.py              # Aplicação interativa
├── data/
│   └── wfp_food_prices_moz.csv   # Base de dados original
├── modelo/
│   └── modelo_rf.pkl             # (Link externo para download)
├── notebooks/
│   └── 04_Prevendo_Precos.ipynb  # Notebook de modelagem
├── PowerBI/
│   └── precos_agricolas_powerbi.csv  # Dataset limpo para Power BI
├── requirements.txt              # Dependências
├── .gitignore
└── README.md
```

---

## Como Executar Localmente

```bash
# Clone o repositório
git clone https://github.com/Shelzia/Previsao_Precos_Agricolas.git
cd Previsao_Precos_Agricolas

# (Opcional) Crie ambiente virtual
python -m venv venv
venv\Scripts\activate   # Windows

# Instale as dependências
pip install -r requirements.txt

# Baixe o modelo pré-treinado
# Coloque em: /modelo/modelo_rf.pkl

# Inicie a aplicação
streamlit run app_streamlit.py
```

---

## Principais Descobertas

- **Milho branco (Maize white)**, **Arroz importado** e **Farinha de trigo** são os produtos com maior variação de preços.
- As províncias do sul apresentam preços historicamente mais altos.
- Tendência de aumento de preços nos últimos dois anos para cereais básicos.
- O modelo Random Forest obteve melhor desempenho para previsão multivariada.

---

## Dashboard Power BI

> Arquivo: `PowerBI/precos_agricolas_powerbi.csv`

O dashboard inclui:

- Série temporal de preços por província
- Comparação entre produtos e anos
- Tabelas interativas por mercado

---

## Aplicação Streamlit

Interface interativa para simular previsões de preços agrícolas:

---

## Autora

**Shelzia Macie**  
Maputo, Moçambique  
Cientista de Dados | Analista de BI  
[LinkedIn](https://www.linkedin.com/in/shelzia-macie)

---

## Licença

Este projeto é de uso educacional e analítico.  
Fonte dos dados: [World Food Programme - WFP](https://data.humdata.org/dataset/wfp-food-prices-for-mozambique).

---
