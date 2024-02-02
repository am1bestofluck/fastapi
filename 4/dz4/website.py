"""
Написать программу,
которая скачивает изображения с заданных URL-адресов
 и сохраняет их на диск.
  Каждое изображение должно сохраняться в отдельном файле,
   название которого соответствует названию изображения в URL-адресе.
Например, URL-адрес: https://example/images/image1.jpg -> файл на диске: image1.jpg
— Программа должна использовать многопоточный,
 многопроцессорный
 и асинхронный подходы.
— Программа должна иметь возможность задавать список URL-адресов через аргументы командной строки.

— Программа должна выводить в консоль информацию о времени скачивания каждого изображения
 и общем времени выполнения программы.
"""
import os
import pdb
from pathlib import Path
from sys import argv, exit
import requests
from time import time
from typing import Callable
from threading import Thread
from multiprocessing import Process

STORAGE = Path("./can")


def help_on_console():
    return """аргументы: [способ загрузки] [адрес файла в сети] (адрес файла в сети)
    [обязательный аргумент] (опциональный аргумент)
    Способ загрузки:
        0: синхронный
        1: многопроцессорный
        2: многопоточный
        3: асинхронный
    
    адрес файла в сети:
        ктрл-ц ктрл-в из адресной строки браузера"""


def clean_up():
    for i in STORAGE.iterdir():
        i.unlink()
    # pdb.set_trace(header="43")


def time_it(func: Callable):
    def wrapper(*args):
        for i in args:
            mini_start = time()
            func(i)
            print(f"{func.__name__} time:{time()-mini_start}")
        return True

    return wrapper


def __get_one_photo_sync(item: str):
    """Фасады нужны чтобы декоратор давал понятные подсказки"""
    item_m = requests.get(item)
    if item_m.status_code == 200:
        with open(file=(
                STORAGE / f"{item_m.url.split('/')[-1].split('.')[0]}.jpg").as_posix(),
                  mode="wb") as file_:
            file_.write(item_m.content)


@time_it
def get_photo_synchronized(item: str):
    return __get_one_photo_sync(item)


@time_it
def get_photo_threaded(item: str):
    return __get_one_photo_sync(item)


@time_it
def get_photo_multi_processed(item: str):
    return __get_one_photo_sync(item)


@time_it
def get_all_pics(approach: str):
    start = time()
    match approach:
        case "0":
            for i in argv[2:]:
                get_photo_synchronized(i)

        case "1":
            processes = []
            for i in argv[2:]:
                prc_ = Process(target=get_photo_multi_processed, args=(i,))
                prc_.run()
                processes.append(prc_)
            for prc_ in processes:
                try:
                    prc_.join()
                except AssertionError:
                    pass  # ну а чо. Интернет говорит что процессы нужно
                    # join'ить только если их нужно дождаться; а они закончились уже?
                    # https://stackoverflow.com/questions/25391025/what-exactly-is-python-multiprocessing-modules-join-method-doing
        case "2":
            threads = []
            for i in argv[2:]:
                thread = Thread(target=get_photo_threaded, args=(i,))
                thread.start()
                threads.append(thread)
            for thread in threads:
                thread.join()
        case "3":
            print("3")
        case _:
            raise ValueError("1st arg in [0,1,2,3] !")


if __name__ == '__main__':
    if len(argv) < 3:
        print(help_on_console())
        quit()
    clean_up()
    get_all_pics(argv[1])
