import streamlit as st
import random
import datetime

# Configuración básica
MODELOS = ['Modelo 1', 'Modelo 2', 'Modelo 3', 'Modelo 4', 'Modelo 5']

# Configuración de la página
st.set_page_config(page_title="Chatbot de IA", page_icon="🤖", layout="centered")

# Función para configurar la página
def configurar_pagina():
    st.title("Chatbot de IA")
    st.sidebar.title("Configuración de la IA")
    modelo_seleccionado = st.sidebar.selectbox('Elegí un Modelo', options=MODELOS, index=0)
    return modelo_seleccionado

# Configuración de la aplicación
modelo = configurar_pagina()

# Función para generar respuestas del chatbot
def generar_respuesta(mensaje, modelo):
    if "crufty" in mensaje.lower():
        return "Crufty? El mejor de todos los tiempos."
    
    respuestas = {
        'Modelo 1': [
            f"Respuesta del {modelo}: Entiendo que quieres saber sobre '{mensaje}'. Aquí tienes una respuesta simple.",
            f"{mensaje} es un tema interesante. Te recomiendo investigar más sobre ello.",
            f"No estoy seguro de cómo responder a '{mensaje}', pero puedo ayudarte con otra cosa.",
            f"El tema '{mensaje}' tiene muchas aristas. ¿Te gustaría profundizar en alguna en particular?",
            f"Para '{mensaje}', te sugiero que revises algunas fuentes confiables."
        ],
        'Modelo 2': [
            f"Respuesta del {modelo}: Interesante que digas '{mensaje}'. Aquí hay algo más elaborado.",
            f"{mensaje} es un concepto complejo. ¿Has considerado leer sobre ello?",
            f"Para '{mensaje}', podría ser útil revisar recursos específicos.",
            f"Sobre '{mensaje}', aquí tienes un análisis que podrías encontrar útil.",
            f"¿Has escuchado hablar sobre los diferentes enfoques respecto a '{mensaje}'?"
        ],
        'Modelo 3': [
            f"Respuesta del {modelo}: Ah, '{mensaje}' es un tema fascinante. Aquí está una respuesta detallada.",
            f"Sobre '{mensaje}', te sugiero que investigues los siguientes puntos.",
            f"Si estás buscando información sobre '{mensaje}', aquí hay algunos datos que podrían interesarte.",
            f"Al hablar de '{mensaje}', es crucial considerar diferentes perspectivas.",
            f"Hay muchos estudios sobre '{mensaje}'. ¿Te gustaría saber más sobre alguno en particular?"
        ],
        'Modelo 4': [
            f"Respuesta del {modelo}: En relación a '{mensaje}', considera los siguientes aspectos.",
            f"Es interesante que menciones '{mensaje}', porque hay diversas opiniones al respecto.",
            f"A menudo, cuando se discute sobre '{mensaje}', se ignoran ciertos factores importantes.",
            f"Sobre el tema de '{mensaje}', hay un debate activo que podrías explorar.",
            f"Me gustaría recomendarte algunos artículos que discuten '{mensaje}' más a fondo."
        ],
        'Modelo 5': [
            f"Respuesta del {modelo}: La perspectiva sobre '{mensaje}' es muy amplia.",
            f"En el contexto de '{mensaje}', aquí hay algunas ideas que podrían ser útiles.",
            f"Muchos expertos tienen puntos de vista diferentes sobre '{mensaje}'. ¿Te gustaría saber más?",
            f"Si consideras '{mensaje}', es esencial mirar todos los ángulos posibles.",
            f"En general, la discusión sobre '{mensaje}' incluye una variedad de opiniones."
        ],
    }
    return random.choice(respuestas[modelo])

# Lista para almacenar mensajes
if 'historial' not in st.session_state:
    st.session_state.historial = []

# Mensaje del usuario
mensaje = st.chat_input("Escribí tu mensaje:")

# Mostrar la respuesta si hay un mensaje
if mensaje:
    respuesta = generar_respuesta(mensaje, modelo)
    # Guardar el mensaje y respuesta en el historial
    st.session_state.historial.append((datetime.datetime.now(), mensaje, respuesta))
    st.write(respuesta)

# Mostrar el historial de conversaciones
st.sidebar.header("Historial de Conversaciones")
if st.session_state.historial:
    for fecha, msg, resp in st.session_state.historial:
        st.sidebar.write(f"**{fecha.strftime('%Y-%m-%d %H:%M:%S')}**")
        st.sidebar.write(f"**Tú:** {msg}")
        st.sidebar.write(f"**Bot:** {resp}")
        st.sidebar.write("---")

# Sección de consejos
st.sidebar.header("Consejos de Uso")
st.sidebar.write("1. Puedes preguntar sobre cualquier tema.")
st.sidebar.write("2. Usa palabras clave para obtener respuestas más precisas.")
st.sidebar.write("3. Si necesitas ayuda, no dudes en preguntar.")
st.sidebar.write("4. Recuerda que este es un chatbot, ¡puede que no tenga todas las respuestas!")

# Funciones adicionales
def mostrar_informacion_adicional():
    st.sidebar.header("Información Adicional")
    st.sidebar.write("Este chatbot está diseñado para interactuar de manera simple.")
    st.sidebar.write("Puedes elegir entre diferentes modelos para ver distintas respuestas.")
    st.sidebar.write("¡Diviértete chateando!")

# Llamar a la función de información adicional
mostrar_informacion_adicional()

# Función para resetear el historial
def resetear_historial():
    if st.sidebar.button("Resetear Historial"):
        st.session_state.historial = []
        st.success("Historial de conversaciones reseteado.")

# Llamar a la función de resetear historial
resetear_historial()

# Estadísticas de uso
def mostrar_estadisticas():
    total_mensajes = len(st.session_state.historial)
    st.sidebar.header("Estadísticas")
    st.sidebar.write(f"Total de mensajes enviados: {total_mensajes}")
    if total_mensajes > 0:
        st.sidebar.write(f"Último mensaje: '{st.session_state.historial[-1][1]}'")
    else:
        st.sidebar.write("Aún no has enviado mensajes.")

# Llamar a la función de estadísticas
mostrar_estadisticas()
