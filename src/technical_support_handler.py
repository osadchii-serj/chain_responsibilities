from interface import ComplaintHandler

from dataclasses import dataclass


@dataclass
class TechnicalSupportHandler(ComplaintHandler):

    def handle_complaint(self, complaint: str):
        if complaint.level == "technical":
            print(f"Техническая поддержка: {complaint.message}")
        else:
            super().handle_complaint(complaint)
