
from pybricks.tools import multitask, run_task, wait
from robot_config import DRIVE_RIGHT, LEFT_ATTACHMENT, RIGHT_ATTACHMENT

from library import set_drivebase
from robot_config import DRIVE_BASE


async def ResetArmPosition():
    await RIGHT_ATTACHMENT.run_target(900,  45)
    #await DRIVE_BASE.turn(45)
    #
    #await DRIVE_BASE.curve(-900, 50)
    """
    await multitask(
            RIGHT_ATTACHMENT.run_angle(360, 180),
     
    )

    await DRIVE_BASE.turn(-48)
    await wait(1500)
    await DRIVE_BASE.straight(130)
    await RIGHT_ATTACHMENT.run_angle(360, -60)
    await DRIVE_BASE.curve(-350, -160)
    """
if __name__ == "__main__":
    run_task(ResetArmPosition())