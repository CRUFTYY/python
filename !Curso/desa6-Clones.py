import streamlit as st
import datetime
from groq import Groq

# Obtener la API Key desde los secretos de Streamlit Cloud
API_KEY = "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"

# Crea el cliente de Groq con la API Key
client = Groq(api_key=API_KEY)

# Configuración de la página
st.set_page_config(page_title="ELÍAS IA", page_icon="😎", layout="centered")

def configurar_pagina():
    st.title("Chatbot de IA")
    st.sidebar.title("Configuración de la IA")
    st.sidebar.write("Modelo seleccionado: Groq")
    return "Groq"

modelo = configurar_pagina()

# Función para generar una respuesta utilizando la API de Groq
def generar_respuesta_groq(mensaje):
    try:
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": mensaje}],
            model="llama3-8b-8192",  # Asegúrate de usar el modelo correcto
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        st.error(f"Error al obtener respuesta de Groq: {e}")
        return "Error en la API de Groq."

# Función principal para generar la respuesta del chatbot
def generar_respuesta(mensaje):
    if "crufty" in mensaje.lower():
        st.success("Felicitaciones, has mencionado al mejor de la historia.")
        return "Crufty? El mejor de todos los tiempos."
    
    return generar_respuesta_groq(mensaje)

# Manejar el historial de conversaciones en la sesión
if 'historial' not in st.session_state:
    st.session_state.historial = []

# Entrada de texto para el mensaje del usuario
mensaje = st.chat_input("Escribí tu mensaje:")

if mensaje:
    respuesta = generar_respuesta(mensaje)
    st.session_state.historial.append((datetime.datetime.now(), mensaje, respuesta))
    st.write(respuesta)

# Mostrar historial de conversaciones en la sidebar
st.sidebar.header("Historial de Conversaciones")
if st.session_state.historial:
    for fecha, msg, resp in st.session_state.historial:
        st.sidebar.write(f"**{fecha.strftime('%Y-%m-%d %H:%M:%S')}**")
        st.sidebar.write(f"**Tú:** {msg}")
        st.sidebar.write(f"**Bot:** {resp}")
        st.sidebar.write("---")

# Consejos de uso en la sidebar
st.sidebar.header("Consejos de Uso")
st.sidebar.write("1. Podes preguntar sobre cualquier tema.")
st.sidebar.write("2. Usa palabras clave para obtener respuestas más precisas.")
st.sidebar.write("3. Si necesitas ayuda, no dudes en preguntar.")
st.sidebar.write("4. Recordá que es un chatbot hecho por el genio de CRUFTY.")

# Información adicional en la sidebar
def mostrar_informacion_adicional():
    st.sidebar.header("Información Adicional")
    st.sidebar.write("Este chatbot está diseñado por CRUFTY.")
    st.sidebar.write("Cuidadito con lo que le preguntás a la IA.")

mostrar_informacion_adicional()

# Opción para resetear el historial de conversaciones
def resetear_historial():
    if st.sidebar.button("Resetear Historial"):
        st.session_state.historial = []
        st.success("El historial de conversaciones se reseteó. Casi te atrapa la policía.")

resetear_historial()

# Mostrar estadísticas en la sidebar
def mostrar_estadisticas():
    total_mensajes = len(st.session_state.historial)
    st.sidebar.header("Estadísticas")
    st.sidebar.write(f"Total de mensajes enviados: {total_mensajes}")
    if total_mensajes > 0:
        st.sidebar.write(f"Último mensaje: '{st.session_state.historial[-1][1]}'")
    else:
        st.sidebar.write("No mandaste ningún mensaje todavía.")

mostrar_estadisticas()
