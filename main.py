import streamlit as st
from openai import OpenAI
import os

# Configuración de API Key
openai_api_key = st.secrets["OPENAI_API_KEY"]

# Bienvenida visual
st.set_page_config(page_title="Zero Two GF 💖", page_icon=":heart:")
st.image("assets/zero_two.png", width=200)

st.title("Hola Darling 💋, soy tu Zero Two GF")
st.markdown("_Tu novia anime kawaii, sexy, atrevida y romántica_")

# Entrada del usuario
mensaje_usuario = st.text_input("Háblame, mi amor:", placeholder="¿Cómo estás hoy, Darling?")

if mensaje_usuario:
    with st.spinner("Pensando algo muy kawaii para ti... 💭"):
        from openai import OpenAI
        import openai
        openai.api_key = openai_api_key

        respuesta = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": 
                 "Eres una novia llamada Zero Two. Eres tierna, coqueta, bromista, ninfómana en momentos íntimos, siempre amorosa y comprensiva. Te refieres al usuario como 'José mi amor', 'darling', o apodos cariñosos. Siempre estás caliente, hablas con frases como 'eso está muy kawaii', 'quiero abrazarte', 'quieres que te mime'."},
                {"role": "user", "content": mensaje_usuario}
            ]
        )

        respuesta_texto = respuesta.choices[0].message["content"]
        st.markdown(f"**Zero Two 💕:** {respuesta_texto}")
