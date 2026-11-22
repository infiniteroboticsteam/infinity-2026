

from pybricks.tools import multitask, run_task, wait

from library import set_drivebase
from robot_config import DRIVE_BASE, DRIVE_LEFT, DRIVE_RIGHT, LEFT_ATTACHMENT, RIGHT_ATTACHMENT


#WHEEL_DIAMETER = 56
#ONE_WHEEL_ROTATION = pi * WHEEL_DIAMETER


async def M12():
	
	
	await set_drivebase()
	DRIVE_BASE.settings(
		straight_speed=500,
		straight_acceleration=500,
		turn_rate=600,
		turn_acceleration=600,
	)
	DRIVE_BASE.use_gyro(True)

	"""
	await DRIVE_BASE.arc(1200, 25)
	await RIGHT_ATTACHMENT.run_angle(50, -20)
	await DRIVE_RIGHT.run_angle(50,-75)
	await multitask(
		DRIVE_BASE.straight(-100),
		RIGHT_ATTACHMENT.run_angle(50,10),
	)

	"""
	await DRIVE_BASE.straight(350)
	await RIGHT_ATTACHMENT.run_angle(50, -50)
	await wait(2000)
	await multitask(
		RIGHT_ATTACHMENT.run_angle(50, 70),
		DRIVE_BASE.straight(-36),
	)
	#await DRIVE_BASE.straight(-40)
	
	
	await set_drivebase()
	DRIVE_BASE.settings(
		straight_speed=500,
		straight_acceleration=100,
		turn_rate=600,
		turn_acceleration=600,
	)
	await DRIVE_BASE.straight(-260)
	#await RIGHT_ATTACHMENT.run_angle(50, 40)
	#await DRIVE_BASE.turn(-30)
	#await DRIVE_BASE.straight(-100)
	
if __name__ == "__main__":
	run_task(M12())
