
from pybricks.tools import run_task,multitask
from robot_config import LEFT_ATTACHMENT,RIGHT_ATTACHMENT

from library import set_drivebase
from robot_config import DRIVE_BASE


async def main():
    await multitask(RIGHT_ATTACHMENT.reset_angle(45),LEFT_ATTACHMENT.reset_angle(45))

if __name__ == "__main__":
    run_task(main())