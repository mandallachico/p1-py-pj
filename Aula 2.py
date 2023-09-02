print("Aula 2")
print("Objetos tipo sequência")
text = input("Digite uma palavra:")
print(f"Text size = {len(text)}")
print(f"Numbers of a in the word = {text.count('a')}")
print(f"The first 3 letter are: {text[0:3]}")


vowels = ['a', 'e', 'i', 'o', 'u']
print("Vowels")
for vowel in vowels:
    print (f"Position = {vowels.index(vowel)}, Each value = {vowel}\n")

print("Slpit Function")
splith = input("Insert a phrase with ; ")
words = splith.split(";")
print(f"Separated words by ; = {words}")

todolist = ['StUdy, lIvE, enJoY, work']
print(f"List of to to list {todolist}")
todolist = [up.upper() for up in todolist]
print("\nAfter the list comprehension upper =",todolist)

newtodolist = map(lambda lo: lo.lower(), todolist)
newtodolist = list(newtodolist)
print(f"New to do list with map lower is = {newtodolist}")

print("Range function use")
numbersto20 = list(range(0,21))

print(f"List of numbers to 20 = {numbersto20}\n")

print("These are the even numbers in this list of numbers to 20")
even_numbers = list(filter(lambda pa: pa %2 == 0, numbersto20))

print(even_numbers)

print("Using set\n")
numbersto9 = {'1,2,3,4,5,6,7,8,7,9,9'}
print(f"Numbers to 10 without set = {numbersto9}")
numbersto9 = {'1','2','3','4','5','6','7','8','7','9','9'}
print(f"Numbers to 10 with set = {numbersto9}")
numbord = sorted(numbersto9)
print(f"Lista ordenada de numbersto9 ={numbord}")
#numbersto10 = '1,2,3,4,5,6,7,8,7,9,9,10'
#print("11" not in numbersto10)

print("Algoritmos de ordenacao")
list = [15,12]
if list[0] > list[1]:
    aux = list[1]
    list[1] = list[0]
    list[0] = aux
print(list)


