
from pybricks.tools import multitask, run_task, wait
from robot_config import DRIVE_RIGHT, LEFT_ATTACHMENT, RIGHT_ATTACHMENT, DRIVE_LEFT

from library import set_drivebase
from robot_config import DRIVE_BASE


async def MotorAngleTest():
    # 1. Total accumulated angle (e.g., 720, -45)
    total_angle = RIGHT_ATTACHMENT.angle()

    # 2. Absolute angle between 0 and 359 degrees
    absolute_angle = RIGHT_ATTACHMENT.angle() % 360

    # 3. Wrapped angle between -180 and 179 degrees
    wrapped_angle = (RIGHT_ATTACHMENT.angle() + 180) % 360 - 180

    print(f"Total: {total_angle} | Abs: {absolute_angle} | Wrapped: {wrapped_angle}")
    wait(100)
    
    
if __name__ == "__main__":
    run_task(MotorAngleTest())


   