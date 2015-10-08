from Message.Parameters.Parameter import Parameter, ParameterType


class Current(Parameter):
    def __init__(self, amps=0.0):
        super(Current, self).__init__(value=amps, length=2, type=ParameterType.IEEEFloat, resolution=0.01)