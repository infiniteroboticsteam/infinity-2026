
from pybricks.tools import multitask, run_task, wait

from library import set_drivebase
from robot_config import DRIVE_BASE, DRIVE_LEFT, DRIVE_RIGHT, LEFT_ATTACHMENT, RIGHT_ATTACHMENT


#WHEEL_DIAMETER = 56
#ONE_WHEEL_ROTATION = pi * WHEEL_DIAMETER


async def test_run():
	DRIVE_BASE.use_gyro(True)
	await wait(1000)
	await set_drivebase()
	DRIVE_BASE.settings(
		straight_speed=900,
		straight_acceleration=500,
		turn_rate=600,
		turn_acceleration=600,
	)

	await DRIVE_BASE.straight(690)
	await DRIVE_BASE.turn(45)
	await DRIVE_BASE.straight(300)
	await DRIVE_BASE.turn(-53)
	await DRIVE_BASE.straight(-800)
	
