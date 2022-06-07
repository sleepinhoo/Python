#par ou impar
num = int(input("Qual é o número? "))
obj_num = num % 2 # vendo qual é o resto da divisão do numero por 2

if obj_num == 0: 
    print("É par :)")
else:
    print("É impar :)")
    
print("End of transmission...")