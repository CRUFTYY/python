import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Configura tus credenciales de Spotify
client_id = '05433e3e0cf74be18a7ce106735e20c3'
client_secret = 'f51a16328944432e9a82a1850e005726'

# Configura las credenciales del cliente
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)

# Inicia la instancia de Spotipy
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# URL de la playlist de Spotify
playlist_url = 'https://open.spotify.com/playlist/5UuJ23cLNkesN7VKdOxN2N'

# Obtiene la ID de la playlist
playlist_id = playlist_url.split('/')[-1]

# Lista para almacenar los nombres de los álbumes
album_names = []

# Variable para realizar solicitudes adicionales
offset = 0
limit = 100  # Cantidad de canciones por solicitud

# Realiza solicitudes múltiples para obtener todas las canciones
while True:
    results = sp.playlist_tracks(playlist_id, offset=offset, limit=limit)

    for track in results['items']:
        album_name = track['track']['album']['name']
        album_names.append(album_name)

    offset += limit

    if len(results['items']) < limit:
        # Si no hay más canciones, sal del bucle
        break

# Nombre del archivo de texto donde se guardarán los nombres de los álbumes
file_name = 'C:\\Users\\cruft\\OneDrive\\Escritorio\\album_names.txt'

# Escribe los nombres de los álbumes en el archivo de texto
with open(file_name, 'w', encoding='utf-8') as file:
    for album_name in album_names:
        file.write(album_name + '\n')

print(f'Se han guardado los nombres de los álbumes en {file_name}')
