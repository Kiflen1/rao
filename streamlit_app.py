# streamlit_app.py

import streamlit as st
import requests

st.set_page_config(page_title="Gerar PIX", layout="centered")

st.title("💸 Gerar Código PIX 🔥")

valor = st.number_input("Digite o valor (R$):", min_value=0.01, step=0.01)

if st.button("Gerar PIX"):
    with st.spinner("Gerando código..."):
        payload = {
            "value": valor,
            "key": "contato@pixvoluti.com.br",  # Chave PIX cadastrada na PushingPay
            "name": "Grupo VIP",
            "city": "Sao Paulo",
            "external_reference": "pedido-001",
            "webhook_url": ""  # pode deixar vazio por enquanto
        }

        headers = {
            "Authorization": "Bearer 24803|KwXSjzStpqWESR4MYZJ9EdlgmRsecfD5ohgrZzXe9adbcb97"
        }

        r = requests.post("https://api.pushingpay.com/api/v1/pix/charge", json=payload, headers=headers)

        if r.status_code == 201:
            data = r.json()
            st.success("✅ Código gerado com sucesso!")
            st.text_area("Código PIX Copia e Cola:", data['pix']['copyPaste'], height=150)
            st.markdown(f"🔗 QR Code: [Clique aqui]({data['pix']['qrCode']})")
        else:
            st.error("❌ Erro ao gerar PIX.")
            st.json(r.json())