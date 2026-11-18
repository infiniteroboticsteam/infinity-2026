

from pybricks.tools import multitask, run_task, wait

from library import set_drivebase
from robot_config import DRIVE_BASE, DRIVE_LEFT, DRIVE_RIGHT, LEFT_ATTACHMENT, RIGHT_ATTACHMENT


#WHEEL_DIAMETER = 56
#ONE_WHEEL_ROTATION = pi * WHEEL_DIAMETER


async def test_run():
	
	
	await set_drivebase()
	DRIVE_BASE.settings(
		straight_speed=300,
		straight_acceleration=500,
		turn_rate=600,
		turn_acceleration=600,
	)
	DRIVE_BASE.use_gyro(True)
	#RIGHT_ATTACHMENT.dc(100)
	await DRIVE_BASE.turn(15)
	await LEFT_ATTACHMENT.run_angle(100, -90)
	#await LEFT_ATTACHMENT.run_angle(300, 20)	
	#await DRIVE_BASE.turn(45)
	
	await DRIVE_BASE.straight(270)
	await LEFT_ATTACHMENT.run_angle(100, 40)
	await DRIVE_BASE.straight(-160)
	await set_drivebase()
	DRIVE_BASE.settings(
		straight_speed=300,
		straight_acceleration=500,
		turn_rate=50,
		turn_acceleration=50,
	)
	await DRIVE_BASE.turn(11)
	#await LEFT_ATTACHMENT.run_angle(50, -60),
	#await DRIVE_BASE.straight(-60)
	#await DRIVE_BASE.turn(-10)
	await multitask(
			LEFT_ATTACHMENT.run_angle(50, -60),
			DRIVE_BASE.straight(-60),
		)
	#await LEFT_ATTACHMENT.run_angle(50, 100)
	await set_drivebase()
	DRIVE_BASE.settings(
		straight_speed=800,
		straight_acceleration=800,
		turn_rate=500,
		turn_acceleration=500,
	)
	await DRIVE_BASE.turn(-40)
	await multitask(
		LEFT_ATTACHMENT.run_angle(50, 110),
		DRIVE_BASE.straight(710),
	)
	#await DRIVE_BASE.turn(-40)
	
	await DRIVE_BASE.turn(85)
	#await DRIVE_BASE.curve(-200,70)
	await DRIVE_BASE.straight(120)
	await RIGHT_ATTACHMENT.run_angle(50, -60)
	await multitask(
		RIGHT_ATTACHMENT.run_angle(50, 60),
		DRIVE_BASE.straight(-100),
	)
	await DRIVE_BASE.turn(18)
	await RIGHT_ATTACHMENT.run_angle(50, -60)
	await DRIVE_BASE.turn(60)
	await DRIVE_BASE.straight(600)
	await RIGHT_ATTACHMENT.run_angle(50, 60)
	"""
	
	await DRIVE_BASE.turn(-60)
	await DRIVE_BASE.straight(-800)
	"""

	#print("Driving forward one wheel rotation")
	#await DRIVE_BASE.straight(ONE_WHEEL_ROTATION)
	#print("Driving backward one wheel rotation")
	#await DRIVE_BASE.straight(-ONE_WHEEL_ROTATION
	#await DRIVE_BASE.straight(300)
	#await DRIVE_BASE.straight(-300)
	#await DRIVE_BASE.turn(90)
	#await DRIVE_BASE.straight(100)

if __name__ == "__main__":
	run_task(test_run())
