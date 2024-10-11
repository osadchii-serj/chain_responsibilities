from technical_support_handler import TechnicalSupportHandler
from manager_support_handler import ManagerSupportHandler
from basic_support_handler import BasicSupportHandler
from interface import ComplaintHandler
from complaint import Complaint

from typing import List

complaints = [
    Complaint("У меня вопрос о продукте.", "basic"),
    Complaint("Программа выдает ошибку.", "technical"),
    Complaint("Серьезная проблема с заказом.", "serious"),
    Complaint("Не могу войти в аккаунт.", "unknown"),
]


def client_code(complaints: List):

    # Создаем обработчиков
    basic_handler = BasicSupportHandler()
    tech_handler = TechnicalSupportHandler()
    manager_handler = ManagerSupportHandler()

    # Устанавливаем цепочку обработчиков
    basic_handler.successor = tech_handler
    tech_handler.successor = manager_handler

    for complaint in complaints:
        print(f"Обработка жалобы: {complaint.message}")
        basic_handler.handle_complaint(complaint)


if __name__ == "__main__":
    client_code(complaints)
