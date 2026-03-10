import numpy as np

def half_predict(number: int = 1) -> int:
    """Угадывает число от половины

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    low = 1
    high = 100  # верхняя граница поиска
    
    while True:
        count += 1
        predict_number = (low + high) // 2  # беру середину диапазона
        
        if predict_number == number:
            break  # угадал число
        elif predict_number < number:
            low = predict_number + 1  # отсекаем все числа меньше середины
        else:
            high = predict_number - 1  # отсекаем все числа больше середины
    
    return count

def score_game(predict_function) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        predict_function ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    
    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=1000) # загадали список чисел

    for number in random_array:
        count_ls.append(predict_function(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток
    
    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    
    return score

if __name__ == '__main__':
    score_game(half_predict)