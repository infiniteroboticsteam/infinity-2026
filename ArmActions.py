from pybricks.tools import run_task
from library import set_drivebase
from pybricks.parameters import Color, Direction, Stop
from robot_config import DRIVE_BASE,LEFT_ATTACHMENT,RIGHT_ATTACHMENT

async def main():
    DRIVE_BASE.use_gyro(True)
    LEFT_ATTACHMENT.run_angle(180,-90)
    RIGHT_ATTACHMENT.run_angle(180,-90)

if __name__ == "__main__":
    run_task(main())
