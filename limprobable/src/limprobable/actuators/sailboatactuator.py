import logging; logger = logging.getLogger("morse." + __name__)

import morse.core.actuator

from morse.core.services import service, async_service, interruptible
from morse.core import status
from morse.helpers.components import add_data, add_property

class Sailboatactuator(morse.core.actuator.Actuator):
    """Write here the general documentation of your actuator.
    It will appear in the generated online documentation.
    """
    _name = "Sailboatactuator"
    _short_desc = "State equations for a Robotic Sailboat"

    # define here the data fields required by your actuator
    # format is: field name, initial value, type, description
    add_data('sail_angle', 0, 'float', 'Angle of the sail')
    add_data('rudder_angle', 0, 'float', 'Angle of the rudder')

    def __init__(self, obj, parent=None):
        logger.info("%s initialization" % obj.name)
        # Call the constructor of the parent class
        morse.core.actuator.Actuator.__init__(self, obj, parent)

        # Do here actuator specific initializations

        self._target_count = 0 # dummy internal variable, for testing purposes

        logger.info('Component initialized')

    def default_action(self):
        """ Main loop of the actuator.

        Implements the component behaviour
        """
        pass
