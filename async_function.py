import asyncio
from decorator_name import name
from decorator_time import measure_time


@measure_time
@name
async def print_numbers(n: int):
    """Асинхронная функция выводит числа от 1 до n с задержкой в полсекунды."""
    if number < 1:
        print("Число должно быть больше одного.")
        return None

    for i in range(1, n + 1):
        await asyncio.sleep(0.5)
        print(i)



if __name__ == '__main__':
    try:
        number = int(input("Введите число n: \n"))
        asyncio.run(print_numbers(number))
    except ValueError:
        print("Необходимо ввести число!")
