from pybricks.tools import run_task, wait
from robot_config import DRIVE_BASE, HUB, CENTER_ATTACHMENT
from library import set_drivebase
from pybricks.tools import run_task, wait
from pybricks.parameters import Direction, Port, Stop
from pybricks.pupdevices import Motor




#use this function as a template to define how to drive the base
async def run4():
    #await set_drivebase()
    #CENTER_ATTACHMENT = Motor(Port.D, Direction.CLOCKWISE)
    CENTER_ATTACHMENT.reconfigure(positive_direction=Direction.COUNTERCLOCKWISE,gears=None)
    #CENTER_ATTACHMENT.reconfigure(positive_direction=Direction.COUNTERCLOCKWISE, gears=[12,36])
    # Turn on Gyro
    DRIVE_BASE.use_gyro(True)


    #await CENTER_ATTACHMENT.run_angle(100,120)
    DRIVE_BASE.settings(straight_speed=700,straight_acceleration=650)
    await DRIVE_BASE.straight(-600)
    #await DRIVE_BASE.straight(-350) #to be deleted at coach's house
    await DRIVE_BASE.straight(140)
    DRIVE_BASE.settings(straight_speed=360,straight_acceleration=360)
    await DRIVE_BASE.turn(-90)
    await DRIVE_BASE.straight(30)
    await CENTER_ATTACHMENT.run_angle(150,-120*1.56)
    await wait(500)
    await CENTER_ATTACHMENT.run_angle(20,-8*1.56)
    await wait(500)
    DRIVE_BASE.settings(straight_speed=600,straight_acceleration=650)
    await DRIVE_BASE.straight(-82)
    DRIVE_BASE.settings(straight_speed=360,straight_acceleration=360)
    await CENTER_ATTACHMENT.run_angle(500,105*1.57)
    #return
    await wait(500)
    await DRIVE_BASE.straight(240) # move back
    DRIVE_BASE.settings(straight_speed=250,straight_acceleration=250)
    await DRIVE_BASE.turn(-135) #End of Mission 1
    await DRIVE_BASE.straight(266)
    #await DRIVE_BASE.straight(200) #To be deleted at coach's house
    await CENTER_ATTACHMENT.run_angle(100,-126.7, then = Stop.COAST)
    #await DRIVE_BASE.straight(-120)
    DRIVE_BASE.settings(straight_speed=500,straight_acceleration=500)
    #await DRIVE_BASE.turn(30)
    await DRIVE_BASE.straight(-270)
    await DRIVE_BASE.turn(-100)
    DRIVE_BASE.settings(straight_speed=900,straight_acceleration=900)
    await DRIVE_BASE.straight(530)
    #await DRIVE_BASE.stop()
    DRIVE_BASE.use_gyro(False)
    



if __name__ == "__main__":
    run_task(run4())