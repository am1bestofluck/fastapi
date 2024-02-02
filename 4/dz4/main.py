"""
Напишите программу на Python, которая будет находить
сумму элементов массива из 1000000 целых чисел.
� Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
� Массив должен быть заполнен случайными целыми числами
от 1 до 100.
� При решении задачи нужно использовать многопоточность,
многопроцессорность и асинхронность.
� В каждом решении нужно вывести время выполнения
вычислений.
"""
from random import choices
from time import time
from typing import Callable
from threading import Thread
from multiprocessing import Process, Value

ITEMS = choices(range(-1000000, 1000000), k=10000000)


def time_it(func: Callable):
    def wrapper():
        start = time()
        out = func()
        print(f"{func.__name__} took {time() - start:.6f} seconds.")
        return out

    return wrapper


@time_it
def synced():
    global ITEMS
    return sum(ITEMS)


def sum_subroutine(collection_: list, *args):
    collection_.append(sum(*args))


@time_it
def threaded():
    global ITEMS
    threads = []
    results = []
    step = int(len(ITEMS) / 10)
    for i in range(0, len(ITEMS), int(len(ITEMS) / 10)):
        thread = Thread(target=sum_subroutine, args=(results, ITEMS[i:i + step]))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
    return sum(results)


@time_it
def multi_processed():
    def sum_subroutine_(itm, *args):
        with itm.get_lock():
            itm.value += sum(*args)

    global ITEMS
    processes = []
    step = int(len(ITEMS) / 10)
    results = Value('i', 0)

    for i in range(0, len(ITEMS), step):
        prc = Process(target=sum_subroutine_, args=(results, ITEMS[i:i + step]))
        prc.start()
        processes.append(prc)
    for process in processes:
        process.join()
    return results.value


if __name__ == '__main__':
    # assert (synced() == threaded() ==
    multi_processed()
