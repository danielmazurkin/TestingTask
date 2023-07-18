""""
Модуль, который демонстрирует работу декоратора, который
возвращает имя функции.
"""

import asyncio


def name(function):
    """
    Декоратор для двух видов функций. синхронных и асинхронных
    печатает имя функции.
    """
    async def wrapper_async(*args, **kwargs):
        result =  await function(*args, **kwargs)
        print(f"Имя функции {function.__name__}")
        return result

    def wrapper_sync(*args, **kwargs):
        result = function(*args, **kwargs)
        print(f"Имя функции {function.__name__}")
        return result

    if asyncio.iscoroutinefunction(function):
        return wrapper_async

    return wrapper_sync

@name
def print_hello():
    """Демонстрация синхронной функции и декоратора."""
    print("Hello")

@name
async def print_hello_async():
    """Демонстрация асинхронной функции и декоратора."""
    print("Hello async")


if __name__ == '__main__':
    print_hello()
    asyncio.run(print_hello_async())
