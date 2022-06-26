# aplicador de multa
# kilometragem: 80km
# valor por kilomretro excedido: 7.00

print("OPA meu jovem, cuidado com a velocidade!")
km = float(input("Ovo ter que conferir se vc passou da velocidade, me informe o a kilometragem por favor: "))

vl = km - 80.0

if vl < 1.0 :
    print("\033[0;30;42mTá limpo meu rei, pode passar.\033[m")
else :
    mt = vl * 7
    print("\033[0;30;43mTá correndo mermão?\033[m")
    print(f"Ovo ter que te aplicar uma \033[7;31mmulta de R${mt}\033[m")
    
print("End of transmission...")