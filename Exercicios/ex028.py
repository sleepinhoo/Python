# jooj da adivinhação

import random as rdm #biblioteca para randomizar numeros

num = rdm.randint(1,6)

print("Ovo pensar num número de 1 a 6, e vc tenta adivinar qual foi")
r = int(input("Pronto, em qual número eu pensei? "))

if r == num :
    print("Parabens, vc me venceu!")
else:
    print(f"Há otário, vc perdeu, o número era o {num}")