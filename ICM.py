"""
    solicite para o usuario informar:
    - nome
    -altura (cm)
    - peso (kg)
    com base nestes dados realize o calculo para descobrir
    qual o IMC (indice de massa corporea) da pessoa.
    para o calculo utilize a tabela padrão di imc.
    abaixo de 18,5 - abaixo do peso (pegue suplementos do cariani)
    entre 18,6 e 24,9 - peso ideal (para bens)
    ente 25,0 e 29,9 - sobrepeso
    entre 30,0 e 34,9 - obesidade grau 1
    entre 35,0 e 39,9 - obesidade grau 2
    acima de 40,0 - obesidade grau 3 (dr. nowzaradan te espera)
"""
nome = input("digite o nome da pessoa: ")
altura = float(input("digite a altura em centimetros: "))
Peso = float(input("digite o peso em quilogramas: "))
alturaMetros = altura / 100
imc = Peso / (alturaMetros ** 2)

if imc <= 18.5:
    print(f"{nome}, o imc seu será: {imc:.2f}. Você está abaixo do peso, pegue suplementos do Cariani.")
elif imc >= 18.6 and imc <= 24.9:
    print(f"{nome}, o imc seu será {imc:.2f}. peso ideal parabens.")
elif imc >= 25.0 and imc <= 29.9:
    print(f"{nome}, o imc seu será {imc:.2f}. sobrepesso.")
elif imc >= 30.0 and imc <= 34.9:
    print(f"{nome}, o imc seu será {imc:.2f}. obesidade grau 1.")
elif imc >= 35.0 and imc <= 39.9:
    print(f"{nome}, o imc seu será {imc:.2f}. obesidade grau 2.")
else:
    print(f"{nome}, o imc seu será {imc:.2f}. obesidade grau 3, dr. nowzaradan te espera.")