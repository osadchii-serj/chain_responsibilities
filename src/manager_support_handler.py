from interface import ComplaintHandler

from dataclasses import dataclass


@dataclass
class ManagerSupportHandler(ComplaintHandler):

    def handle_complaint(self, complaint: str):
        if complaint.level == "serious":
            print(f"Руководство: {complaint.message}")
        else:
            super().handle_complaint(complaint)
