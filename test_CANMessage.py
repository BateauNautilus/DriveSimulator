import unittest
from bigfloat import *
import struct
from Message.CANMessage import combine_messageId_byte,combine_messageId_int, MessageToCan, typeConverter
from Message.MotorStatus import MotorStatus
from Message.Parameters.Current import Current
from Message.Parameters.RPM import Rpm
from Message.Parameters.Vibration import Vibration
from Message.Parameters.Voltage import Voltage
from lib.float16.float16 import Float16Compressor


class TestCanMessage(unittest.TestCase):
    def test_combine_messageid(self):
        self.assertEqual(bytes([0x1, 0xF, 0xF]), combine_messageId_byte(1, 255))
        self.assertEqual(bytes([0x7, 0xF, 0xF]), combine_messageId_byte(7, 255))
        self.assertEqual(bytes([0x7, 0x0, 0x0]), combine_messageId_byte(7, 0))
        self.assertEqual(bytes([0x7, 0x0, 0xF]), combine_messageId_byte(7, 15))

    def test_combine_messageid_int(self):
        self.assertEqual(511, combine_messageId_int(1, 255))

    def test_motorStatusMessageByte(self):
        msg = MotorStatus(rpm=Rpm(2000), voltage=Voltage(5.5), current=Current(1), vibration=Vibration(0))
        canmsg = MessageToCan(msg, 3)
        self.assertEqual(0x30A, canmsg.arbitration_id)
        bit=typeConverter._toIEEEFloat(0)
        self.assertEqual(bytes([0x07, 0xd0, 0x45, 0x80, 0x3c, 0x00, 0x00, 0x00]), canmsg.data)

    def test_ascii(self):
        self.assertEqual(bytes([0x74, 0x65, 0x73, 0x74]), typeConverter._textToAscii("test"))
        self.assertEqual(bytes([0x54, 0x45, 0x53, 0x54]), typeConverter._textToAscii("TEST"))
        self.assertEqual("test", typeConverter._AsciiToText(bytes([0x74, 0x65, 0x73, 0x74])))

    def test_ieee754(self):
        self.assertEqual(bytes([0b00111100, 0x0]), typeConverter._toIEEEFloat(1))
        self.assertEqual(bytes([0b11000000, 0x0]), typeConverter._toIEEEFloat(-2))
        self.assertEqual(bytes([0b11000000, 0x0]), typeConverter._toIEEEFloat(-2))
        self.assertEqual(-2, typeConverter._IEEEFloatToFloat(bytes([0b11000000, 0x0])))




if __name__ == '__main__':
    unittest.main()
