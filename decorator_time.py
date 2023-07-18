""""
Модуль, который демонстрирует работу декоратора, который
возвращает время работы функции.
"""

import time
import requests
import asyncio


def measure_time(func, *args, **kwargs):
    """Декоратор для измерения времени выполнения функции."""

    async def wrapper_async(*args, **kwargs):
        start_time = time.time()
        result = await func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        formatted_time = time.strftime("%H:%M:%S", time.gmtime(execution_time))
        print(f"Функция {func.__name__} выполнилась за {formatted_time}")
        return result

    def wrapper_sync(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        formatted_time = time.strftime("%H:%M:%S", time.gmtime(execution_time))
        print(f"Асинхронная Функция {func.__name__} выполнилась за {formatted_time}")
        return result

    if asyncio.iscoroutinefunction(func):
        return wrapper_async

    return wrapper_sync


@measure_time
async def function_get_google_async(*args, **kwargs):
    """
    Функция получает страницу google для измерения результата по времени.
    Асинхронная.
    """
    response = requests.get('https://google.com')
    return response.status_code


@measure_time
def function_get_google(*args, **kwargs):
    """
    Функция получает страницу google для измерения результата по времени.
    Синхронная.
    """
    response = requests.get('https://google.com')
    return response.status_code


if __name__ == '__main__':
    function_get_google()
    asyncio.run(function_get_google_async())
