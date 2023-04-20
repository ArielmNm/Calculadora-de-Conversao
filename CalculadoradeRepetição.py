medidas = ["bit", "byte", "kilobyte", "megabyte", "gigabyte","terabyte","petabyte"]

valoratual = int(input("Escolha o Valor a ser convertido:"))

unid_atual = input("Escolha a unidade de medida:")

unid_final = input("Escolha a unidade de medida:")

while unid_atual not in medidas :
    print("Unidade não existente, tente novamente!:")
    unid_atual = input()

while unid_final not in medidas :
    print("Unidade não existente, tente novamente!:")
    unid_final = input()

def conversao (valoratual, unid_atual, unid_final):
    valor_final = valoratual
    if unid_atual == 'bit':
        valor_final = valor_final/8
        unid_atual = 'byte'

    if medidas.index(unid_atual)<medidas.index(unid_final):
        for i in range(medidas.index(unid_atual),medidas.index(unid_final)):
            valor_final=valor_final/1024    

    else:
        for i in range (medidas.index(unid_atual), medidas.index(unid_final),-1):
            valor_final = valor_final *1024
        if unid_atual == 'bit':
            valor_final = (valor_final/1024)*8
    print(valor_final)