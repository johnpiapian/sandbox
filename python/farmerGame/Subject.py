from enum import Enum
from typing import List


class SubjectType(Enum):
    FARMER = 0
    FOX = 1
    CHICKEN = 2
    GRAIN = 3


class Subject:
    def __init__(self, subject_type: SubjectType, actors: List[SubjectType] = []):
        self.subject_type = subject_type
        self.edible = actors

    def set_edible(self, actors: List[SubjectType] = []):
        self.edible = actors

    def __str__(self):
        return self.subject_type.name