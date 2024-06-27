'''
Faça um programa em python que abra e reproduza o áudio de um arquivo mp3.
'''
#Solução dada pelo Chat GPT, porém mais difícil
import pygame
pygame.init()
mp3 = "c:/Users/Wesley 1/OneDrive/Área de Trabalho/Curso em Vídeo/Acalanto.mp3"
pygame.mixer.music.load(mp3)
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():pygame.time.Clock().tick(10)
pygame.quit