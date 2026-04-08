lista = []
for i in range(10):
    item = int(input(f"Digite o item {i+1}: "))
    lista.append(item)

print("Lista final:", lista)

maiorvalor = max(lista)
print("O maior valor da lista é:", maiorvalor)
menorvalor = min(lista)
print("O menor valor da lista é:", menorvalor)
media = sum(lista) / len(lista)
print("A média dos valores da lista é:", media)
acimadamedia = [x for x in lista if x > media]
print("Valores acima da média:", acimadamedia)
