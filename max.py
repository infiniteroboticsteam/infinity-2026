from pybricks.tools import run_task, wait
from library import set_drivebase
from robot_config import DRIVE_BASE, LEFT_ATTACHMENT, RIGHT_ATTACHMENT

async def main():

	await set_drivebase()
	DRIVE_BASE.settings(
		straight_speed=500,
		straight_acceleration=900,
		turn_rate=100,
		turn_acceleration=400,
	)
	DRIVE_BASE.use_gyro(False)
	#driving there
	#await DRIVE_BASE.arc(-500, 79)
	await RIGHT_ATTACHMENT.run_angle(1000, 90)
	await DRIVE_BASE.straight(630)
	await DRIVE_BASE.turn(-105)
	await DRIVE_BASE.straight(260)
	await DRIVE_BASE.turn(105)
	DRIVE_BASE.settings(
		straight_speed=900,
		straight_acceleration=900,
		turn_rate=900,
		turn_acceleration=900,
	)
	await DRIVE_BASE.straight(110)
	await RIGHT_ATTACHMENT.run_angle(1000, -50)
	await wait(200)
	
	await DRIVE_BASE.straight(10)
	await wait(200)
	await DRIVE_BASE.straight(-30)
	await wait(200)
	await DRIVE_BASE.straight(-10)
	DRIVE_BASE.settings(
		straight_speed=900,
		straight_acceleration=900,
		turn_rate=100,
		turn_acceleration=400,
	)

	await DRIVE_BASE.straight(97.5)

	DRIVE_BASE.settings(
		straight_speed=350,
		straight_acceleration=400,
		turn_rate=100,
		turn_acceleration=400,
	)
	
	await DRIVE_BASE.straight(-10)
	DRIVE_BASE.settings(
		straight_speed=900,
		straight_acceleration=900,
		turn_rate=100,
		turn_acceleration=400,
	)
	await DRIVE_BASE.straight(50)
	DRIVE_BASE.settings(
		straight_speed=140,
		straight_acceleration=400,
		turn_rate=100,
		turn_acceleration=400,
	)
	await RIGHT_ATTACHMENT.run_angle(1000, -50)
	await DRIVE_BASE.straight(-50)
	await wait(500)
	await DRIVE_BASE.straight(-130)
	DRIVE_BASE.settings(
		straight_speed=800,
		straight_acceleration=700,
		turn_rate=100,
		turn_acceleration=400,
	)
	await DRIVE_BASE.turn(180)
	await DRIVE_BASE.straight(700)

if __name__ == "__main__":
	run_task(main()) 
