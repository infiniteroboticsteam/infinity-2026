from pybricks.tools import multitask, run_task, wait
from robot_config import DRIVE_RIGHT, LEFT_ATTACHMENT, RIGHT_ATTACHMENT

from library import set_drivebase
from robot_config import DRIVE_BASE


async def M5():
    
    await set_drivebase()
    DRIVE_BASE.settings(
        straight_speed=400,
        straight_acceleration=400,
        turn_rate=500,
        turn_acceleration=400,
    )
    DRIVE_BASE.use_gyro(True)
    
    await RIGHT_ATTACHMENT.run_angle(1000, -270)
    await DRIVE_BASE.straight(790),
    
    RIGHT_ATTACHMENT.control.limits(
        speed=1100,
        acceleration=20000,
        torque=1000,
    )
    await RIGHT_ATTACHMENT.run_angle(1000, 180)    
    await DRIVE_BASE.straight(-800),
    
    
if __name__ == "__main__":
    run_task(M5())