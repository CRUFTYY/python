import pygame

# Inicializar pygame
pygame.init()

# Establecer tamaño de la ventana
window_size = (300, 300)

# Crear ventana
screen = pygame.display.set_mode(window_size)

# Poner título a la ventana
pygame.display.set_caption("Tateti")

# Variables para el tamaño de las casillas
box_size = 100

# Bucle del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Dibujar tablero
    for i in range(3):
        for j in range(3):
            pygame.draw.rect(screen, (255, 255, 255), (i*box_size, j*box_size, box_size, box_size), 2)

    # Actualizar pantalla
    pygame.display.flip()

# Finalizar pygame
pygame.quit()
