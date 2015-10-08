from Message.Parameters.Parameter import Parameter, ParameterType


class Rpm(Parameter):
    def __init__(self, rpm=0):
        super(Rpm, self).__init__(value=rpm, length=2, type=ParameterType.Integer, resolution=1)

