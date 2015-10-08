import struct
from Message.Parameters.Parameter import Parameter, ParameterType
from lib.float16.float16 import Float16Compressor
from lib.pythoncan.can.message import Message as pyMessage
from Message.Message import Message


def MessageToCan(message: Message, deviceId=0) -> pyMessage:
    pym = pyMessage(arbitration_id=combine_messageId_int(deviceId, message.id))
    messageByte = b''
    byteIndex=0
    for param in message.parameters:
        bb = typeConverter.parameterConvert(param)
        messageByte = b''.join([messageByte, bb])
    pym.data = messageByte
    return pym


def combine_messageId_byte(deviceId, messageId) -> bytes:
    return bytes([deviceId & 0x7, (messageId & 0x0F0) >> 4, messageId & 0x00F])


def combine_messageId_int(deviceId, messageId) -> int:
    byte = combine_messageId_byte(deviceId, messageId)
    return int((byte[0] << 8) + (byte[1] << 4) + byte[2])


class typeConverter(object):
    @staticmethod
    def parameterConvert(param: Parameter) -> bytes:
        if param is None:
            return bytearray([])
        if param.type is ParameterType.IEEEFloat:
            return typeConverter._paramToIEEEFloat(param)
        elif param.type is ParameterType.Integer:
            return typeConverter._fromInteger(param)
        elif param.type is ParameterType.Ascii:
            return typeConverter._paramToAscii(param)
        elif param.type is ParameterType.Temperature:
            return typeConverter._paramToIEEEFloat(param)

    @staticmethod
    def _IEEEFloatToParameter(value: bytes, param: Parameter) -> float:
        param.value = typeConverter._IEEEFloatToFloat(value)

    @staticmethod
    def _IEEEFloatToFloat(value: bytes) -> float:
        number = int(((value[0] & 0xFF) << 8) | (value[1] & 0xFF))
        temp = Float16Compressor.decompress(number)
        bytestr = struct.pack('I', temp)
        f = struct.unpack('f', bytestr)[0]
        return f

    @staticmethod
    def _paramToIEEEFloat(param: Parameter):
        return typeConverter._toIEEEFloat(param.value)

    @staticmethod
    def _toIEEEFloat(value: float) -> bytes:
        bitval = Float16Compressor.compress(value)
        return bytes([(bitval & 0xFF00) >> 8, bitval & 0xFF])

    @staticmethod
    def _fromInteger(param: Parameter) -> bytes:
        return bytes([(param.value & 0xFF00) >> 8, param.value & 0xFF])

    @staticmethod
    def _textToAscii(text: str) -> bytes:
        return bytes([ord(c) for c in text])

    @staticmethod
    def _paramToAscii(param: Parameter) -> bytes:
        return typeConverter._textToAscii(param.value)

    @staticmethod
    def _AsciiToText(value:bytes) -> str:
        msg=[chr(int(b)) for b in value]
        return "".join(msg)

