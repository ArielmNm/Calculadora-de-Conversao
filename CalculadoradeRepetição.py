medidas = ["bit", "byte", "kilobyte", "megabyte", "gigabyte","terabyte","petabyte"]

print("Escolha a unidade de medida:(Gigabyte):")
unid1 = input()
print(unid1)

print("Escolha a unidade de medida:(Terabyte):")
unid2 = input()
print(unid2)

def conversor_medidas (numero,unidOrigem,unidSaida):
    indice_Origem = medidas.index(unidOrigem)
    indice_saida = medidas.index(unidSaida)
    fator = 1024** (indice_saida - indice_Origem)
    return numero * fator

valor = input("Escolha o Valor a ser convertido:")


