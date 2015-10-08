from Message.Message import Message, MessageId


class EnvironmentStatus(Message):
    def __init__(self, waterTemperature=None, humidity=None):
        self.waterTemperature = waterTemperature
        self.humidity = humidity
        super(EnvironmentStatus, self).__init__(id=MessageId.EnvironmentStatus.value,
                                                parameters=[self.waterTemperature, self.humidity],
                                                period=5)
