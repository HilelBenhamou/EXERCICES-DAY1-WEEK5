# EXO CAT
# class Cat:
#     species = 'mammal'
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# cat1=Cat('Rouxy',18)
# cat2=Cat('Chily',9)
# cat3=Cat('Rex',15)

# # print(Cat.age)

# def oldest():
#   if cat1.age<cat2.age:
#     old=cat2.age
#     if cat2.age<cat3.age:
#       old=cat3.age
#   else:
#     old=cat1.age
#   print(old)
#   return
# old=oldest()

# print(f'The oldest cat is {old}')

#####################################################################
# EXO1
# class Dog:
#   def __init__(self,nameDog, heightDog):
#     self.nameDog=nameDog
#     self.heightDog=heightDog
#
#   def talk(self):
#     print('Wouaf')
#
#   def jump(self):
#     return self.heightDog*2
#
# Davids_dog=Dog('Rex',50)
# Sarahs_dog=Dog('Teacup',20)
#
# print(Davids_dog.nameDog)
# print(Davids_dog.heightDog)
# print(Sarahs_dog.nameDog)
# print(Sarahs_dog.heightDog)
#
# if Sarahs_dog.heightDog>Davids_dog.heightDog:
#   print(f'This is the davids dog who has {Sarahs_dog.heightDog} years old')
# else:
#   print(f'This is the davids dog who has {Davids_dog.heightDog} years old')

#####################################################################
# EXO2
# class Zoo:
#     def __repr__(self):
#         return f'<This is the Zoo {self.zooName}>'
#
#     def __init__(self, zooName):
#         self.animals = []
#         self.zooName = zooName
#
#     def addAnimal(self, newAnimal):
#         if newAnimal not in self.animals:
#           self.animals.append(newAnimal)
#         else:
#           print('He is already in the list')
#
#
#     def getAnimal(self):
#       print(self.animals)
#
#     def sellAnimal(self, soldAnimal):
#       print(f'Goodbye to {soldAnimal}')
#       self.animals.remove(soldAnimal)
#       # print(self.animals)
#
#     def sortAnimal(self):
#       self.animals.sort()
#       for i, each in enumerate(self.animals,1):
#         print(f'{i}:{(each)}')

# def getPen(self):

# from EXO.exo import Zoo

# zoo1=Zoo('zoo1')
# zoo1.addAnimal('Tiger')
# zoo1.addAnimal('Lion')
# zoo1.addAnimal('Elephant')
# zoo1.addAnimal('Toucan')
# zoo1.addAnimal('Zebra')
# zoo1.getAnimal()
# zoo1.sellAnimal('Lion')
# zoo1.sortAnimal()
#
# ramatGanSafari=Zoo('Ramat Gan Safary')
# ramatGanSafari.addAnimal('Singe')
# ramatGanSafari.addAnimal('Panthere')
# ramatGanSafari.addAnimal('Birds')
# ramatGanSafari.addAnimal('Girafe')
# ramatGanSafari.addAnimal('Rhinoceros')
# ramatGanSafari.getAnimal()
# ramatGanSafari.sortAnimal()

##################XP GOLD###########################################
# EXO1 XP GOLD

# import math
# from math import pi
#
# class Circle:
#   def __init__(self,radius=1.0):
#     self.radius = radius
#   def perimeter(self):
#     return 2*pi*self.radius
#   def area(self):
#     return pi*self.radius
#
#   @staticmethod
#   def definition():
#     print('''
#     A circle is an important shape in the field of geometry.
#     Let's look at the definition of a circle and its parts.
#     We will also examine the relationship between the circle and the plane.     A circle is a shape with all points the same distance from its center. ...
#     Thus, the diameter of a circle is twice as long as the radius.
#     ''')
#
# mycircle=Circle()
# print(f'the Perimeter of the circle is {mycircle.perimeter()}')
# print(f'the Area of the circle is {mycircle.area()}')
# mycircle.definition()

###################################################
# EXO2 XP GOLD
# import random
#
# class Mylist:
#   def __init__(self):
#     self.python=[]
#   def reversed(self):
#     self.python.reverse()
#     return self.python
#   def sortedlist(self):
#     return sorted(self.python)
#   def randomlist(self):
#     self.python=[random.randint(1,300) for i in range(len(self.python))]
#     return self.python
#
# list1=Mylist()
# list1.python=[1,2,50,48,99,100,125,75,45]
# print(f'This is the list:{list1.python}')
# print(f'This is the reverse list:{list1.reversed()}')
# print(f'This is the sorted list: {list1.sortedlist()}')
# print(f'This is the random list: {list1.randomlist()}')

########################################################
# EXO3 XP GOLD
import random


# class QuantumParticle:
#   def __init__(self,x,p,spin):
#     self.x=random.radint(1,1000)
#     self.p=round(random.uniform(1,1000),2)
#     listspin=[0.5,-0.5]
#     self.spin=random.sample(listspin,1)


#########################################
# EXO1 NINJA
# class MenuManager:
#     def __init__(self,name):
#       self.name=name
#       self.main_menu={}
#       self.menu = {'meal':{'price': 0, 'spice_level': '', 'gluten': ''}}
#
#     def add_item(self, meal, price, spice_level, gluten):
#         menu2={meal:{'price':price,'spice_level':spice_level,'gluten':gluten}}
#         self.main_menu.update(menu2)
#
#     def update_item(self, meal, price, spice_level='', gluten=''):
#       menu2 = {meal: {'price': price, 'spice_level': spice_level, 'gluten': gluten}}
#       if self.main_menu[meal]:
#         self.main_menu.update(menu2)
#       else:
#         print("Doesn't exit")
#
#     def remove_item(self, meal):
#       if self.main_menu[meal]:
#         print(meal)
#         self.main_menu.pop(meal)
#
# Mymenu = MenuManager('ChezLuigi')
# Mymenu.add_item('pizza', 10, 'C', True)
# Mymenu.add_item('Salad', 15, 'A', False)
# Mymenu.add_item('Fish', 10, 'A', False)
# Mymenu.add_item('Coktail', 10, 'A', False)
# Mymenu.update_item('pizza', 24)
# print(Mymenu.main_menu)
# Mymenu.remove_item('pizza')

#############################################################################
#EXO2 NINJA
class Farm:
  def __init__(self,nameFarm):
    self.name=nameFarm
    self.animals={}

  def add_animal(self,animal,number=1):
    if animal not in self.animals:
      animals2={animal:number}
      self.animals.update(animals2)
    else:
      animals2 = {animal: number+1}
      self.animals.update(animals2)

  def get_info(self):
    print(f'{self.name}={self.animals}')

  def get_animal_types(self):
    list = []
    for key in self.animals:
      list.append(key)
    return list

  def get_short_info(self):
    return print(f"{self.name}'s farm has {self.name.get_animal_types()}")

macdonald=Farm('McDonald')
macdonald.add_animal('cow',5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat',12)
print(macdonald.get_info())
print(macdonald.get_animal_types())
macdonald.get_short_info()