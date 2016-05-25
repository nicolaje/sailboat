#! /usr/bin/env morseexec

from morse.builder import *
from limprobable.builder.robots import Limprobable
from limprobable.builder.actuators import Sailboatactuator

limprobable = Limprobable()
limprobable.add_default_interface('socket')
limprobable.translate(z=4.2)

sailboatactuator = Sailboatactuator()
sailboatactuator.add_interface('socket')
limprobable.append(sailboatactuator)

env = Environment('water-1/water_scene', fastmode = False)
env.set_camera_location([-18.0, -6.7, 10.8])
env.set_camera_rotation([1.09, 0, -1.14])

