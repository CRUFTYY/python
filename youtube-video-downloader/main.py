from pytube import YouTube

def descargar_video():
    try:
        # Solicitar al usuario la URL del video
        url = input("Ingrese la URL del video de YouTube: ")

        # Crear un objeto YouTube
        video = YouTube(url)

        # Seleccionar la corriente con la mayor resolución disponible
        stream = video.streams.get_highest_resolution()

        # Solicitar al usuario la ubicación para guardar el video
        directorio_destino = input("Ingrese la ubicación para guardar el video (deje en blanco para usar el directorio actual): ")
        directorio_destino = directorio_destino.strip()  # Eliminar posibles espacios en blanco al inicio y al final

        if not directorio_destino:
            directorio_destino = "."  # Usar el directorio actual si no se proporciona ninguno

        # Descargar el video
        print(f"Descargando video: {video.title}...")
        stream.download(output_path=directorio_destino)
        print(f"Descarga completada. El video se guardó en: {directorio_destino}/{video.title}.mp4")

    except Exception as e:
        print(f"Error: {e}")

# Ejecutar la función
descargar_video()
