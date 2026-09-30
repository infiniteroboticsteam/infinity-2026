from pybricks.tools import multitask, run_task, wait
from pybricks.parameters import Direction,Stop
from robot_config import CENTER_ATTACHMENT, DRIVE_BASE, FRONT_ATTACHMENT
from library import set_drivebase

async def run3():
    CENTER_ATTACHMENT.reconfigure(Direction.COUNTERCLOCKWISE,gears=[12,36])
    FRONT_ATTACHMENT.reconfigure(Direction.CLOCKWISE,gears=[28,36])
    await set_drivebase()
    DRIVE_BASE.settings(straight_speed=700, straight_acceleration=700)
    DRIVE_BASE.use_gyro(True)
    await wait(100)

    await DRIVE_BASE.straight(-718.7)
    await DRIVE_BASE.turn(-90)
    await DRIVE_BASE.straight(-150)
    await DRIVE_BASE.turn(-15)
    #pull up artifacts
    await FRONT_ATTACHMENT.run_angle(999, 1000, then=Stop.COAST)

    await DRIVE_BASE.turn(15)
    await DRIVE_BASE.straight(100)
    await DRIVE_BASE.turn(90)
    await DRIVE_BASE.straight(-600)


    await DRIVE_BASE.turn(-90)
    await DRIVE_BASE.straight(-170)
    await DRIVE_BASE.turn(90)

    await DRIVE_BASE.straight(70)

    await CENTER_ATTACHMENT.run_angle(550, -140)
    await DRIVE_BASE.straight(-65)
    await CENTER_ATTACHMENT.run_angle(550, 140,then=Stop.COAST)
    #push ship up and drop flag
    await multitask(DRIVE_BASE.straight(200),
                    FRONT_ATTACHMENT.run_angle(999,1500,then=Stop.COAST)
                    )
    #await DRIVE_BASE.straight(200)
    #await FRONT_ATTACHMENT.run_angle(999,3000)

    DRIVE_BASE.settings(straight_speed=900, straight_acceleration=900)
    await DRIVE_BASE.straight(-630)

    DRIVE_BASE.use_gyro(False) 
  


if __name__ == "__main__":
    run_task(run3())