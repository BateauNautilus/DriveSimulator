from Message.Message import Message, MessageId


class MotorStatus(Message):
    def __init__(self, rpm=None, voltage=None, current=None, vibration=None):
        self.rpmParameter = rpm
        self.voltageParameter = voltage
        self.currentParameter = current
        self.vibrationParameter = vibration
        super(MotorStatus, self).__init__(id=MessageId.MotorStatus.value,
                                          parameters=[self.rpmParameter, self.voltageParameter, self.currentParameter,
                                                      self.vibrationParameter],
                                          period=2)
