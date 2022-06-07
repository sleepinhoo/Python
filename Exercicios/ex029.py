# aplicador de multa
# kilometragem: 80km
# valor por kilomretro excedido: 7.00

print("OPA meu jovem, cuidado com a velocidade!")
km = float(input("Ovo ter que conferir se vc passou da velocidade, me informe o a kilometragem por favor: "))

vl = km - 80.0

if vl < 1.0 :
    print("Tá limpo meu rei, pode passar.")
else :
    mt = vl * 7
    print("Tá correndo mermão?")
    print(f"Ovo ter que te aplicar uma multa de R${mt}")
    
print("End of transmission...")