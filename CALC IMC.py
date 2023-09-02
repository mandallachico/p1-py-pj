print("Calculadora de Indice de Massa Corporal em funcionamento")
print("\nVou calcular seu IMC, ok? Mas antes preciso de alguns dados seus.")
name = input("Qual seu nome?\n")
age = int(input("Qual sua idade?\n"))
if age <= 19:
    print("Hmm, vamos continuar mas não vou conseguir calcular com mais precisão seu IMC pois voce tem menos que 20 anos\n")
elif age > 65:
    print("Hmm, vamos continuar mas não vou conseguir calcular com mais precisão seu IMC pois voce tem mais que 65 anos")

eight = float(input("Qual seu peso(ex:82.3)?\n"))
weight = float(input("Qual sua altura(ex: 1.77)?\n"))
gender = input("Voce eh homem ou mulher? Digite h para o primeiro e m para o segundo\n")

print("De acordo com seu peso e altura vamos te dizer seu IMC")
c6 = range(6)
for c5 in c6:
    print(c5)

imc = eight//(weight**2)
print(f"Seu Indice de Massa Corporal eh de:{imc}")

if imc < 18.5:
    print(f"{name}, de acordo com os dados que voce me passou, parece que tu estas abaixo do peso :(")
elif imc < 25:
    print(f"{name}, de acordo com os dados que voce me passou, parece que tu estas com o peso normal:D")
elif imc < 30:
    print(f"{name}, de acordo com os dados que voce me passou, parece que tu estas com pre obesidade, atenção :|")
elif imc < 35:
    print(f"{name}, de acordo com os dados que voce me passou, parece que tu estas com obesidade de grau 1 :[")
elif imc < 40:
    print(f"{name}, de acordo com os dados que voce me passou, parece que tu estas com obesidade de grau 2 :(")
elif imc > 40:
    print(f"{name}, de acordo com os dados que voce me passou, parece que tu estas com obesidade de grau 3 :!")
elif imc <= 0:
    print("Hmm, parece que algo deu errado, seu peso e altura foram digitados corretamente")

print("\nMuito obrigado por calcular seu IMC comigo! Alimente-se bem, se exercite e beba água.")
