# tip: a ocondição poderia ser escrita da forma reduzida >>> pr = dist * 0.50 if dist <= 200 else dist * 0.45 >>> use-a para códigos menores, caso contrário, use a versão tradicional, deixa o código mais bonito

dist = float(input("QUal é a distância da sua passagem? "))
print(f"Você está prestes a começar uma viagem de {dist}Km.")

if dist <= 200:
    pr = dist * 0.50
else:
    pr = dist * 0.45
    
print(f"O preço da sua passagem será de R${pr}")
