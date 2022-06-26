# jooj da adivinhação

import random as rdm #biblioteca para randomizar numeros

num = rdm.randint(1,6)

print("Ovo pensar num número de 1 a 6, e vc tenta adivinar qual foi")
r = int(input("Pronto, em qual número eu pensei? "))

if r == num :
    print("\033[0;34mParabens, vc me venceu!\033[m")
else:
    print(f"\033[7;31mHá otário, vc perdeu\033[m, o número era o \033[0;32m{num}\033[m")