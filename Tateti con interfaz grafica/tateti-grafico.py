import pygame

# Initialize pygame
pygame.init()

# Set the screen size
screen = pygame.display.set_mode((300, 300))

# Set the title of the window
pygame.display.set_caption("CRUFTY TIC TAC")

# Create a 2D array to store the state of the game
board = [[None, None, None], [None, None, None], [None, None, None]]

# Create a variable to store the current player
player = "X"

# Create a font for displaying the winner
font = pygame.font.Font(None, 66)

screen.fill((255, 255, 255)) # This set the color of the window

winner = None

filled_squares = 0

# Run the game loop
running = True
while running:
    for event in pygame.event.get():
        pygame.display.update()
        if event.type == pygame.QUIT:
            running = False

        # Check for mouse clicks
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Get the coordinates of the click
            x, y = event.pos
            # Calculate the row and column of the click
            row, col = y // 100, x // 100
            # Make a move if the square is empty
            if board[row][col] is None:
                board[row][col] = player
                player = "X" if player == "O" else "O"
    # Clear the screen
    screen.fill((255, 255, 255))
    # Draw the lines of the board
    for i in range(1, 3):
        pygame.draw.line(screen, (0, 0, 0), (100 * i, 0), (100 * i, 300))
        pygame.draw.line(screen, (0, 0, 0), (0, 100 * i), (300, 100 * i))

    # Draw the X's and O's
    for row in range(3):
        for col in range(3):
            if board[row][col] == "X":
                pygame.draw.line(screen, (255, 0, 0), (col * 100 + 10, row * 100 + 10), (col * 100 + 90, row * 100 + 90), 5)
                pygame.draw.line(screen, (255, 0, 0), (col * 100 + 90, row * 100 + 10), (col * 100 + 10, row * 100 + 90), 5)
            elif board[row][col] == "O":
                pygame.draw.circle(screen, (0, 0, 255), (col * 100 + 50, row * 100 + 50), 40, 5)

# Check for a winner
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] and board[row][0] is not None:
            winner = board[row][0]
            running = False
            break
    else:
        for col in range(3):
            if board[0][col] == board[1][col] == board[2][col] and board[0][col] is not None:
                winner = board[0][col]
                running = False
                break
# Check for diagonal wins (top-left to bottom-right)
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        winner = board[0][0]
    elif board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        winner = board[0][2]

    if winner is not None:
        winner_text = font.render(f"{winner} GANO!!", True, (255, 0, 0))
        screen.blit(winner_text, (100, 150))
        pygame.display.update()
        pygame.time.wait(3000)
        running = False

    if filled_squares == 9 and winner is None:
        winner_text = font.render("Empate!!", True, (0, 0, 0))
        screen.blit(winner_text, (100, 150))
        pygame.display.update()
        pygame.time.wait(3000)
        running = False
    


        
