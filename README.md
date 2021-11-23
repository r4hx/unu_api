# UNU_API

Библиотека для интеграции с биржой микрозадач https://unu.im

## Содержание

  - [Как работает UNU?](#как-работает-unu)
  - [Доступные типы задач](#доступные-типы-задач)
  - [Установка](#установка)
  - [Зависимости](#зависимости)
  - [Использование](#использование)
  - [Тестирование](#тестирование)
  - [Доступные методы](#доступные-методы)
  - [Кастомные исключения](#кастомные-исключения)
  - [Устранение неполадок](#устранение-неполадок)
  - [Ссылки](#ссылки)


## Как работает UNU?

* Регистрируетесь на сайте
* Добавляете задание и оплачиваете необходимое количество работ
* Получаете результат и проверяете выполненные работы

## Доступные типы задач

![This is an image](https://unu.im/files/image.svg)
* Наполнение сайтов: комментарии, отзывы, форумы, доски объявлений
* Продвижение в социальных сетях: подписчики в группы, лайки, репосты
* Продвижение приложений: установки и действия
* Любые произвольные задачи, которые нужно выполнять на регулярной основе

## Установка

```shell
pip install unu_api
```

## Зависимости

На данный момент библиотека зависит только от ```requests```

## Использование

Получите токен в личном кабинете на сайте https://unu.im/api-info и инициализируйте класс для работы с API

```python
from unu_api import Api

u = Api(token="ВАШ_ТОКЕН")

request = u.get_balance()
```

## Тестирование

Протестировать библиотеку можно запустив команду pytest указав в переменной окружения ваш API_KEY

```shell
API_KEY=ВАШ_ТОКЕН pytest
```
## Доступные методы

Реализован полный набор методов доступный в официальном API

* **get_balance** - Возвращает количество доступных средств
* **get_folders** - Возвращает все созданные папки с задачами
* **create_folder** - Создаёт новую папку
* **move_task** - Перемещает задачу в указанную папку
* **get_tasks** - Возвращает существующие задачи
* **get_reports** - Возвращает отчёты по определённой задаче или все существующие отчёты
* **approve_report** - Принимает (оплачивает) отчёт по заданию
* **reject_report** - Отклоняет отчёт по заданию
* **get_expenses** - Возврашает сумму израсходованных средств
* **add_task** - Создаёт новую задачу
* **task_limit_add** - Устанавливает лимит (добавляет выполнения) определённой задачи
* **edit_task** - Редактирует существующую задачу
* **get_tariffs** - Возвращает все доступные тарифы
* **task_pause** - Приостанавливает выполнение задачи
* **task_play** - Активирует выполнение задачи
* **get_minter_wallet** - Возвращает адрес Minter-кошелька для пополнения баланса аккаунта

## Кастомные исключения

Мне пришлось реализовать кастомный набор ошибок для удобства разработки.

* **AuthError** - Исключение при отсутствие токена
* **BalanceError** - Исключения при отрицательном балансе
* **RequestError** - Исключение для неуспешных запросов к API
* **JsonParsingError** - Исключение для ошибок декодирования Json
* **UnknowError** - Для неизвестных ошибок

## Устранение неполадок

Время от времени могут переставать работать определенные методы. Вместо json будет в ответ прилетать лог ошибки php, обычно я пишу в поддержку на сайте и разработчики фиксят эти баги. Для этого кейса я ввел кастомное исключение **JsonParsingError**.

## Ссылки

Сайт биржи - https://unu.im

Блог автора - https://egorovegor.ru

Ссылка на GitHub - https://github.com/r4hx/unu_api/

Ссылка на PyPi - https://pypi.org/project/unu_api/
