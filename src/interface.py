from abc import ABC, abstractmethod

from dataclasses import dataclass


class ComplaintHandler(ABC):

    successor: object = None

    @abstractmethod
    def handle_complaint(self, complaint: str):
        if self.successor:
            self.successor.handle_complaint(complaint)
