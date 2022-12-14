# 4 Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

quarter_num = int(input ('Введите номер четверти: '))
if quarter_num <1 or quarter_num >4:
    print ('Вы ввели некоректный номер четверти')
elif quarter_num == 1:
    print ('Диапазон координат: +X,+Y')
elif quarter_num == 2:
    print ('Диапазон координат: -X,+Y')
elif quarter_num == 3:
    print ('Диапазон координат: -X,-Y')
elif quarter_num == 4:
    print ('Диапазон координат: +X,-Y')