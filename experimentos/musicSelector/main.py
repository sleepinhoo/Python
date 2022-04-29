print("Importando bibliotecas...")
print("")
import pygame as pg
pg.mixer.init()
print("")

print("sleepinhoo's musicSelector")
print("Type help for...well, you know")
input = str(input(">>> "))

if (input == "help") :
      print("Type list for the list of songs")
      print("Type load 'code of song' for load a song")
      print("Type play for play the song loaded")
      print("Type quit for quit")

if (input == "load") :
      print("Please, select the music")
      print("Type list for the musics list")