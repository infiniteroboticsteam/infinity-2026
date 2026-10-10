
from pybricks.tools import run_task
from robot_config import LEFT_ATTACHMENT

from library import set_drivebase
from robot_config import DRIVE_BASE


async def main():
    await set_drivebase()
    await DRIVE_BASE.straight(390)
    await DRIVE_BASE.arc(55, 10)
    await DRIVE_BASE.straight(45)
    await LEFT_ATTACHMENT.run_angle(80,40)

if __name__ == "__main__":
    run_task(main())