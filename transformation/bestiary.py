
from __future__ import division

from math import pi
from random import choice, uniform

from pyglet.window import key

from .component.shapes import ( Cube, Cuboid, CubeCorners, CubeCross, CubeFrame, CubeLattice, CubeRing, DualTetrahedron, Ring, RgbCubeCluster, Tetrahedron
)
from .component.slowmo import SlowMo
from .component.spinner import Spinner
from .component.wobblyorbit import Orbit
from .component.color import ( Color, red, orange, yellow, green, cyan, blue, purple, white, grey, black )
from .engine.gameitem import GameItem
from .geometry.orientation import Orientation
from .geometry.vec3 import Origin, Vec3, XAxis


def get_bestiary(world):
    bestiary = {}

    bestiary[key._1] = GameItem(
        shape=Tetrahedron(1.8, blue.variations(cyan)),
        position=Origin,
    )

    bestiary[key._2] = GameItem(
        shape=Cube(0.9, green.variations(purple)),
        position=Origin,
    )

    bestiary[key._3] = GameItem(
        shape=DualTetrahedron(1.8),
        position=Origin,
    )

    bestiary[key._4] = GameItem(
        shape=CubeCross(1, red, red.tinted(yellow)),
        position=Origin,
    )

    bestiary[key._5] = GameItem(
        shape=CubeCorners(1, yellow.tinted(white), yellow),
        position=Origin,
    )

    bestiary[key._6] = GameItem(
        shape=Ring(Cube(1, cyan.tinted(black).variations()), 2, 13),
        position=Origin,
    )

    bestiary[key._7] = GameItem(
        shape=Ring(
            DualTetrahedron(1, orange.tinted(black, 0.5), orange.tinted(black)),
            4,
            54,
        ),
        position=Origin,
        orientation=XAxis,
        spin=Spinner(speed=1),
    )

    bestiary[key._8] = GameItem(
        shape=CubeFrame(10, [grey.tinted(white)]),
        position=Origin,
    )

    bestiary[key._9] = GameItem(
        shape=RgbCubeCluster(1.0, 20, 4000),
        position=Origin,
    )

    edge = 40

    def camera_inside():
        return all(abs(dist) < edge/2 for dist in world.camera.position)

    bestiary[key._0] = GameItem(
        slowmo=SlowMo(camera_inside, 0.2),
        position=Origin,
        shape=CubeLattice(1, edge, 2, white),
    )

    return bestiary

