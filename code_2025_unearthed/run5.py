from pybricks.parameters import Color, Stop
from pybricks.tools import run_task, wait,multitask
from pybricks.parameters import Axis, Direction, Port
from robot_config import HUB, CENTER_ATTACHMENT, FRONT_ATTACHMENT, DRIVE_BASE
from library import set_drivebase

from pybricks.pupdevices import Motor
from pybricks.parameters import Axis, Direction, Port

async def run5():
     #await HUB.speaker.beep()
    CENTER_ATTACHMENT.reconfigure(positive_direction=Direction.COUNTERCLOCKWISE,gears=None)
    DRIVE_BASE.use_gyro(True) 
    await wait(100)
    DRIVE_BASE.settings(straight_speed=400, straight_acceleration=1000, turn_rate=200, turn_acceleration=1000)
    
    await DRIVE_BASE.straight(-758)
    #wait DRIVE_BASE.turn(180)
    #await DRIVE_BASE.straight(-187)
    await DRIVE_BASE.turn(-96)
    await wait(100) 
    CENTER_ATTACHMENT.reset_angle(0)
    FRONT_ATTACHMENT.reset_angle(0) 
    DRIVE_BASE.settings(straight_speed=100, straight_acceleration=200, turn_rate=200, turn_acceleration=1000)
    await DRIVE_BASE.straight(125) 
    await wait(100) 
    await CENTER_ATTACHMENT.run_angle(800, 300)
    await FRONT_ATTACHMENT.run_angle(800, 40)
    await wait(100)
    await CENTER_ATTACHMENT.run_angle(800, -300)
    await DRIVE_BASE.turn(-2)
    await DRIVE_BASE.straight(-115)
    DRIVE_BASE.settings(straight_speed=600, straight_acceleration=1000, turn_rate=200, turn_acceleration=1000)
    await DRIVE_BASE.turn(41)
    #await CENTER_ATTACHMENT.run_angle(800, -305)
    await DRIVE_BASE.straight(317)
    #await DRIVE_BASE.turn(-2)
    #await DRIVE_BASE.straight(70)
    await multitask(CENTER_ATTACHMENT.run_angle(500, 490),)
    #await CENTER_ATTACHMENT.run_angle(800, 400)
    #await DRIVE_BASE.straight(-100)
    #await DRIVE_BASE.turn(35)
    #await DRIVE_BASE.straight(76)
    #await FRONT_ATTACHMENT.run_angle(800, -100)
    DRIVE_BASE.settings(straight_speed=800, straight_acceleration=1000, turn_rate=200, turn_acceleration=1000)
    await DRIVE_BASE.straight(-400)
    await DRIVE_BASE.turn(70)
    await DRIVE_BASE.straight(700)
    #await CENTER_ATTACHMENT.run_angle(800, -400)
    #await FRONT_ATTACHMENT.run_angle(800, -40)

    #await DRIVE_BASE.stop()
    DRIVE_BASE.use_gyro(False) 




if __name__ == "__main__":
    run_task(run5())
