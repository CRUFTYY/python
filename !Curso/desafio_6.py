import streamlit as st
import requests
import datetime  


GROQ_API_URL = "https://api.groq.com/v1/query"
API_KEY = "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"

st.set_page_config(page_title="ELÍAS IA", page_icon="😎", layout="centered")


def configurar_pagina():
    st.title("Chatbot de IA")
    st.sidebar.title("Configuración de la IA")
    st.sidebar.write("Modelo seleccionado: Groq")
    return "Groq"

modelo = configurar_pagina()


def generar_respuesta_groq(mensaje):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "query": mensaje,
        "temperature": 0.7
    }
    response = requests.post(GROQ_API_URL, headers=headers, json=data)
    if response.status_code == 200:
        return response.json().get("answer", "Lo siento, no pude obtener una respuesta.")
    else:
        return "Error en la API de Groq."


def generar_respuesta(mensaje):
    if "crufty" in mensaje.lower():
        st.success("Felicitaciones, has mencionado a el mejor de la historia.")
        return "Crufty? El mejor de todos los tiempos."
    
    return generar_respuesta_groq(mensaje)

if 'historial' not in st.session_state:
    st.session_state.historial = []


mensaje = st.chat_input("Escribí tu mensaje:")

if mensaje:
    respuesta = generar_respuesta(mensaje)
    st.session_state.historial.append((datetime.datetime.now(), mensaje, respuesta))
    st.write(respuesta)

# Historial y sidebar
st.sidebar.header("Historial de Conversaciones")
if st.session_state.historial:
    for fecha, msg, resp in st.session_state.historial:
        st.sidebar.write(f"**{fecha.strftime('%Y-%m-%d %H:%M:%S')}**")
        st.sidebar.write(f"**Tú:** {msg}")
        st.sidebar.write(f"**Bot:** {resp}")
        st.sidebar.write("---")

st.sidebar.header("Consejos de Uso")
st.sidebar.write("1. Podes preguntar sobre cualquier tema.")
st.sidebar.write("2. Usa palabras clave para obtener respuestas más precisas.")
st.sidebar.write("3. Si necesitas ayuda, no dudes en preguntar.")
st.sidebar.write("4. Recordá que es un chatbot hecho por el genio de CRUFTY")

# Información adicional
def mostrar_informacion_adicional():
    st.sidebar.header("Información Adicional")
    st.sidebar.write("Este chatbot está diseñado por CRUFTY")
    st.sidebar.write("Cuidadito con lo que le preguntás a la IA.")

mostrar_informacion_adicional()

# Resetear historial
def resetear_historial():
    if st.sidebar.button("Resetear Historial"):
        st.session_state.historial = []
        st.success("El historial de conversaciones se reseteó. Casi te atrapa la policía.")

resetear_historial()

# Mostrar estadísticas
def mostrar_estadisticas():
    total_mensajes = len(st.session_state.historial)
    st.sidebar.header("Estadísticas")
    st.sidebar.write(f"Total de mensajes enviados: {total_mensajes}")
    if total_mensajes > 0:
        st.sidebar.write(f"Último mensaje: '{st.session_state.historial[-1][1]}'")
    else:
        st.sidebar.write("No mandaste ningún mensaje todavía.")

mostrar_estadisticas()
