from abc import ABC, abstractmethod
from enum import Enum


class State(ABC):
    def return_enum(self) -> Enum:
        pass


class IdleState(State):
    def __str__(self):
        return "Idle"

    def return_enum(self) -> Enum:
        return States.IDLE


class AudioRecording(State):
    def __str__(self):
        return "AudioRecording"

    def return_enum(self) -> Enum:
        return States.RECORDING


class ProcessingState(State):
    def __str__(self):
        return "Processing"

    def return_enum(self) -> Enum:
        return States.PROCESSING


class DisplayingState(State):
    def __str__(self):
        return "Displaying"

    def return_enum(self) -> Enum:
        return States.DISPLAYING


class UnknownState(State):

    def __str__(self):
        return "Unknown"

    def return_enum(self) -> Enum:
        return States.UNKNOWN


class ErrorState(State):
    def __str__(self):
        return "Error"

    def return_enum(self) -> Enum:
        return States.ERROR


class States(Enum):
    IDLE = 0
    PROCESSING = 1
    DISPLAYING = 2
    UNKNOWN = 3
    ERROR = 4
    RECORDING = 5


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
        case States.RECORDING:
            return AudioRecording()
