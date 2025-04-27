from abc import ABC, abstractmethod
from typing import List
from app.models.shift import Shift

class ShiftRepository(ABC):
    @abstractmethod
    def list_shifts(self, employee_id: int) -> List[Shift]:
        pass

    @abstractmethod
    def add_shift(self, employee_id: int, start_time, end_time) -> Shift:
        pass