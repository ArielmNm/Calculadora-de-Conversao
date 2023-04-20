medidas = ["bit", "byte", "kilobyte", "megabyte", "gigabyte","terabyte","petabyte"]

def conversor_medidas (numero,unidorigem,unidsaida):
    indice_Origem = medidas.index(unidorigem)
    indice_saida = medidas.index(unidsaida)
    fator = 1024** (indice_saida - indice_Origem)
    return numero * fator

valor = int(input("Escolha o Valor a ser convertido:"))

unidorigem = input("Escolha a unidade de medida:(Gigabyte):")

while unidorigem not in medidas :
    print("Unidade não existente, tente novamente!: ")
    unid= input()

unidsaida = input("Escolha a unidade de medida:(Terabyte):")
while unidsaida not in medidas :
    print("Unidade não existente, tente novamente!: ")
    unid= input()

while medidas.index(unidorigem) < medidas.index(unidsaida):
    nova_unidade = medidas[medidas.index(unidorigem) + 1]
    quantidade = conversor_medidas(quantidade, unidorigem, nova_unidade)
    unidade_origem = nova_unidade

    print("O resultado é:", quantidade, unidade_origem)