def CriaMatriz(tamanho):
    A = []
    for i in range(tamanho):
        linha = []
        for j in range(tamanho):
            valor = int(input(f"A[{i}][{j}] = "))
            linha.append(valor)
        A.append(linha)
    return A

def soma_matrizes(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        return None
    C = []
    for i in range(len(A)):
        linha = []
        for j in range(len(A[0])):
            linha.append(A[i][j] + B[i][j])
        C.append(linha)
    return C

def subtrai_matrizes(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        return None
    C = []
    for i in range(len(A)):
        linha = []
        for j in range(len(A[0])):
            linha.append(A[i][j] - B[i][j])
        C.append(linha)
    return C

tamanhoM = int(input("Quantas linhas e colunas tem sua matriz quadrada? "))
matriz = CriaMatriz(tamanhoM)
print(matriz)

print("Agora vamos somar e subtrair duas matrizes, crie outra matriz para somar e subtrair com a anterior. Quais são os elementos da sua segunda matriz?")
matriz2 = CriaMatriz(tamanhoM)

resultado_soma = soma_matrizes(matriz, matriz2)
print("A soma das matrizes é:", resultado_soma)

resultado_sub = subtrai_matrizes(matriz, matriz2)
print("A subtração das matrizes é:", resultado_sub)
