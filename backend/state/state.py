from abc import ABC, abstractmethod
from enum import Enum


class State(ABC):
    def __int__(self):
        pass


class IdleState(State):
    def __str__(self):
        return "Idle"


class ProcessingState(State):
    def __str__(self):
        return "Processing"


class DisplayingState(State):
    def __str__(self):
        return "Displaying"


class UnknownState(State):
    def __str__(self):
        return "Unknown"


class ErrorState(State):
    def __str__(self):
        return "Error"


class States(Enum):
    IDLE = 0
    PROCESSING = 1
    DISPLAYING = 2
    UNKNOWN = 3
    ERROR = 4


def create_state(state: States | int) -> State:
    match state:
        case States.IDLE:
            return IdleState()
        case States.PROCESSING:
            return ProcessingState()
        case States.DISPLAYING:
            return DisplayingState()
        case States.UNKNOWN:
            return UnknownState()
        case States.ERROR:
            return ErrorState()
