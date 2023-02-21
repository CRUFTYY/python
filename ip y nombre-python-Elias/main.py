import socket
hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
print("El nombre de tu computadora es:"+ hostname)
print("La direccion de ip es :"+ ip)
