from morse.builder.creator import ActuatorCreator

class Sailboatactuator(ActuatorCreator):
    _classpath = "limprobable.actuators.sailboatactuator.Sailboatactuator"
    _blendname = "sailboatactuator"

    def __init__(self, name=None):
        ActuatorCreator.__init__(self, name)

