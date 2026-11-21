from pybricks.parameters import Color, Direction, Stop
from pybricks.tools import multitask, run_task, wait
from robot_config import RIGHT_ATTACHMENT, DRIVE_BASE, HUB, LEFT_ATTACHMENT

async def reset_attachment_angels():
    LEFT_ATTACHMENT.reconfigure(Direction.CLOCKWISE,gears=None)
    RIGHT_ATTACHMENT.reconfigure(Direction.CLOCKWISE,gears=None)
    initial_angle=-90
    await multitask(LEFT_ATTACHMENT.run_target(300,initial_angle),
                    RIGHT_ATTACHMENT.run_target(300,initial_angle))
    return

async def run2():
    LEFT_ATTACHMENT.reconfigure(Direction.CLOCKWISE,gears=[12,24])
    RIGHT_ATTACHMENT.reconfigure(Direction.CLOCKWISE,gears=[12,24])
    DRIVE_BASE.settings(straight_speed=600, straight_acceleration=600)
    DRIVE_BASE.use_gyro(True)
    await wait(300)

   # await multitask (DRIVE_BASE.straight(394), RIGHT_ATTACHMENT.run_angle(600,-10),
    #                 LEFT_ATTACHMENT.run_angle(600,15))
    await DRIVE_BASE.straight(394)
    
    #await wait(5)
    await DRIVE_BASE.arc(375,27)
    #await DRIVE_BASE.straight(2)
    #await RIGHT_ATTATCHMENT.
    await multitask (LEFT_ATTACHMENT.run_angle(600,20),
                     RIGHT_ATTACHMENT.run_angle(600,37))
    #await LEFT_ATTACHMENT.run_angle(100,40)
    return
    await DRIVE_BASE.straight(-60)
    await DRIVE_BASE.straight(50)
    await DRIVE_BASE.turn(-21)  
    await DRIVE_BASE.turn(1)

    await DRIVE_BASE.straight(-200)
    #await DRIVE_BASE.turn(15)
    
    return
    #await multitask(LEFT_ATTACHMENT.run_angle(600,-15),
       #             RIGHT_ATTACHMENT.run_angle(600,15))
    await multitask(LEFT_ATTACHMENT.run_target(0),RIGHT_ATTACHMENT.run_target(0))
    #await multitask(DRIVE_BASE.turn(-15), LEFT_ATTACHMENT.run_angle(600,-20))
    #await LEFT_ATTACHMENT.run_angle(600,-0)
    await DRIVE_BASE.straight(-290)
    #await DRIVE_BASE.straight(-100)
    await multitask(RIGHT_ATTACHMENT.run_target(0),LEFT_ATTACHMENT.run_target(0))
    return
    await DRIVE_BASE.turn(-20) 
    await RIGHT_ATTACHMENT.run_angle(600,-30)
    #await wait(500)
    await multitask (DRIVE_BASE.straight(290),
                    LEFT_ATTACHMENT.run_angle(600,-200))
    await DRIVE_BASE.turn(-10)
    await DRIVE_BASE.straight(100)
    await DRIVE_BASE.turn(27)
    await multitask (DRIVE_BASE.straight(260), 
                     RIGHT_ATTACHMENT.run_angle(600,-20))
    await RIGHT_ATTACHMENT.run_angle(600,95)
    await RIGHT_ATTACHMENT.run_angle(600,-95)
    await DRIVE_BASE.straight(-800)

    DRIVE_BASE.use_gyro(False) 


if __name__ == "__main__":
    run_task(run2())
