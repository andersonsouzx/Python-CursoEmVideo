import pygame
import time

# Inicializa o mixer do Pygame
pygame.init()
pygame.mixer.init()

# Carrega e toca a música
pygame.mixer.music.load('Ex021.mp3')
pygame.mixer.music.play()

# Mantém o programa em execução enquanto a música toca
while pygame.mixer.music.get_busy():
    time.sleep(1)  # Espera 1 segundo antes de verificar novamente

print("Música terminada")
