"""
Тесты методов API
"""
import os
from uuid import uuid4

from unu_api import Api


def test_get_balance():
    """
    Тест метода проверки баланса
    """
    unu = Api(token=os.getenv("API_KEY"))
    request = unu.get_balance()
    assert request["success"] == "true"
    assert isinstance(request["balance"], float)


def test_get_folders():
    """
    Тест метода получения директорий
    """
    unu = Api(token=os.getenv("API_KEY"))
    request = unu.get_folders()
    assert request["success"] == "true"
    assert isinstance(request["folders"], list)


def test_create_folder():
    """
    Тест метода создания директорий
    """
    unu = Api(token=os.getenv("API_KEY"))
    folder_name = uuid4()
    request = unu.create_folder(folder_name)
    assert request["success"] == "true"
    assert isinstance(request["folder_id"], int)


def test_add_task():
    """
    Тест метода создания задачи
    """
    unu = Api(token=os.getenv("API_KEY"))
    name = uuid4()
    descr = uuid4()
    need_for_report = uuid4()
    price = 1.2
    tarif_id = 11
    folder_id = 0
    request = unu.add_task(
        name=name,
        descr=descr,
        need_for_report=need_for_report,
        price=price,
        tarif_id=tarif_id,
        folder_id=folder_id,
    )
    assert request["success"] == "true"
    assert isinstance(request["task_id"], int)


def test_move_task():
    """
    Тест метода перемещения задачи
    """
    unu = Api(token=os.getenv("API_KEY"))
    name = uuid4()
    descr = uuid4()
    need_for_report = uuid4()
    price = 1.2
    tarif_id = 11
    folder_id = 0
    request = unu.add_task(
        name=name,
        descr=descr,
        need_for_report=need_for_report,
        price=price,
        tarif_id=tarif_id,
        folder_id=folder_id,
    )
    assert request["success"] == "true"
    assert isinstance(request["task_id"], int)
    task_id = request["task_id"]
    folder_name = uuid4()
    request = unu.create_folder(folder_name)
    assert request["success"] == "true"
    assert isinstance(request["folder_id"], int)
    folder_id = request["folder_id"]
    request = unu.move_task(task_id=task_id, folder_id=folder_id)
    assert request["success"] == "true"


def test_get_tasks():
    """
    Тест метода получения списка задач
    """
    unu = Api(token=os.getenv("API_KEY"))
    request = unu.get_tasks()
    assert request["success"] == "true"
    assert isinstance(request["tasks"], list)


def test_get_reports():
    """
    Тест метода получения отчетов по задачам
    """
    unu = Api(token=os.getenv("API_KEY"))
    request = unu.get_reports()
    assert request["success"] == "true"
    assert isinstance(request["reports"], list)


def test_get_minter_wallet():
    """
    Тест метода получения идентификатора кошелька минтер
    """
    unu = Api(token=os.getenv("API_KEY"))
    request = unu.get_minter_wallet()
    assert request["success"] == "true"


def test_get_expenses():
    """
    Тест метода проверки расходов
    """
    unu = Api(token=os.getenv("API_KEY"))
    request = unu.get_expenses()
    assert request["success"] == "true"


def test_task_limit_add():
    """
    Тест метода добавления лимитов задаче
    """
    unu = Api(token=os.getenv("API_KEY"))
    name = uuid4()
    descr = uuid4()
    need_for_report = uuid4()
    price = 1.2
    tarif_id = 11
    folder_id = 0
    request = unu.add_task(
        name=name,
        descr=descr,
        need_for_report=need_for_report,
        price=price,
        tarif_id=tarif_id,
        folder_id=folder_id,
    )
    assert request["success"] == "true"
    assert isinstance(request["task_id"], int)
    task_id = request["task_id"]
    limit = 1
    request = unu.task_limit_add(task_id=task_id, add_to_limit=limit)
    assert request["success"] == "true"
    request = unu.task_pause(task_id=task_id)
    assert request["success"] == "true"
