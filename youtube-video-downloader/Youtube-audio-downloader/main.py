from pytube import YouTube
import os

def descargar_audio_youtube(url, directorio_descarga=None):
    try:
        # Crear un objeto YouTube
        video = YouTube(url)

        # Seleccionar la corriente de audio
        audio_stream = video.streams.filter(only_audio=True).first()

        # Obtener el título del video
        video_title = video.title

        # Establecer el directorio de descarga
        if directorio_descarga:
            if not os.path.exists(directorio_descarga):
                os.makedirs(directorio_descarga)
        else:
            directorio_descarga = "A:\\Videos\\Youtube videos download"
            if not os.path.exists(directorio_descarga):
                os.makedirs(directorio_descarga)

        # Descargar el audio en el directorio especificado
        print(f"Descargando audio de '{video_title}'...")
        video_title += f"{video_title}.mp3"
        ruta_descarga = os.path.join(directorio_descarga, f"{video_title}.mp3")
        audio_stream.download(output_path=directorio_descarga, filename=video_title)

        print(f"Audio descargado y guardado como '{video_title}' en {ruta_descarga}")

    except Exception as e:
        print(f"Ocurrió un error: {str(e)}")

if __name__ == "__main__":
    # Pedir al usuario que ingrese el enlace de YouTube
    enlace_youtube = input("Ingrese el enlace de YouTube del video que desea descargar: ")

    # Pedir al usuario que elija la ruta de descarga
    ruta_descarga = input("Ingrese la ruta de descarga (deje en blanco para usar la ruta predeterminada): ")

    # Llamar a la función para descargar el audio
    descargar_audio_youtube(enlace_youtube, ruta_descarga)
