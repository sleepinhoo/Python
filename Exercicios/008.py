print("Aviso: Use o ponto final em vez de vírgulas para representar números decimais")
print("Não é necessário colocar a unidade de medida no final do valor")

medida = float(input("Digite uma distancia em metros: "))

print(f"A medida {medida}m corresponde a:")
print(f"{medida / 1000}km")
print(f"{medida / 100}hm")
print(f"{medida / 10}dam")
print(f"{medida * 10}dm")
print(f"{medida * 100}cm")
print(f"{medida * 1000}mm")
