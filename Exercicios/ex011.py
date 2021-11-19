nome =  str(input("Digite o seu nome: ")).strip() # Use o .strip() para eliminar os espacos antes e depois de uma cadeia de caracteres, isso eh util para nomes de pessoas.

print("Um momento, estamos analisando seu nome...")
print(f"Seu nome no formato original e: {nome}")
print(f"Em mauisculas fica assim: {nome.upper()}") #variavel.upper() deixa todos os caracteres da cadeia em maiusculo
print(f"Em minusculas, fica assim: {nome.lower()}") #variavel.lower() deixa todas as cadeias de caracteres em minusculo
print("Seu nome tem {} letras.".format(len(nome) - nome.count(" "))) # len(variavel) eh usado para contar quantos caracteres tem em uma cadeia (contando os espacos)
# para tirar os espacos, basta subtrair len(variavel) - nome.count(" ") >>> ele vai contar quantos desse caractere colocado entre parenteses tem na cadeia (espaco conta), e vai subtrair no resultado.
print("Seu primeiro nome tem {}".format(nome.find(" "))) #esse nome.find(" "), ele vai achar o primeiro espaco e vai cortar ele e todos os caracteres em diante, util para achar o primeiro nome de uma pessoa.
split = nome.split()
print(f"E antes que eu me esqueca, seu primeiro nome eh {split[0]}")
