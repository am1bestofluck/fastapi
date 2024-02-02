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
import asyncio
from multiprocessing import Process, Value
from random import choices
from threading import Thread
from time import time
from typing import Callable

ITEMS = choices(range(-1000000, 1000000), k=1000000)
THREADS_CORES = 4


def time_it(func: Callable):
    def wrapper():
        start = time()
        out = func()
        print(f"{func.__name__} took {time()-start:.6f} seconds.")
        return out

    return wrapper


@time_it
def c_plus_plus():
    global ITEMS
    return sum(ITEMS)


@time_it
def synced():
    global ITEMS
    result = 0
    step = int(len(ITEMS) / THREADS_CORES)
    for i in range(0, len(ITEMS), int(len(ITEMS) / THREADS_CORES)):
        result += sum(ITEMS[i:i+step])
    return result


def sum_subroutine(collection_: list, *args):
    collection_.append(sum(*args))


def sum_subroutine_(results, *args):
    with results.get_lock():
        results.value += sum(*args)


@time_it
def threaded():
    global ITEMS
    threads = []
    results = []
    step = int(len(ITEMS) / THREADS_CORES)
    for i in range(0, len(ITEMS), int(len(ITEMS) / THREADS_CORES)):
        thread = Thread(target=sum_subroutine, args=(results, ITEMS[i:i+step]))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
    return sum(results)


@time_it
def multi_processed():
    global ITEMS
    processes = []
    step = int(len(ITEMS) / THREADS_CORES)
    results = Value('i', 0)

    for i in range(0, len(ITEMS), step):
        prc = Process(target=sum_subroutine_, args=(results, ITEMS[i:i+step]))
        prc.start()
        processes.append(prc)
    for process in processes:
        process.join()
    return results.value


async def asynced():
    global THREADS_CORES, ITEMS

    async def sub_sum(args):
        return sum(args)

    start = time()

    result = 0
    coroutines = []
    step = int(len(ITEMS) / THREADS_CORES)
    for i in range(0, len(ITEMS), step):
        coroutines.append(asyncio.create_task(sub_sum(ITEMS[i: i+step])))
    for i in coroutines:
        await i
        result += i.result()
    print(f"asynced took {time()-start:.6f} seconds.")
    return result


if __name__ == '__main__':
    assert c_plus_plus() == synced() == threaded() == asyncio.run(
        asynced()) == multi_processed()

