from pybricks.parameters import Direction
from pybricks.tools import run_task, wait
from library import set_drivebase
from robot_config import DRIVE_BASE, LEFT_ATTACHMENT, RIGHT_ATTACHMENT


async def TEST():
    LEFT_ATTACHMENT.reconfigure(Direction.CLOCKWISE, gears=None)
    RIGHT_ATTACHMENT.reconfigure(Direction.CLOCKWISE, gears=None)
    DRIVE_BASE.settings(straight_speed=600, straight_acceleration=600)
    DRIVE_BASE.use_gyro(True)
    await wait(300)

    await DRIVE_BASE.straight(-100)
    DRIVE_BASE.use_gyro(False)

async def main():
    DRIVE_BASE.use_gyro(False)
    await set_drivebase()
    DRIVE_BASE.settings(
        straight_speed=700,
        straight_acceleration=900,
        turn_rate=100,
        turn_acceleration=400,
    )
    await DRIVE_BASE.straight(600)
    await wait(500)

if __name__ == "__main__":
    run_task(main())
