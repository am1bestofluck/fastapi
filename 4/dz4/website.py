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
import asyncio
from random import choice

import aiohttp
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
            print(f"{func.__name__} time:{time() - mini_start}")
        return True

    return wrapper


async def __get_one_photo_async(item: str):
    """декоратор здесь приводит к ошибке ._."""
    local_start = time()
    file_name = f"{item.split('/')[-1].split('.')[0]}.jpg"
    async with aiohttp.ClientSession() as session:
        async with session.get(item) as response:
            content = await response.content.read()
            with open(file=(
                    STORAGE / file_name).as_posix(),
                      mode="wb") as file_:
                file_.write(content)
    print(f"Photo {file_name} downloaded in {time() - local_start:.6f} seconds.")


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
        case _:
            print(help_on_console())
            raise ValueError("1st arg in [0,1,2,3] !")


async def get_all_pics_false_asynced():
    tasks = []
    for pic_path in argv[2:]:
        await __get_one_photo_async(pic_path)


async def get_all_pics_asynced():
    tasks = []
    for pic_path in argv[2:]:
        task = asyncio.ensure_future(__get_one_photo_async(pic_path))
        tasks.append(task)
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    if len(argv) < 3:
        print(help_on_console())
        quit()
    clean_up()
    if argv[1] == "3":
        start_async = time()
        strategy = choice((True, False))
        if strategy:
            asyncio.run(get_all_pics_false_asynced())  # я так понимаю, что это синхронная загрузка
        else:
            loop = asyncio.get_event_loop()
            loop.run_until_complete(get_all_pics_asynced())
        print(f"Downloaded asynchronously in {time() - start_async:.6f} seconds.")
    else:
        get_all_pics(argv[1])
