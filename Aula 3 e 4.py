
import pandas as pd

print("Hello everyone. Lets work with db.")

print("\nThere's a db with sums of x plus 10. An example of pandas series")

a = [1,11,21,31,41,51]

mylist_plus10 = pd.Series(a)

print (mylist_plus10)

print("\nThere's a db with sums of var plus 10 with names and your ages. An example of pandas dataframe")

name_lists = 'Peter Gabriel Jay Alison'.split()
age_list = '35 29 49 28'.split()

data = list(zip(name_lists, age_list)) #Creating tuplas
pd.DataFrame(data, columns=['name', 'age plus 10']) #Creating a dataframe with tuplas
df = pd.DataFrame(data, columns=['name', '   age plus 10'])
print(df)

print("\nWhat's the true age of this members?\n")

class doguinhos:
  def __init__(self, name, age):
    self.name = name
    self.age = age

dog1 = doguinhos("john", 6)
dog2 = doguinhos("bela", 3)
dog3 = doguinhos("mich", 9)

print(dog1.name)
print(dog1.age)

print(dog2.name)
print(dog2.age)

print(dog3.name)
print(dog3.age)

print("Back again to DB!")

