Репозиторий для тестового задания:

Задание:

```
1. Декораторы  
    1. Написать декоратор который получает название функции  
    2. Написать декоратор который получает время выполнения функции  
    3. Написать асинхронною функцию которая выводит числа от 1 до  n с задержкой в пол секунды  
    4. Накинуть декораторы таким образом чтоб сначала вызвался результат функции, после название функции, после  время выполнения  
  в n должна быть возможность поставить любое число  
 
2. Мини сервис 
  Необходимо реализовать RESTAPI на fastapi + sqlalchemy который реализовывает в себе  функционал по работе с формой обратной связи клиента (фио, обращение, контактные данные)  
  1. В апи должен быть реализован весь функционал CRUD  
  плюсы к выполнению задания (не обязательные)  
    1) код покрыт тестами  
    2) проект запускается из контейнеров  
    3) есть функционал на частичный и полнотекстовый поиск  
```

Пояснения к коду



**Задание 1**

1.1 decorator_name.py - декоратор который возвращает имя функции. 

1.2 decorator_time.py - декоратор получает время выполнения функции.

1.3 async_function.py - асинхронная функция которая выводит числа от 1 до  n с задержкой в пол секунды 

1.4 Декораторы навешиваются на функцию в async_function.py

**Задание 2** 

Код для второго задания находится в папке app_src 

Код CRUD операций находится в app_src/api/v1/feedback/router.py

Для выполнения тестов необходимо экспортировать переменную PYTHONPATH
c указанием на app_src, например, как показано ниже.

`export PYTHONPATH=~/PycharmProjects/pythonProject_testing/app_src/
`
Код с тестами находится в app_src/tests/ 

Код для деплоя в контейнере находится в корневой директории 
- docker-compose.yml
- Dockerfile
