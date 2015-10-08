from enum import Enum
from Message.Parameters import Parameter


class MessageId(Enum):
    Unknown = 0
    MotorStatus = 10
    EnvironmentStatus = 11


class Message(object):
    def __init__(self, id=0, parameters: Parameter=[], period=1):
        self.id = id
        self.parameters = parameters
        self.period = period