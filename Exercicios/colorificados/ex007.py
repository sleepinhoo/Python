print("Aviso: use o ponto final em vez de vírgula para representar números decimais.")

nota1 = float(input("\033[0;35mDigite nota 1:/033[m "))
nota2 = float(input("Digite a nota 2: "))

med = (nota1 + nota2) / 2

print(f"A média do aluno foi \033[4;34m{med}\033[m")
