# Напишите программу для. проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.


X = int(input('Введите значение X'))
Y = int(input('Введите значение Y'))
Z = int(input('Введите значение Z'))
first = not (X or Y or Z)
second = not X and not Y and not Z
result = first==second
print (result)

