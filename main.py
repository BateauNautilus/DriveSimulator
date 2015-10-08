#!/usr/bin/env python3
import time
from Message.CANMessage import MessageToCan
from Message.EnvironmentStatus import EnvironmentStatus
from Message.MotorStatus import MotorStatus
from Message.Parameters.Current import Current
from Message.Parameters.Humidity import Humidity
from Message.Parameters.Vibration import Vibration
from Message.Parameters.Voltage import Voltage
from Message.Parameters.WaterTemperature import WaterTemperature
from config import Config

from lib.pythoncan import can
from Message.Parameters.RPM import Rpm


tasks = {}


def main():
    bus = can.interface.Bus(channel=Config.getChannel(), bustype=Config.getBusType())
    print('start_transmit()')
    sendMotorStatusMessage()
    sendEnvironmentStatusMessage()
    while True:
        time.sleep(20)


def sendMotorStatusMessage():
    msg = MotorStatus(rpm=Rpm(5000), voltage=Voltage(12.5), current=Current(2), vibration=Vibration(0.2))
    canmsg = MessageToCan(msg, deviceId=Config.getDeviceId())
    tasks['motorStatus'] = can.send_periodic(Config.getChannel(), canmsg, msg.period)

def sendEnvironmentStatusMessage():
    msg = EnvironmentStatus(waterTemperature=WaterTemperature(5), humidity=Humidity(0.12))
    canmsg = MessageToCan(msg, deviceId=Config.getDeviceId())
    tasks['EnvironmentStatus'] = can.send_periodic(Config.getChannel(), canmsg, msg.period)


if __name__ == "__main__":
    main()