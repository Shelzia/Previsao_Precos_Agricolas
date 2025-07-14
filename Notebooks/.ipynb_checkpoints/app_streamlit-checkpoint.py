import streamlit as st
import pandas as pd
import joblib

# Loading model e encoders
rf_model = joblib.load("model/modelo_rf.pkl")
label_encoders = joblib.load("model/label_encoders.pkl")

st.title("📈 Previsão de Preços Agrícolas - Moçambique") 
st.markdown("Preve o preço de produtos agrícolas com base em localização, data e tipo de produto.")

# User Inputs 
province = st.selectbox("Província", label_encoders['province'].classes_)
district = st.selectbox("Distrito", label_encoders['district'].classes_)
market = st.selectbox("Mercado", label_encoders['market'].classes_)
category = st.selectbox("Categoria", label_encoders['category'].classes_)
commodity = st.selectbox("Produto (Commodity)", label_encoders['commodity'].classes_)
unit = st.selectbox("Unidade", label_encoders['unit'].classes_)
pricetype = st.selectbox("Tipo de Preço", label_encoders['pricetype'].classes_)
year = st.slider("Ano da Previsão", 2024, 2030, 2026)
month = st.slider("Mês", 1, 12, 1)

# Transform inputs
entrada = {
    'province': label_encoders['province'].transform([province])[0],
    'district': label_encoders['district'].transform([district])[0],
    'market': label_encoders['market'].transform([market])[0],
    'category': label_encoders['category'].transform([category])[0],
    'commodity': label_encoders['commodity'].transform([commodity])[0],
    'unit': label_encoders['unit'].transform([unit])[0],
    'pricetype': label_encoders['pricetype'].transform([pricetype])[0],
    'month': month,
    'year': year,
    'month_id': (year - 1992) * 12 + month  # Ajustar com base nos dados históricos
}

entrada_df = pd.DataFrame([entrada])

# Forecast Prices
if st.button("Prever Preço"):
    preco = rf_model.predict(entrada_df)[0]
    st.success(f"Preço Previsto: {preco:.2f} MZN")
