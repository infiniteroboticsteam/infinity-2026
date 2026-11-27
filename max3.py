
from pybricks.tools import multitask, run_task, wait
from robot_config import DRIVE_RIGHT, LEFT_ATTACHMENT, RIGHT_ATTACHMENT, DRIVE_LEFT

from library import set_drivebase
from robot_config import DRIVE_BASE


async def M13():
    await set_drivebase()
    DRIVE_BASE.settings(
        straight_speed=400,
        straight_acceleration=900,
        turn_rate=400,
        turn_acceleration=900,
    )
    DRIVE_BASE.use_gyro(True)
    await LEFT_ATTACHMENT.run_angle(1000, 90)
    await DRIVE_BASE.arc(-487.5, -70)
    await DRIVE_BASE.arc(100, -65)
    await DRIVE_BASE.straight(-300)
    await wait(500)
    await LEFT_ATTACHMENT.run_angle(10000, -50)
    await wait (500)
    DRIVE_BASE.settings(
        straight_speed=100,
        straight_acceleration=100,
    )

    await DRIVE_BASE.arc(500,30)
    
    DRIVE_BASE.settings(
        straight_speed=400,
        straight_acceleration=900,
    )
    

if __name__ == "__main__":
    run_task(M13())