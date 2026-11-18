from math import pi

from pybricks.tools import multitask, run_task

from library import SPEED, set_drivebase
from robot_config import (
    DRIVE_BASE,
    LEFT_ATTACHMENT,
    LEFT_COLOR_SENSOR,
    RIGHT_ATTACHMENT,
    RIGHT_COLOR_SENSOR,
)

WHEEL_DIAMETER = 56
ONE_WHEEL_ROTATION = pi * WHEEL_DIAMETER


async def M6():
    SPEED = 200
    set_drivebase()
    DRIVE_BASE.settings(
        straight_speed=500,
        straight_acceleration=200,
        turn_rate=200,
        turn_acceleration=200,
    )

    # separator between missions
    await DRIVE_BASE.straight(-990.4206741)  # step 1 move forward
    await DRIVE_BASE.turn(51)  # step 4 turn toward leaves
    await DRIVE_BASE.straight(-420.9767)  # step 5 move forward to leaves
    await DRIVE_BASE.turn(-44.75)  # step 8 turn towards handle

    DRIVE_BASE.settings(
        straight_speed=100,
        straight_acceleration=200,
        turn_rate=200,
        turn_acceleration=200,
    )
    await LEFT_COLOR_SENSOR.color()
    await DRIVE_BASE.straight(-110)  # step 9 push handle
    DRIVE_BASE.settings(
        straight_speed=500,
        straight_acceleration=200,
        turn_rate=200,
        turn_acceleration=200,
    )
    await DRIVE_BASE.straight(35)  # step 10 back up from handle

    DRIVE_BASE.use_gyro(True)
    await DRIVE_BASE.turn(83.67)  # step 11 turn away from leaves
    await DRIVE_BASE.straight(-1000)  # step 12 go home


if __name__ == "__main__":
    run_task(M6())
