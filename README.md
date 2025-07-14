
# 📊 Previsão de Preços Agrícolas em Moçambique

Este projeto utiliza Machine Learning para prever os preços de produtos agrícolas em Moçambique com base em dados históricos da WFP (World Food Programme). Ele inclui pré-processamento, modelagem, visualização interativa em Streamlit e integração com Power BI.

---

## 🚀 Objetivo

- Ajudar agricultores, analistas e gestores públicos a prever tendências de preços agrícolas
- Utilizar dados reais e públicos para desenvolver um modelo robusto e prático
- Fornecer uma aplicação interativa para previsões futuras

---

## 🧠 Tecnologias Utilizadas

- `Python`
- `Pandas`, `scikit-learn`, `XGBoost`, `Joblib`
- `Streamlit` (interface web)
- `Power BI` (dashboard)
- `Google Drive` (armazenamento do modelo)
- `Git & GitHub` (versionamento)

---

## 📦 Download do Modelo Treinado

Devido ao limite de 100MB do GitHub, o modelo treinado (`modelo_rf.pkl`) foi armazenado externamente.

📥 **[Clique aqui para acessar a pasta `modelo` no Google Drive](https://drive.google.com/drive/folders/1_LDhv1TXYSrMF7V6q8-gncyUc6nfyXYa?usp=drive_link)**

> Após o download, coloque o arquivo `modelo_rf.pkl` dentro da pasta:

```
/modelo/modelo_rf.pkl
```

---

## ⚙️ Como Rodar Localmente

1. Clone este repositório:

```bash
git clone https://github.com/Shelzia/Previsao_Precos_Agricolas.git
cd Previsao_Precos_Agricolas
```

2. Crie e ative um ambiente virtual (opcional, mas recomendado):

```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Coloque o modelo na pasta `modelo/` (como explicado acima)

5. Inicie o app Streamlit:

```bash
streamlit run app_streamlit.py
```

---

## 📊 Power BI Dashboard

O projeto inclui um dataset limpo (`PowerBI/precos_agricolas_powerbi.csv`) para visualizações interativas no Power BI, destacando:

- Evolução mensal de preços
- Diferença entre províncias e produtos
- Tendências anuais

---

## 📎 Estrutura do Projeto

```
📁 data/
   └── wfp_food_prices_moz.csv
📁 modelo/
   └── modelo_rf.pkl (baixar via link)
📁 notebooks/
   └── 04_Prevendo_Precos.ipynb
📁 PowerBI/
   └── precos_agricolas_powerbi.csv
📁 apresentacoes/
   └── Apresentacao_Stakeholders.pptx
📄 app_streamlit.py
📄 requirements.txt
📄 README.md
```

---

## 👩🏽‍💻 Autor(a)

**Shelzia Macie**  
📍 Maputo, Moçambique  
💼 Cientista de Dados | Analista de BI  
🔗 [LinkedIn](https://www.linkedin.com/in/shelzia-macie)

---

## 📃 Licença

Este projeto é de uso educacional e analítico. Dados cedidos pela WFP.

---
