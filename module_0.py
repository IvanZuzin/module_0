import numpy as np

number = np.random.randint(1,101)      # загадали число

print ("Загадано число от 1 до 100")

def game_core_v3(number):
    '''Начинаем с середины диапазона (50), в зависимости от результата 
    больше/меньше определяем новый диапозон в котором продолжаем искать число.
    Функция принимает загаданное число и возвращает число попыток вместе с загаданным числом'''
    
    count = 0
    min_range = 1
    max_range = 100
    predict = 50 # начальная позиция поиска
    
    while number != predict:
        count += 1
        if number > predict: 
            min_range = predict # определение ноговго минимума диапозона поиска
            predict += int((max_range - min_range)//2 + (1 if (max_range - min_range)//2 == 0 else 0))   
        elif number < predict: 
            max_range = predict # определение ноговго максимума диапозона поиска
            predict -= int((max_range - min_range)//2 + (1 if (max_range - min_range)//2 == 0 else 0))
    return print (f"Вы угадали число {number} за {count} попыток.")

game_core_v3(number)