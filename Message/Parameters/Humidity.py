from Message.Parameters.Parameter import Parameter, ParameterType


class Humidity(Parameter):
    def __init__(self, humidity=0.0):
        super(Humidity, self).__init__(value=humidity, length=2, type=ParameterType.IEEEFloat, resolution=0.01)

