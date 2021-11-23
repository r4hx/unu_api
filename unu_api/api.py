""" Text """
from datetime import datetime

from .client import Client
from .exceptions import AuthError


class Api(Client):
    """
    Класс для работы с API
    """

    def __init__(self, url: str = "https://unu.im/api", token: str = None):
        self.url = url
        self.token = token
        if self.token is None:
            raise AuthError

    def get_balance(self) -> str:
        """
        Возвращает количество доступных средств.

        Входные данные
            Отсутствует
        Выходные данные
            balance (float) - количество средств на балансе в UNU
            blocked_money (float) - количество замороженных средств текущих задач
        """
        data = {
            "api_key": self.token,
            "action": "get_balance",
        }
        return Client.post(url=self.url, data=data)

    def get_folders(self) -> str:
        """
        Возвращает все созданные папки с задачами.

        Входные данные
            Отсутствует
        Выходные данные
            folders (array) - массив с папками
        Каждый элемент массива содержит:
            id (int) - уникальный идентификатор папки
            name (text) - имя папки
        """
        data = {
            "api_key": self.token,
            "action": "get_folders",
        }
        return Client.post(url=self.url, data=data)

    def create_folder(self, name: str) -> str:
        """
        Создаёт новую папку.

        Входные данные
            name (text) - имя папки
        Выходные данные
            folder_id (int) - уникальный идентификатор созданной папки
        """
        data = {
            "api_key": self.token,
            "action": "create_folder",
            "name": name,
        }
        return Client.post(url=self.url, data=data)

    def move_task(self, task_id: int, folder_id: int) -> str:
        """
        Перемещает задачу в указанную папку.

        Входные данные
            task_id (int) - идентификатор задачи
            folder_id (int) - идентификатор папки, куда нужно переместить задачу
        Выходные данные
            Отсутствуют
        """
        data = {
            "api_key": self.token,
            "action": "move_task",
            "task_id": task_id,
            "folder_id": folder_id,
        }
        return Client.post(url=self.url, data=data)

    def get_tasks(self, folder_id: int = None) -> str:
        """
        Возвращает существующие задачи.

        Входные данные
            folder_id (int) - идентификатор папки, из которой \
                нужно показать задачи (необязательный параметр)
        Выходные данные
            id (int) - идентификатор задачи
            name (text) - название задачи
            price_unu (float) - стоимость выполнения в UNU
            price_rub (float) - стоимость выполнения в рублях
            status (int) - текущий статус задачи
                1 - новое задание, нужно оплатить (увеличить лимит)
                2 - достигло лимита
                3 - остановлено
                4 - активно
                5 - отклонено модератором
                6 - на модерации
            folder_id (int) - идентификатор папки
        """
        data = {
            "api_key": self.token,
            "action": "get_tasks",
            "folder_id": folder_id,
        }
        return Client.post(url=self.url, data=data)

    def get_reports(self, task_id: int = None) -> str:
        """
        Возвращает отчёты по определённой задаче или все существующие отчёты.

        Входные данные
            task_id (int) - идентификатор задачи, по которой \
                нужно вернуть отчёты (необязательный параметр)

        Выходные данные
            id (int) - идентификатор отчёта
            task_id (int) - идентификатор отчёта
            worker_id (int) - идентификатор пользователя, выполняющего работу
            price_unu (float) - стоимость выполнения в UNU
            price_rub (float) - стоимость выполнения в рублях
            status (int) - текущий статус отчёта
                1 - в работе
                2 - на проверке
                3 - на доработке
                6 - оплачено
            folder_id (int) - идентификатор папки
        """
        data = {
            "api_key": self.token,
            "action": "get_reports",
            "task_id": task_id,
        }
        return Client.post(url=self.url, data=data)

    def approve_report(self, report_id: int) -> str:
        """
        Принимает (оплачивает) отчёт по заданию.

        Входные данные
            report_id (int) - идентификатор отчёта, который нужно одобрить
        Выходные данные
            отсутствуют
        """
        data = {
            "api_key": self.token,
            "action": "approve_report",
            "report_id": report_id,
        }
        return Client.post(url=self.url, data=data)

    def reject_report(
        self, report_id: int, reject_type: int, comment: str = None
    ) -> str:
        """
        Отклоняет отчёт по заданию.

        Входные данные
            report_id (int) - идентификатор отчёта, который нужно одобрить
            comment (text) - причина отказа
            reject_type (int) - какое именно действие нужно выполнить
                1 - отправить на доработку
                2 - отказать
        Выходные данные
            отсутствуют
        """
        data = {
            "api_key": self.token,
            "action": "reject_report",
            "report_id": report_id,
            "comment": comment,
            "reject_type": reject_type,
        }
        return Client.post(url=self.url, data=data)

    def get_expenses(
        self,
        task_id: int = None,
        folder_id: int = None,
        date_from: datetime = None,
        date_to: datetime = None,
    ) -> str:
        """
        Возврашает сумму израсходованных средств

        Входные данные
            task_id (int) - идентификатор задачи по которой нужно \
                получить расходы (необязательный параметр)
            folder_id (int) - идентификатор папки по которой нужно \
                получить расходы (необязательный параметр)
            date_from (datetime) - начало периода \
                (с какой даты нужно вернуть расходы), \
                    пример 2019-11-01 13:00:00 (необязательный параметр)
            date_to (datetime) - конец периода \
                (по какую дату нужно вернуть расходы), \
                    пример 2019-11-05 13:00:00 (необязательный параметр)
        Выходные данные
            expenses (float) - сумма расходов в UNU
            expenses_in_rub (float) - сумма расходов в рублях
        """
        data = {
            "api_key": self.token,
            "action": "get_expenses",
            "task_id": task_id,
            "folder_id": folder_id,
            "date_from": date_from,
            "date_to": date_to,
        }
        return Client.post(url=self.url, data=data)

    def add_task(
        self,
        name: str,
        descr: str,
        need_for_report: str,
        price: float,
        tarif_id: int,
        folder_id: int,
        link: str = None,
        need_screen: bool = False,
        time_for_work: int = None,
        limit_per_day: int = None,
        limit_per_hour: int = None,
        limit_per_user: int = None,
        limit_per_user_folder: int = None,
        delay_from: int = None,
        delay_to: int = None,
        targeting_gender: int = None,
        targeting_age_from: int = None,
        targeting_age_to: int = None,
        targeting_geo_country_id: int = None,
        targeting_geo_region_id: int = None,
        targeting_geo_city_id: int = None,
        task_only_for_list_id: int = None,
    ) -> str:
        """
        Создаёт новую задачу

        Входные данные
            name (text) - название задачи
            descr (text) - текст задания
            link (text) - URL, необходимый для выполнения \
                задания (необязательный параметр)
            need_for_report (text) - что должен предоставить \
                исполнитель для отчёта по задаче
            price (float) - стоимость одного выполнения задачи в рублях
            tarif_id (int) - идентификатор тарифа
            folder_id (int) - идентификатор папки, в которую \
                нужно поместить задачу
            need_screen (boolean) - если в задании исполнителю нужно \
                прикерпить скриншот, нужно передать 1 (необязательный параметр)
            time_for_work (int) - сколько часов дать исполнителю для работы, \
                от 2 до 168 (необязательный параметр)
            limit_per_day (int) - лимит выполнений в сутки \
                (необязательный параметр)
            limit_per_hour (int) - лимит выполнений в час \
                (необязательный параметр)
            limit_per_user (int) - лимит выполнений для одного исполнителя \
                (необязательный параметр)
            limit_per_user_folder (int) - лимит от исполнителя на папку \
                (необязательный параметр)
            delay_from (int) - задержка между выполнениями в минутах, от \
                (необязательный параметр)
            delay_to (int) - задержка между выполнениями в минутах, до \
                (необязательный параметр)
            targeting_gender (int) - параметр таргетинга: \
                пол. 1 - женский, 2 - мужской (необязательный параметр)
            targeting_age_from (int) - параметр таргетинга: возраст от \
                (необязательный параметр)
            targeting_age_to (int) - параметр таргетинга: возраст до \
                (необязательный параметр)
            targeting_geo_country_id (int) - параметр геотаргетинга: ID страны \
                (необязательный параметр)
            targeting_geo_region_id (int) - параметр геотаргетинга: ID региона \
                (необязательный параметр)
            targeting_geo_city_id (int) - параметр геотаргетинга: ID города \
                (необязательный параметр)
            task_only_for_list_id (int) - ID белого списка исполнителей, \
                которому будет доступно задание (необязательный параметр)
        Выходные данные
            task_id (int) - идентификатор созданной задачи
        """
        data = {
            "api_key": self.token,
            "action": "add_task",
            "name": name,
            "descr": descr,
            "need_for_report": need_for_report,
            "price": price,
            "tarif_id": tarif_id,
            "folder_id": folder_id,
            "link": link,
            "need_screen": need_screen,
            "time_for_work": time_for_work,
            "limit_per_day": limit_per_day,
            "limit_per_hour": limit_per_hour,
            "limit_per_user": limit_per_user,
            "limit_per_user_folder": limit_per_user_folder,
            "delay_from": delay_from,
            "delay_to": delay_to,
            "targeting_gender": targeting_gender,
            "targeting_age_from": targeting_age_from,
            "targeting_age_to": targeting_age_to,
            "targeting_geo_country_id": targeting_geo_country_id,
            "targeting_geo_region_id": targeting_geo_region_id,
            "targeting_geo_city_id": targeting_geo_city_id,
            "task_only_for_list_id": task_only_for_list_id,
        }
        return Client.post(url=self.url, data=data)

    def task_limit_add(self, task_id: int, add_to_limit: int) -> str:
        """
        Устанавливает лимит (добавляет выполнения) определённой задачи. \
            После создания любой задачи обязательно нужно \
                задать лимит выполнений по ней.

        Входные данные
            task_id (int) - идентификатор задачи
            add_to_limit (int) - сколько раз нужно выполнить задание
        Выходные данные
            отсутствуют
        """
        data = {
            "api_key": self.token,
            "action": "task_limit_add",
            "task_id": task_id,
            "add_to_limit": add_to_limit,
        }
        return Client.post(url=self.url, data=data)

    def edit_task(
        self,
        task_id: int,
        name: str,
        descr: str,
        need_for_report: str,
        price: float,
        tarif_id: int,
        folder_id: int,
        need_screen: bool = False,
        time_for_work: int = None,
        limit_per_day: int = None,
        limit_per_hour: int = None,
        limit_per_user: int = None,
        limit_per_user_folder: int = None,
        delay_from: int = None,
        delay_to: int = None,
        targeting_gender: int = None,
        targeting_age_from: int = None,
        targeting_age_to: int = None,
        targeting_geo_country_id: int = None,
        targeting_geo_region_id: int = None,
        targeting_geo_city_id: int = None,
    ) -> str:
        """
        Редактирует существующую задачу

        Входные данные
            task_id (int) - идентификатор задачи для редактирования
            name (text) - название задачи
            descr (text) - текст задания
            need_for_report (text) - что должен предоставить \
                исполнитель для отчёта по задаче
            price (float) - стоимость одного выполнения задачи в рублях
            tarif_id (int) - идентификатор тарифа
            folder_id (int) - идентификатор папки, в которую \
                нужно поместить задачу
            need_screen (boolean) - если в задании исполнителю \
                нужно прикерпить скриншот, нужно передать 1 \
                    (необязательный параметр)
            time_for_work (int) - сколько часов дать исполнителю \
                для работы, от 2 до 168 (необязательный параметр)
            limit_per_day (int) - лимит выполнений в сутки \
                (необязательный параметр)
            limit_per_hour (int) - лимит выполнений в час \
                (необязательный параметр)
            limit_per_user (int) - лимит выполнений для одного исполнителя \
                (необязательный параметр)
            limit_per_user_folder (int) - лимит от исполнителя на папку \
                (необязательный параметр)
            delay_from (int) - задержка между выполнениями в минутах, от \
                (необязательный параметр)
            delay_to (int) - задержка между выполнениями в минутах, до \
                (необязательный параметр)
            targeting_gender (int) - параметр таргетинга: \
                пол. 1 - женский, 2 - мужской (необязательный параметр)
            targeting_age_from (int) - параметр таргетинга: возраст от \
                (необязательный параметр)
            targeting_age_to (int) - параметр таргетинга: возраст до \
                (необязательный параметр)
            targeting_geo_country_id (int) - параметр геотаргетинга: ID страны \
                (необязательный параметр)
            targeting_geo_region_id (int) - параметр геотаргетинга: ID региона \
                (необязательный параметр)
            targeting_geo_city_id (int) - параметр геотаргетинга: ID города \
                (необязательный параметр)
        Выходные данные
            отсутствуют
        """
        data = {
            "api_key": self.token,
            "action": "edit_task",
            "task_id": task_id,
            "name": name,
            "descr": descr,
            "need_for_report": need_for_report,
            "price": price,
            "tarif_id": tarif_id,
            "folder_id": folder_id,
            "need_screen": need_screen,
            "time_for_work": time_for_work,
            "limit_per_day": limit_per_day,
            "limit_per_hour": limit_per_hour,
            "limit_per_user": limit_per_user,
            "limit_per_user_folder": limit_per_user_folder,
            "delay_from": delay_from,
            "delay_to": delay_to,
            "targeting_gender": targeting_gender,
            "targeting_age_from": targeting_age_from,
            "targeting_age_to": targeting_age_to,
            "targeting_geo_country_id": targeting_geo_country_id,
            "targeting_geo_region_id": targeting_geo_region_id,
            "targeting_geo_city_id": targeting_geo_city_id,
        }
        return Client.post(url=self.url, data=data)

    def get_tariffs(self) -> str:
        """
        Возвращает все доступные тарифы.

        Входные данные
            Отсутствует
        Выходные данные
            tariffs (array) - массив с тарифами
        Каждый элемент массива содержит:
            id (int) - уникальный идентификатор тарифа
            name (text) - названия тарифа
            min_price_rub (float) - минимальная стоимость в рублях
            group_id (int) - идентификатор группы тарифов
        """
        data = {
            "api_key": self.token,
            "action": "get_tariffs",
        }
        return Client.post(url=self.url, data=data)

    def task_pause(self, task_id: int) -> str:
        """
        Приостанавливает выполнение задачи

        Входные данные
            task_id (int) - идентификатор задачи
        Выходные данные
            отсутствуют
        """
        data = {
            "api_key": self.token,
            "action": "task_pause",
            "task_id": task_id,
        }
        return Client.post(url=self.url, data=data)

    def task_play(self, task_id: int) -> str:
        """
        Активирует выполнение задачи

        Входные данные
            task_id (int) - идентификатор задачи
        Выходные данные
            отсутствуют
        """
        data = {
            "api_key": self.token,
            "action": "task_play",
            "task_id": task_id,
        }
        return Client.post(url=self.url, data=data)

    def get_minter_wallet(self, email: str = None) -> str:
        """
        Возвращает адрес Minter-кошелька для пополнения баланса аккаунта

        Входные данные
            email (text) - email аккаунта, который нужно пополнить \
                (необязательный параметр). Указываеться только если \
                    нужно получить кошелёк для пополнения \
                        аккаунта другого пользователя.
        Выходные данные
            wallet (text) - Адрес Minter-кошелька
        """
        data = {
            "api_key": self.token,
            "action": "get_minter_wallet",
            "email": email,
        }
        return Client.post(url=self.url, data=data)
