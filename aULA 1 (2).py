print('Hello, world! My name is...')

name = input("Complete the phrase: ")
print(name)
if name:
    print('A variável não é vazia')

print(type(name))

print(f'Congrats, {name}! Its your first program!')

x = int(input("Tell me your age:"))
y = int(input("Tell me your weight:"))
if x > y:
    print ("You cannot be thinner than your age!")

elif x >= 18:
    print("Maior de idade em!")

print("The sum of your age and weight is:") 
print(x+y)

qtde_faltas = int(input("Quantas faltas você tem na academia? "))
mensa_pag = int(input("Você pagou a academia esse mês? 1 para sim e 2 para não: "))

if qtde_faltas >= 10 and mensa_pag == 1:
    print("Você é um vacilão!")
if qtde_faltas >= 10 and mensa_pag == 2:
    print("Caloteiro faltante!")
if qtde_faltas <= 10 and mensa_pag == 2:
    print("Caloteiro!")
else:
    print("Usou bem a academia!")

print("while qtde_faltas != 0:" "Mas ainda um faltante!")

the_word = (input("Tell me a word: "))

for i, c in enumerate(the_word):
    print(f"Posição = {i}, valor ={c}")

print("For now, we'll get some math functions" )

