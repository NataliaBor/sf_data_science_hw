"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    predict_number = 50 #Первая попытка
    min_val = 0
    max_val = 101
    
    while True:
        count+=1
        if predict_number > number:
            max_val = predict_number
            predict_number  = round((max_val+min_val)/2)
        elif predict_number < number:
            min_val = predict_number
            predict_number = round((max_val+min_val)/2)
        else:
            break
          
    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    #для контроля выводим максимальное и минимальное число попыток
    max_tries = int(np.max(count_ls))
    min_tries = int(np.min(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    print(max_tries)
    print(min_tries)
   
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
