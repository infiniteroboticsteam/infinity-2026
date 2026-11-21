
from pybricks.tools import multitask, run_task, wait
from robot_config import DRIVE_RIGHT, LEFT_ATTACHMENT, RIGHT_ATTACHMENT

from library import set_drivebase
from robot_config import DRIVE_BASE


async def M13():
    await set_drivebase()
    DRIVE_BASE.settings(
        straight_speed=500,
        straight_acceleration=400,
        turn_rate=600,
        turn_acceleration=600,
    )
    DRIVE_BASE.use_gyro(True)
    await DRIVE_BASE.straight(720)
    await DRIVE_BASE.turn(45)
    await DRIVE_BASE.straight(250)
    await DRIVE_BASE.straight(-250)
    await DRIVE_BASE.turn(-60)

    await multitask(
        LEFT_ATTACHMENT.run_target(360, 50),
        RIGHT_ATTACHMENT.run_target(360, 40),
        DRIVE_BASE.straight(-800),
    )
    
if __name__ == "__main__":
    run_task(M13())