
from pybricks.tools import multitask, run_task, wait
from robot_config import DRIVE_LEFT, DRIVE_RIGHT, LEFT_ATTACHMENT, RIGHT_ATTACHMENT

from library import set_drivebase
from robot_config import DRIVE_BASE


async def ResetArmPosition():
    await multitask(
        LEFT_ATTACHMENT.run_target(360, 44),
        RIGHT_ATTACHMENT.run_target(360, 29),
    )
if __name__ == "__main__":
    run_task(ResetArmPosition())