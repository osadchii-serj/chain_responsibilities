from interface import ComplaintHandler

from dataclasses import dataclass


@dataclass
class BasicSupportHandler(ComplaintHandler):

    def handle_complaint(self, complaint: str):
        if complaint.level == "basic":
            print(f"Базовая поддержка: {complaint.message}")
        else:
            super().handle_complaint(complaint)
