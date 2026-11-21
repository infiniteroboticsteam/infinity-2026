from pybricks.tools import multitask, run_task, wait
from pybricks.parameters import Stop
from library import set_drivebase
from robot_config import DRIVE_BASE, LEFT_ATTACHMENT

async def M1():
	DRIVE_BASE.use_gyro(True)
	await wait(1000)
	await set_drivebase()	
	DRIVE_BASE.settings(
		straight_speed=400,
		straight_acceleration=200,
		turn_rate=600,
		turn_acceleration=600,
	)
	await set_drivebase()	
	print("Turning -20 degrees")
	await DRIVE_BASE.turn(-180)

	DRIVE_BASE.settings(
			straight_speed=400,
			straight_acceleration=200,
			turn_rate=100,
			turn_acceleration=100,
		)
	
	print("Turning -20 degrees")
	await DRIVE_BASE.turn(-180)
	

if __name__ == "__main__":
	run_task(M1())
