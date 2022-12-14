# 5 Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.

# *Пример:*

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

First_Point_X = int(input ("Введите значение для X первой точки: "))
First_Point_Y = int(input ("Введите значение для Y первой точки: "))
Second_Point_X = int(input ("Введите значение для X второй точки: "))
Second_Point_Y = int(input ("Введите значение для Y второй точки: "))
Dist = ((Second_Point_X-First_Point_X)**2 + (Second_Point_Y-First_Point_Y)**2)**0.5
Dist = round(Dist,3)
print (Dist)