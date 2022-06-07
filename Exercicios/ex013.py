num = int(input("Lança um numero: "))

print(f"{num} não é? deixe-me ver isso aqui...")
print(f"Unidade: {num // 1 % 10}")
print(f"Dezena {num // 10 % 10}")
print(f"Centena {num // 100 % 10}")
print(f"Milhar {num // 100 % 10}")

print("End of transmision.")
