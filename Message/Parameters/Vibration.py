from Message.Parameters.Parameter import Parameter, ParameterType


class Vibration(Parameter):
    def __init__(self, vibration=0.0):
        super(Vibration, self).__init__(value=vibration, length=2, type=ParameterType.IEEEFloat, resolution=0.01)

