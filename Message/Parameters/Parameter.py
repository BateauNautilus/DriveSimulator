from enum import Enum


class ParameterType(Enum):
    Unknown = 0
    Ascii = 1
    Temperature = 6
    Integer = 8
    IEEEFloat = 13


class Parameter(object):
    def __init__(self, value=None, type=ParameterType.Unknown, length=0, units='', resolution=0, signed=False):
        self.type = type
        self.length = length
        self.resolution = resolution
        self.signed = signed
        self.units = units
        self.value = value


