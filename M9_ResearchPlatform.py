from pybricks.tools import multitask, run_task, wait
from robot_config import DRIVE_RIGHT, LEFT_ATTACHMENT, RIGHT_ATTACHMENT

from library import set_drivebase
from robot_config import DRIVE_BASE


async def M9():
    
    await set_drivebase()
    DRIVE_BASE.settings(
        straight_speed=400,
        straight_acceleration=400,
        turn_rate=500,
        turn_acceleration=400,
    )
    DRIVE_BASE.use_gyro(True)
    await DRIVE_BASE.arc(750,52)
    await DRIVE_RIGHT.run_angle(300,220)
        
    await DRIVE_BASE.straight(-100)

    #DRIVE_BASE.distance_control.limits(speed=500, acceleration=800, torque=1000)

    await DRIVE_BASE.straight(600)
    await DRIVE_BASE.straight(-30)
    await DRIVE_BASE.straight(30)
    await set_drivebase()
    DRIVE_BASE.settings(
        straight_speed=100,
        straight_acceleration=100,
        turn_rate=500,
        turn_acceleration=400,
    )
        
    await DRIVE_BASE.straight(-150)
    await DRIVE_BASE.turn(40)
    await set_drivebase()
    DRIVE_BASE.settings(
    straight_speed=800,
    straight_acceleration=800,
    turn_rate=500,
    turn_acceleration=400,
)
    await DRIVE_BASE.straight(-800)
    #await DRIVE_BASE.arc(-1000,-70)
    #await RIGHT_ATTACHMENT.r5n_angle(1000, -180)
    #await RIGHT_ATTACHMENT.run_angle(1000, -90),
    #await DRIVE_BASE.straight(790),
    
    #RIGHT_ATTACHMENT.control.limits(
    #    speed=1100,
    #    acceleration=20000,
    #    torque=1000,
    #)
    #await RIGHT_ATTACHMENT.run_angle(1000, 180)    
    #await DRIVE_BASE.straight(-800),
    
    
if __name__ == "__main__":
    run_task(M9())