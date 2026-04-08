inicio = int(input("Digite o valor inicial: "))
fim = int(input("Digite o valor final: "))
n = 0

if inicio > fim:
    print("O valor inicial deve ser menor ou igual ao valor final.")
else:
    primeiro_par = inicio if inicio % 2 == 0 else inicio + 1
    ultimo_par = fim if fim % 2 == 0 else fim - 1
    for i in range(primeiro_par, ultimo_par + 1, 2):
        print(i)
        n = n+1
print("O total de numeros pares encontrados foi:", n)