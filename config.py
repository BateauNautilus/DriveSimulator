import configparser
config = None


class Config(object):
    def __init__(self):
        self.create()

    @staticmethod
    def create():
        global config
        if config is None:
            config = configparser.ConfigParser()
            config.read('can.conf')
        return config

    @staticmethod
    def getDeviceId():
        return int(Config.create()['CAN']['device_id'])

    @staticmethod
    def getChannel():
        return Config.create()['CAN']['channel']

    @staticmethod
    def getBusType():
        return Config.create()['CAN']['bustype']

    @staticmethod
    def getInterface():
        return Config.create()['CAN']['interface']