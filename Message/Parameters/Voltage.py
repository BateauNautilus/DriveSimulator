from Message.Parameters.Parameter import Parameter, ParameterType


class Voltage(Parameter):
    def __init__(self, volts=0.0):
        super(Voltage, self).__init__(value=volts, length=2, type=ParameterType.IEEEFloat, resolution=0.01)

