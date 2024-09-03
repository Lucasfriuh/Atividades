# Solicita o texto
texto = input("Informe o texto: ")

# Inicializa contadores
contador = 0
existe_letra_a = False

# Verifica a existência da letra 'a' ou 'A' e conta a quantidade
for c in texto:
    if c == 'a' or c == 'A':
        existe_letra_a = True
        contador += 1

# Resultados
if existe_letra_a:
    print(f"A letra 'a' aparece {contador} vezes no texto.")
else:
    print("A letra 'a' não aparece no texto.")
