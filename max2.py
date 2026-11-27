from pybricks.tools import run_task, wait
from library import set_drivebase
from robot_config import DRIVE_BASE, LEFT_ATTACHMENT, RIGHT_ATTACHMENT

async def main():

	await set_drivebase()
	DRIVE_BASE.settings(
		straight_speed=900,
		straight_acceleration=900,
		turn_rate=900,
		turn_acceleration=900,
	)
	DRIVE_BASE.use_gyro(True)
	#driving there
	#await DRIVE_BASE.arc(-500, 79)
	await RIGHT_ATTACHMENT.run_angle(1000, 90)
	await DRIVE_BASE.straight(-605)
	return




	await DRIVE_BASE.turn(-120)
	await DRIVE_BASE.straight(260)

	DRIVE_BASE.settings(
		turn_rate=400,
		turn_acceleration=400,
	)
	await DRIVE_BASE.turn(110)
	await wait (500)
	await DRIVE_BASE.straight(100)
	await wait(500)
	await DRIVE_BASE.straight(-10)
	await wait(500)
	await DRIVE_BASE.straight(50)
	await wait(500)
	await DRIVE_BASE.straight(-20)
	await wait(500)
	await DRIVE_BASE.straight(50)
	await wait(500)

if __name__ == "__main__":
	run_task(main()) 
