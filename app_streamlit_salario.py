import streamlit as st
import json
import requests

# Título da aplicação
st.title("Modelo de predição de salário")

# Inputs do usuário
st.write("Quantos meses o profissional está na empresa?")
tempo_na_empresa = st.slider("Meses", min_value= 1, max_value= 120, value= 60, step= 1)

st.write("Qual o nível do profissional na empresa?")
nivel_na_empresa = st.slider("Nível", min_value= 1, max_value= 10, value= 5, step= 1)

# Preparar dados para API
input_features = {'tempo_na_empresa': tempo_na_empresa,
                  'nivel_na_empresa': nivel_na_empresa
                  }

# Criar um botao e capturar um evento do mesmo para disparar a API
if st.button('Estimar salário'):
    response = requests.post(url= "http://127.0.0.1:8000/predict", data= json.dumps(input_features))
    response_json = json.loads(response.text)

    salario_em_reais = round(response_json['salario_em_reais'], 2)
    st.subheader(f"O salário estimado é de R$ {salario_em_reais}")