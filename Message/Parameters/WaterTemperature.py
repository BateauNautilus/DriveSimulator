from Message.Parameters.Parameter import Parameter, ParameterType


class WaterTemperature(Parameter):
    def __init__(self, temperature=0.0):
        super(WaterTemperature, self).__init__(value=temperature, length=2, type=ParameterType.Temperature, resolution=0.01)

