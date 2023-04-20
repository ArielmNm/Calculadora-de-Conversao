from calculadora import converterStringParaFloat, bitParaByte, byteParaBit, byteParaKilobyte, KilobyteParabyte, KilobyteParaMegabyte, MegabyteParaKilobyte, MegabyteParaGigabyte, GigabyteParaMegabyte, GigabyteParaTerabyte, TerabyteParaGigabyte, TerabyteParaPetabyte, PetabyteParaTerabyte

print ( '-Write 1 to: Bit to Byte  \n -Write 2 to: Byte to bit \n -Write 3 to: Byte to Kilobyte \n -Write 4 to: Kilobyte to Byte \n -Write 5 to: kilobyte to Megabyte \n -Write 6 to: Megabyte to Kilobyte \n -Write 7 to: Megabyte to Gigabyte \n -Write 8 to: Gigabyte to Megabyte \n -Write 9 to: Gigabyte to Terabyte \n -Write 10 to:Terabyte to Gigabyte \n -Write 11 to: Terabyte to Petabyte \n -Write 12 to:Petabyte to Terabyte')
funcEscolha = input()

if(funcEscolha == '1'):
    print("You chose the option 1")
    teclvalorAserconvertido = converterStringParaFloat(input())
    valorconvertido = bitParaByte(teclvalorAserconvertido)
    print(valorconvertido) 

elif(funcEscolha == '2'):
    print("You chose the option 2")
    teclvalorAserconvertido = converterStringParaFloat(input())
    valorconvertido = byteParaBit(teclvalorAserconvertido)
    print(valorconvertido)

elif(funcEscolha == '3'):
    print("You chose the option 3")
    teclvalorAserconvertido = converterStringParaFloat(input())
    valorconvertido = byteParaKilobyte(teclvalorAserconvertido)
    print(valorconvertido)

elif(funcEscolha == '4'):
    print("You chose the option 4")
    teclvalorAserconvertido = converterStringParaFloat(input())
    valorconvertido = KilobyteParabyte(teclvalorAserconvertido)
    print(valorconvertido)

elif(funcEscolha == '5'):
    print("You chose the option 5")
    teclvalorAserconvertido = converterStringParaFloat(input())
    valorconvertido = KilobyteParaMegabyte(teclvalorAserconvertido)
    print(valorconvertido)

elif(funcEscolha == '6'):
    print("You chose the option 6")
    teclvalorAserconvertido = converterStringParaFloat(input())
    valorconvertido = MegabyteParaKilobyte(teclvalorAserconvertido)
    print(valorconvertido)

elif(funcEscolha == '7'):
    print("You chose the option 7")
    teclvalorAserconvertido = converterStringParaFloat(input())
    valorconvertido = MegabyteParaGigabyte(teclvalorAserconvertido)
    print(valorconvertido)

elif(funcEscolha == '8'):
    print("You chose the option 8")
    teclvalorAserconvertido = converterStringParaFloat(input())
    valorconvertido = GigabyteParaMegabyte(teclvalorAserconvertido)
    print(valorconvertido)

elif(funcEscolha == '9'):
    print("You chose the option 9")
    teclvalorAserconvertido = converterStringParaFloat(input())
    valorconvertido = GigabyteParaTerabyte(teclvalorAserconvertido)
    print(valorconvertido)

elif(funcEscolha == '10'):
    print("You chose the option 10")
    teclvalorAserconvertido = converterStringParaFloat(input())
    valorconvertido = TerabyteParaGigabyte(teclvalorAserconvertido)
    print(valorconvertido)

elif(funcEscolha == '11'):
    print("You chose the option 11")
    teclvalorAserconvertido = converterStringParaFloat(input())
    valorconvertido = TerabyteParaPetabyte(teclvalorAserconvertido)
    print(valorconvertido)

elif(funcEscolha == '12'):
    print("You chose the option 12")
    teclvalorAserconvertido = converterStringParaFloat(input())
    valorconvertido = PetabyteParaTerabyte(teclvalorAserconvertido)
    print(valorconvertido)